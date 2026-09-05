def check_element(lst, target):
    """
    Checks whether all items of a list are equal to a given target.

    Args:
        lst (list): A list of elements.
        target (any): The value to compare all list elements against.

    Returns:
        bool: True if all elements in lst are equal to target, False otherwise.
    """
    if not lst:
        return True
    return all(item == target for item in lst)

if __name__ == "__main__":
    assert check_element(["green", "orange", "black", "white"], 'blue') == False
    assert check_element([1, 2, 3, 4], 7) == False
    assert check_element(["green", "green", "green", "green"], 'green') == True