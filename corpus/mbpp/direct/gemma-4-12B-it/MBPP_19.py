def test_duplicate(arr: list[int]) -> bool:
    """
    Checks if the given list of integers contains any duplicate elements.

    Args:
        arr (list[int]): A list of integers.

    Returns:
        bool: True if there are duplicates, False otherwise.
    """
    seen = set()
    for num in arr:
        if num in seen:
            return True
        seen.add(num)
    return False

if __name__ == "__main__":
    assert test_duplicate([1,2,3,4,5]) == False
    assert test_duplicate([1,2,3,4, 4]) == True
    assert test_duplicate([1,1,2,2,3,3,4,4,5]) == True