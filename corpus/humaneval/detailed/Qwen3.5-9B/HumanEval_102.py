from typing import Union

def choose_num(x, y) -> int:
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """

    # Helper function to validate a single number is a positive integer
    def _is_positive_integer(value) -> bool:
        """Check if value is an integer greater than zero."""
        if not isinstance(value, int):
            return False
        if value <= 0:
            return False
        return True

    # Helper function to ensure the range is valid (lower bound <= upper bound)
    def _validate_range(lower: int, upper: int) -> None:
        """Raise an error if the lower bound is greater than the upper bound."""
        if lower > upper:
            raise ValueError(f"Invalid range: lower bound {lower} cannot be greater than upper bound {upper}.")

    # Validate input types first
    if not _is_positive_integer(x):
        raise TypeError(f"Invalid input x={x}. Expected a positive integer.")

    if not _is_positive_integer(y):
        raise TypeError(f"Invalid input y={y}. Expected a positive integer.")

    # Store validated integers in named variables for clarity
    lower_bound = x
    upper_bound = y

    # Validate the order of the bounds
    _validate_range(lower_bound, upper_bound)

    # Determine the starting point for the search
    # We want the largest even number <= upper_bound
    candidate_start = upper_bound

    # Adjust candidate_start if it is odd
    if candidate_start % 2 != 0:
        candidate_start = candidate_start - 1

    # Check if the adjusted candidate is still within the valid range
    # This handles cases like range [13, 14] where candidate_start becomes 14 (valid)
    # or range [13, 13] where candidate_start becomes 12 (invalid for the range)
    if candidate_start < lower_bound:
        return -1

    # Since we started from the largest possible even number <= upper_bound
    # and verified it is >= lower_bound, it is by definition the biggest.
    return candidate_start