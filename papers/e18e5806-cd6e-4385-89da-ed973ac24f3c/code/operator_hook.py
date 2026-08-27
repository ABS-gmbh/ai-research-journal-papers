import numpy as np

def apply_operator(ctx) -> None:
    state = ctx.state
    
    # Initialize rho (log_sigma) and momentum if not present
    if 'rho' not in state:
        state['rho'] = -3.0
        state['rho_momentum'] = 0.0
    
    # Extract hyperparameters
    lr = ctx.optimizer.param_groups[0]['lr']
    lambda_ent = 0.01
    momentum_coef = 0.9
    
    # Sample epsilon using tensor-valued randomness (same device/dtype as target)
    # This fixes the CUDA tensor error - use ctx.randn_like instead of numpy
    epsilon = ctx.randn_like(ctx.target)
    
    if ctx.condition == 'proposed':
        with ctx.torch.no_grad():
            # Compute sigma = exp(rho) with numerical safeguard
            rho = state['rho']
            sigma = float(np.exp(rho) + 1e-8)
            
            # Apply multiplicative weight noise: W_tilde = W + W * sigma * epsilon
            ctx.target += ctx.target * sigma * epsilon
            
            # Update rho with momentum (entropy maximization)
            # Loss includes -lambda * rho, so gradient w.r.t. rho is -lambda
            # For maximization: rho += lr * lambda
            rho_grad = -lambda_ent
            
            # Clip rho gradient to [-1.0, 1.0]
            rho_grad = float(np.clip(rho_grad, -1.0, 1.0))
            
            rho_momentum = momentum_coef * state['rho_momentum'] + rho_grad
            rho = rho - lr * rho_momentum
            
            # Clip rho parameter to [-5.0, 1.0]
            rho = float(np.clip(rho, -5.0, 1.0))
            
            state['rho'] = rho
            state['rho_momentum'] = rho_momentum
        
    elif ctx.condition == 'baseline_1':
        # Identity no-op: consume RNG but no modifications
        # No weight modification, no rho update
        pass
        
    elif ctx.condition == 'negative_control_1':
        # Entropy minimization (opposite sign on rho update)
        with ctx.torch.no_grad():
            rho = state['rho']
            sigma = float(np.exp(rho) + 1e-8)
            
            # Apply multiplicative weight noise
            ctx.target += ctx.target * sigma * epsilon
            
            # Minimize entropy: opposite gradient direction
            rho_grad = lambda_ent
            
            # Clip rho gradient to [-1.0, 1.0]
            rho_grad = float(np.clip(rho_grad, -1.0, 1.0))
            
            rho_momentum = momentum_coef * state['rho_momentum'] + rho_grad
            rho = rho - lr * rho_momentum
            
            # Clip rho parameter to [-5.0, 1.0]
            rho = float(np.clip(rho, -5.0, 1.0))
            
            state['rho'] = rho
            state['rho_momentum'] = rho_momentum
        
    elif ctx.condition == 'negative_control_2':
        # Fixed noise (rho fixed at initial value -3.0, no updates)
        with ctx.torch.no_grad():
            # Use fixed rho = -3.0
            fixed_rho = -3.0
            sigma = float(np.exp(fixed_rho) + 1e-8)
            
            # Apply multiplicative weight noise
            ctx.target += ctx.target * sigma * epsilon
            # No rho update
    
    return None
