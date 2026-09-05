def loss_amount(initial_amount, final_amount):
    """
    Returns the loss amount if the final_amount is less than the initial_amount,
    otherwise returns None.
    """
    if final_amount < initial_amount:
        return initial_amount - final_amount
    else:
        return None