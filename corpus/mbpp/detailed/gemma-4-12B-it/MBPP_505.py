from typing import List


def re_order(nums: List[int]) -> List[int]:
    """
    Moves all zeroes in a list of integers to the end of the list,
    preserving the relative order of the non-zero elements.

    Args:
        nums (List[int]): A list of integers containing zero and non-zero values.

    Returns:
        List[int]: A new list with zeroes moved to the end.

    Raises:
        TypeError: If the input is not a list.
        ValueError: If the list contains non-integer elements.
    """
    # Input Validation
    if not isinstance(nums, list):
        raise TypeError(f"Expected input type 'list', but got '{type(nums).__name__}'.")

    # Check for non-integer elements in the list
    for item in nums:
        if not isinstance(item, int):
            raise ValueError(f"All elements in the list must be integers. Found: {type(item).__name__}")

    # Handle edge cases: Empty list or single element list
    if len(nums) == 0:
        return []

    if len(nums) == 1:
        # If it's a single element, return it as is (it's either 0 or non-zero)
        return list(nums)

    # Step 1: Identify and collect all non-zero elements
    # This preserves the relative order of the non-zero elements.
    non_zero_elements: List[int] = []
    for value in nums:
        if value != 0:
            non_zero_elements.append(value)

    # Step 2: Count the number of zeroes in the original list
    # This ensures we know exactly how many zeroes to append at the end.
    zero_count: int = 0
    for value in nums:
        if value == 0:
            zero_count += 1

    # Step 3: Construct the resulting list
    # We start with all non-zero elements found in the previous step.
    result: List[int] = list(non_zero_elements)

    # Step 4: Append the required number of zeroes to the end.
    for _ in range(zero_count):
        result.append(0)

    return result


if __name__ == "__main__":
    # Test cases provided in the prompt
    assert re_order([6, 0, 8, 2, 3, 0, 4, 0, 1]) == [6, 8, 2, 3, 4, 1, 0, 0, 0]
    assert re_order([4, 0, 2, 7, 0, 9, 0, 12, 0]) == [4, 2, 7, 9, 12, 0, 0, 0, 0]
    assert re_order([3, 11, 0, 74, 14, 0, 1, 0, 2]) == [3, 11, 74, 14, 1, 2, 0, 0, 0]

    # Additional edge cases
    assert re_order([]) == []
    assert re_order([0]) == [0]
    assert re_order([1, 2, 3]) == [1, 2, 3]
    assert re_order([0, 0, 0]) == [0, 0, 0]
    assert re_order([-1, 0, 5, 0, -2]) == [-1, 5, -2, 0, 0]