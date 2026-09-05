from typing import List, Tuple

def max_Product(nums: List[int]) -> Tuple[int, int]:
    """
    Finds a pair of integers in the array that yields the highest product.
    The function considers both large positive numbers and large negative numbers.
    """
    if len(nums) < 2:
        raise ValueError("Array must contain at least two integers.")

    # Sort the array to easily find the smallest (most negative) 
    # and largest (most positive) numbers.
    nums.sort()

    # Potential candidates for max product:
    # 1. The two largest positive numbers (at the end of the sorted list)
    # 2. The two smallest (most negative) numbers (at the beginning of the sorted list)

    prod_end = nums[-1] * nums[-2]
    prod_start = nums[0] * nums[1]

    if prod_end >= prod_start:
        return (nums[-2], nums[-1])
    else:
        return (nums[0], nums[1])

if __name__ == "__main__":
    assert max_Product([1, 2, 3, 4, 7, 0, 8, 4]) == (7, 8)
    assert max_Product([0, -1, -2, -4, 5, 0, -6]) == (-4, -6)
    assert max_Product([1, 2, 3]) == (2, 3)