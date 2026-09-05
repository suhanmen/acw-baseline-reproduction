def check_type(t):
    """
    Check if all elements in the tuple have the same data type.
    """
    if not isinstance(t, tuple):
        raise ValueError("Input must be a tuple.")

    if len(t) == 0:
        raise ValueError("Empty tuples are not valid for this function.")

    if len(t) == 1:
        return True

    # Get the type of the first element
    first_type = type(t[0])

    # Check each element's type
    for element in t[1:]:
        if type(element) != first_type:
            return False

    return True

# Test cases
assert check_type((5, 6, 7, 3, 5, 6)) == True
assert check_type((1, 2, "4")) == False
assert check_type((3, 2, 1, 4, 5)) == True