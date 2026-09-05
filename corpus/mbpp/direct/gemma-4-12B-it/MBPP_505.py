from typing import List

def re_order(nums: List[int]) -> List[int]:
    """
    Moves all zeroes to the end of the list while maintaining 
    the relative order of non-zero elements.
    """
    non_zeros = [x for x in nums if x != 0]
    zero_count = nums.count(0)
    return non_zeros + [0] * zero_count

if __name__ == "__main__":
    assert re_order([6, 0, 8, 2, 3, 0, 4, 0, 1]) == [6, 8, 2, 3, 4, 1, 0, 0, 0]
    assert re_order([4, 0, 2, 7, 0, 9, 0, 12, 0]) == [4, 2, 7, 9, 12, 0, 0, 0, 0]
    assert re_order([3, 11, 0, 74, 14, 0, 1, 0, 2]) == [3, 11, 74, 14, 1, 2, 0, 0, 0]