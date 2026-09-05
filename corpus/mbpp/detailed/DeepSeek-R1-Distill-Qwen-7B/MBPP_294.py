import numbers

def max_val(lst):
    """
    Finds the maximum value in a given heterogeneous list.

    Args:
        lst: The list to find the maximum value in.

    Returns:
        The maximum value in the list, considering only numeric elements.

    Raises:
        TypeError: If the input is not a list.
        ValueError: If the list is empty after filtering non-numeric elements.
    """
    if not isinstance(lst, list):
        raise TypeError("Input must be a list.")

    # Filter out non-numeric elements
    numeric_elements = [x for x in lst if isinstance(x, numbers.Number)]

    if not numeric_elements:
        raise ValueError("The list must contain at least one numeric element.")

    return max(numeric_elements)