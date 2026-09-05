def chkList(lst):
    """
    Checks whether all elements in a list are the same.

    Args:
        lst (list): A list of elements.

    Returns:
        bool: True if all elements are the same, False otherwise.
    """
    if not lst:
        return True

    first_element = lst[0]
    for item in lst:
        if item != first_element:
            return False
    return True

if __name__ == "__main__":
    assert chkList(['one','one','one']) == True
    assert chkList(['one','Two','Three']) == False
    assert chkList(['bigdata','python','Django']) == False