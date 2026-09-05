from typing import List

def find_first_duplicate(nums: List[int]) -> int:
    """
    Finds the first duplicate element in a given list of integers.
    Returns the value of the first element that appears a second time.
    If no duplicates are found, returns -1.
    """
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
    return -1

if __name__ == "__main__":
    assert find_first_duplicate([1, 2, 3, 4, 4, 5]) == 4
    assert find_first_duplicate([1, 2, 3, 4]) == -1
    assert find_first_duplicate([1, 1, 2, 3, 3, 2, 2]) == 1