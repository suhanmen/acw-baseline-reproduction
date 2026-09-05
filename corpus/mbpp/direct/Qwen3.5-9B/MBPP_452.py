def loss_amount(current, total):
    if current < total:
        return total - current
    return None