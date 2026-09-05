def loss_amount(given_amount, loss_amount):
    if given_amount < loss_amount:
        return None
    else:
        return loss_amount - given_amount if loss_amount != 0 else None