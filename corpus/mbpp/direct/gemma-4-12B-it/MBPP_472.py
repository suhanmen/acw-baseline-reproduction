from typing import List

def check_Consecutive(nums: List[int]) -> bool:
    """
    Checks whether the given list contains consecutive numbers in the given order.

    Args:
        nums: A list of integers.

    Returns:
        True if numbers are consecutive, False otherwise.
    """
    if not nums:
        return True

    for i in range(len(nums) - 1):
        if nums[i+1] != nums[i] + 1:
            return False
    return True

if __name__ == "__main__":
    assert check_Consecutive([1, 2, 3, 4, 5]) == True
    assert check_Consecutive([1, 2, 3, 5, 6]) == False
    assert check_Consecutive([1, 2, 1]) == False