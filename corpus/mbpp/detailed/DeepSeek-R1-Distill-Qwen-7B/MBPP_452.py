def loss_amount(amount, reduced_amount):
    """
    Calculate the loss amount when the given amount is reduced.

    Args:
        amount (int): The original amount.
        reduced_amount (int): The amount after reduction.

    Returns:
        int: The loss amount if amount > reduced_amount, otherwise None.

    Raises:
        ValueError: If either amount or reduced_amount is not an integer.
    """
    if not isinstance(amount, int) or not isinstance(reduced_amount, int):
        raise ValueError("Both arguments must be integers.")

    if amount <= 0 or reduced_amount <= 0:
        raise ValueError("Both arguments must be positive numbers.")

    def calculate_loss(a, r):
        """Calculate the loss when the given amount is reduced."""
        return a - r if a > r else None

    def validate_inputs(*args):
        """Validate the input arguments."""
        if len(args) != 2:
            raise ValueError("Exactly two arguments are required.")
        if not all(isinstance(arg, int) for arg in args):
            raise ValueError("Both arguments must be integers.")
        if any(arg <= 0 for arg in args):
            raise ValueError("Both arguments must be positive numbers.")

    validate_inputs(amount, reduced_amount)

    return calculate_loss(amount, reduced_amount)