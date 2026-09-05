def check_tuplex(tup, element):
    """
    Checks whether an element exists within a tuple.

    Args:
        tup (tuple): The tuple to search within.
        element: The element to look for.

    Returns:
        bool: True if the element exists in the tuple, False otherwise.
    """
    return element in tup

if __name__ == "__main__":
    assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), 'r') == True
    assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), '5') == False
    assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), 3) == True