def apply_operator(ctx) -> None:
    # Only act during loss_term phase as registered
    if ctx.phase != 'loss_term':
        return

    torch = ctx.torch
    target = ctx.target
    coefficient = 0.01
    eps = 1e-8

    if ctx.condition == 'proposed':
        # Proposed: variance penalty on row norms (dim=1, output neurons)
        norms = torch.sqrt(torch.sum(target**2, dim=1) + eps)
        mu = norms.mean()
        centered = norms - mu
        var_penalty = (centered ** 2).mean()
        var_penalty = torch.clamp(var_penalty, min=0.0)
        scaled_penalty = var_penalty * coefficient
        ctx.add_loss(scaled_penalty)
    
    elif ctx.condition == 'negative_control_1':
        # Negative control: variance penalty on column norms (dim=0)
        # This destroys the mechanism by operating on the wrong axis
        norms = torch.sqrt(torch.sum(target**2, dim=0) + eps)
        mu = norms.mean()
        centered = norms - mu
        var_penalty = (centered ** 2).mean()
        var_penalty = torch.clamp(var_penalty, min=0.0)
        scaled_penalty = var_penalty * coefficient
        ctx.add_loss(scaled_penalty)
    
    elif ctx.condition == 'baseline_1':
        # Baseline: no intervention, leave everything unchanged
        return
