from typing import Optional, Union

def loss_amount(current_amount: Union[int, float], initial_amount: Union[int, float]) -> Optional[Union[int, float]]:
    """
    Calculates the loss amount based on the provided assertions:
    - If current_amount >= initial_amount, return None.
    - If current_amount < initial_amount, return the difference (initial_amount - current_amount).
    """
    # Input Validation
    if not isinstance(current_amount, (int, float)) or not isinstance(initial_amount, (int, float)):
        raise TypeError("Inputs must be numeric.")

    # Check if there is a loss
    # A loss occurs only if the current amount is strictly less than the initial amount.
    if current_amount < initial_amount:
        # Calculate the loss amount
        loss = initial_amount - current_amount
        return loss
    else:
        # No loss occurred (either a gain or no change)
        return None