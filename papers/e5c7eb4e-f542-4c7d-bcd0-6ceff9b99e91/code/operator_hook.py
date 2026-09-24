def apply_operator(ctx) -> None:
    if ctx.phase == 'loss_term':
        if ctx.condition == 'baseline_1':
            return
        
        reference_weights = ctx.model.blocks[0].attn.q_proj.weight.detach()
        consistency_coefficient = 0.01
        
        if ctx.condition == 'proposed':
            diff = ctx.target - reference_weights
            loss_raw = (diff * diff).sum()
            loss_term = consistency_coefficient * loss_raw
            ctx.add_loss(loss_term)
        
        elif ctx.condition == 'negative_control_1':
            if 'negative_control_reference' not in ctx.state:
                random_matrix = ctx.randn_like(reference_weights)
                random_norm = random_matrix.norm()
                reference_norm = reference_weights.norm()
                if random_norm > 0:
                    random_matrix = random_matrix * (reference_norm / random_norm)
                ctx.state['negative_control_reference'] = random_matrix.detach()
            
            fixed_reference = ctx.state['negative_control_reference']
            diff = ctx.target - fixed_reference
            loss_raw = (diff * diff).sum()
            loss_term = consistency_coefficient * loss_raw
            ctx.add_loss(loss_term)
