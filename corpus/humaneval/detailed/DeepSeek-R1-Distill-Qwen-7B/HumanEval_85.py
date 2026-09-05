def add(lst):
    """
    Given a non-empty list of integers lst. Add the even elements that are at odd indices.

    Examples:
        add([4, 2, 6, 7]) ==> 2
    """
    # Validate input
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")
    if len(lst) == 0:
        return 0

    total = 0
    for index, element in enumerate(lst):
        if index % 2 == 1:  # Check if index is odd
            if element % 2 == 0:  # Check if element is even
                total += element
    return total