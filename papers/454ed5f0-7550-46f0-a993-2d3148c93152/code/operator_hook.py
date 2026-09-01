def apply_operator(ctx) -> None:
    if ctx.phase == 'loss_term':
        if ctx.condition == 'proposed':
            # Spectral Entropy Minimization loss term (with gradients)
            W = ctx.target
            # Compute singular values
            sigma = ctx.torch.linalg.svdvals(W)
            # Sum with epsilon safeguard
            sum_sigma = sigma.sum() + 1e-8
            # Normalize to probabilities
            p = sigma / sum_sigma
            # Compute entropy H = -sum(p * log(p + eps))
            H = -(p * ctx.torch.log(p + 1e-8)).sum()
            # Scale and add to loss (part of autograd graph)
            loss_term = 0.01 * H
            ctx.add_loss(loss_term)
        
        elif ctx.condition == 'baseline_1':
            # Control arm: do nothing (no loss term, no parameter modification)
            pass
        
        elif ctx.condition == 'negative_control_1':
            # Compute spectral entropy on W detached from graph (no gradient flow)
            # Do NOT add to loss - just compute without building autograd graph
            W = ctx.target.detach()
            sigma = ctx.torch.linalg.svdvals(W)
            sum_sigma = sigma.sum() + 1e-8
            p = sigma / sum_sigma
            H = -(p * ctx.torch.log(p + 1e-8)).sum()
            # No ctx.add_loss call - computation happens but no term added to objective
        
        elif ctx.condition == 'negative_control_2':
            # Standard Weight Decay (No Spectral Entropy Term)
            # Weight decay is handled by optimizer, no spectral entropy added
            pass
