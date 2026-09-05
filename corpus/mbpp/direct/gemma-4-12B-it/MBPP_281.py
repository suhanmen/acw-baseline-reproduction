def all_unique(input_list: list) -> bool:
    """
    Checks if all elements in the given list are unique.

    Args:
        input_list (list): A list of elements to check.

    Returns:
        bool: True if all elements are unique, False otherwise.
    """
    return len(input_list) == len(set(input_list))

if __name__ == "__main__":
    assert all_unique([1,2,3]) == True
    assert all_unique([1,2,1,2]) == False
    assert all_unique([1,2,3,4,5]) == True