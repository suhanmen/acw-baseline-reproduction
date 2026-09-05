def is_sublist(main_list, sublist):
    """
    Checks whether a list contains the given sublist as a contiguous sequence.

    Args:
        main_list (list): The list to search within.
        sublist (list): The sequence to look for.

    Returns:
        bool: True if sublist is a contiguous sequence within main_list, False otherwise.
    """
    if not sublist:
        return True

    n = len(main_list)
    m = len(sublist)

    for i in range(n - m + 1):
        if main_list[i : i + m] == sublist:
            return True

    return False

if __name__ == "__main__":
    assert is_sublist([2,4,3,5,7],[3,7])==False
    assert is_sublist([2,4,3,5,7],[4,3])==True
    assert is_sublist([2,4,3,5,7],[1,6])==False