def apply_operator(ctx) -> None:
    # Only act in loss_term phase (the only registered phase)
    if ctx.phase != 'loss_term':
        return
    
    # Control arm (baseline_1): do nothing - no loss term added
    if ctx.condition == 'baseline_1':
        return
    
    # Get reference weights from block 0's q_proj
    reference_weights = ctx.model.blocks[0].attn.q_proj.weight.detach()
    
    # For negative_control_1, use a fixed random matrix instead of block 0's weights
    if ctx.condition == 'negative_control_1':
        # Initialize fixed random matrix on first call
        if 'negative_control_reference' not in ctx.state:
            # Create fixed random matrix with same shape and norm as block 0's weights
            ref_norm = ctx.torch.norm(reference_weights)
            random_matrix = ctx.randn_like(reference_weights)
            random_norm = ctx.torch.norm(random_matrix)
            random_matrix = random_matrix * (ref_norm / random_norm)
            ctx.state['negative_control_reference'] = random_matrix
        reference_weights = ctx.state['negative_control_reference'].detach()
    
    # Compute Frobenius norm consistency loss
    diff = ctx.target - reference_weights
    squared_elements = diff * diff
    loss_raw = ctx.torch.sum(squared_elements)
    consistency_coefficient = 0.01
    loss_term = consistency_coefficient * loss_raw
    
    # Add loss term to training objective
    ctx.add_loss(loss_term)
