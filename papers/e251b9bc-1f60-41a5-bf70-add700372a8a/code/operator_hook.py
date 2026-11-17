def apply_operator(ctx) -> None:
    # Only act at post_step phase
    if ctx.phase != 'post_step':
        return

    condition = ctx.condition
    target = ctx.target
    momentum_buffer = ctx.momentum_buffer
    torch = ctx.torch

    # Handle baseline condition: return immediately without any mutation
    if condition == 'baseline_1':
        return

    # Handle negative_control_1 and proposed: both require momentum_buffer
    if momentum_buffer is None:
        return

    with torch.no_grad():
        # Compute row-wise squared norms of M
        norm_M_sq = torch.sum(momentum_buffer * momentum_buffer, dim=1)
        valid_rows = (norm_M_sq > 1e-12)
        
        # If no valid rows, skip for all non-baseline conditions
        if not torch.any(valid_rows):
            return
        
        # Compute row-wise dot products: dot = sum(W * M, dim=1)
        dot = torch.sum(target * momentum_buffer, dim=1)
        
        # Compute projection scalars: alpha = dot / (norm_M_sq + 1e-12)
        alpha = dot / (norm_M_sq + 1e-12)
        
        # Broadcast alpha to match W shape
        alpha_expanded = alpha.unsqueeze(1)
        
        # Compute projection update: delta = alpha_expanded * M
        delta = alpha_expanded * momentum_buffer

    # Apply condition-specific updates
    if condition == 'negative_control_1':
        with torch.no_grad():
            # Generate random signs using the operator's own RNG stream
            # Use rand_like on the valid rows subset to ensure device/dtype match
            signs = 1.0 - 2.0 * (ctx.rand_like(target[valid_rows, 0]) < 0.5).to(target.dtype)
            
            # Apply sign-randomized projection only to valid rows
            target[valid_rows, :] = target[valid_rows, :] - signs.unsqueeze(1) * delta[valid_rows, :]

    elif condition == 'proposed':
        with torch.no_grad():
            # Apply orthogonal projection only to valid rows
            target[valid_rows, :] = target[valid_rows, :] - delta[valid_rows, :]
