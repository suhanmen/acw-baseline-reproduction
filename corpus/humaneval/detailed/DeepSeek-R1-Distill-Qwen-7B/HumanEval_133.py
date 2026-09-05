import math

def sum_squares(lst):
    """You are given a list of numbers.
    You need to return the sum of squared numbers in the given list,
    round each element in the list to the upper int(Ceiling) first.

    Args:
        lst (list): A list of numbers.

    Returns:
        int: The sum of squares after rounding each element up.

    Raises:
        TypeError: If the input is not a list or contains non-numeric elements.
    """
    # Check if the input is a list
    if not isinstance(lst, list):
        raise TypeError("Input must be a list.")

    # Check if all elements are numeric
    for num in lst:
        if not isinstance(num, (int, float)):
            raise TypeError("All elements in the list must be numeric.")

    # Process each element: round up to the nearest integer
    rounded = [math.ceil(num) for num in lst]

    # Square each rounded number and sum them
    squared_sum = sum(num ** 2 for num in rounded)

    return squared_sum