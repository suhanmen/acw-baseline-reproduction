def tup_string(tup):
    """
    Convert a tuple to a string.

    Parameters:
        tup (tuple): The input tuple to convert.

    Returns:
        str: The concatenated string of the tuple elements.

    Raises:
        TypeError: If the input is not a tuple.
        ValueError: If any element in the tuple is not a string.
    """
    # Check if the input is a tuple
    if not isinstance(tup, tuple):
        raise TypeError("Input must be a tuple.")

    # Check if all elements are strings
    if not all(isinstance(item, str) for item in tup):
        raise ValueError("All elements in the tuple must be strings.")

    # Handle empty tuple
    if not tup:
        return ""

    # Join all elements of the tuple into a single string
    try:
        result = ''.join(tup)
    except TypeError:
        raise ValueError("All elements in the tuple must be strings.")

    return result

# Example usage and assertions
def test_tup_string():
    assert tup_string(('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')) == "exercises"
    assert tup_string(('p', 'y', 't', 'h', 'o', 'n')) == "python"
    assert tup_string(('p', 'r', 'o', 'g', 'r', 'a', 'm')) == "program"

test_tup_string()