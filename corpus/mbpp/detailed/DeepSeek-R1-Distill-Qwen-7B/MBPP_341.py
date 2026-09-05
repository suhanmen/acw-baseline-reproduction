def set_to_tuple(s):
    # Check if the input is a valid set
    if not isinstance(s, set):
        raise TypeError("Input must be a set.")

    # Convert the set to a list to maintain order
    elements = list(s)

    # Convert the list to a tuple
    ordered_tuple = tuple(elements)

    # Handle special cases
    if len(ordered_tuple) == 0:
        return ()
    elif len(ordered_tuple) == 1:
        return ordered_tuple
    else:
        return ordered_tuple

# Test the function with the given examples
def test_set_to_tuple():
    assert set_to_tuple({1, 2, 3, 4, 5}) == (1, 2, 3, 4, 5)
    assert set_to_tuple({6, 7, 8, 9, 10, 11}) == (6, 7, 8, 9, 10, 11)
    assert set_to_tuple({12, 13, 14, 15, 16}) == (12, 13, 14, 15, 16)
    print("All tests passed.")

test_set_to_tuple()