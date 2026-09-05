from typing import List, Union

def kth_element(nums: List[Union[int, float]], n: int, k: int) -> Union[int, float]:
    """
    Finds the kth smallest element in an array of n elements.

    Args:
        nums: A list of integers or floats.
        n: The number of elements in the list.
        k: The rank of the element to retrieve (1-indexed, where 1 is smallest).

    Returns:
        The kth smallest element in the list.

    Raises:
        ValueError: If inputs are inconsistent with the list size or range.
        TypeError: If inputs are of incorrect types.
    """
    # 1. Validate the input types
    if not isinstance(nums, list):
        raise TypeError(f"Expected a list for 'nums', but got {type(nums).__name__}")

    if not isinstance(n, int):
        raise TypeError(f"Expected an integer for 'n', but got {type(n).__name__}")

    if not isinstance(k, int):
        raise TypeError(f"Expected an integer for 'k', but got {type(k).__name__}")

    # 2. Validate lengths and bounds
    actual_length = len(nums)

    if actual_length != n:
        raise ValueError(
            f"The length of the list ({actual_length}) does not match the provided 'n' ({n})."
        )

    if n == 0:
        raise ValueError("The list and 'n' cannot be zero.")

    if k < 1 or k > n:
        raise ValueError(
            f"The rank 'k' ({k}) must be between 1 and {n} inclusive."
        )

    # 3. Defensive check for non-numeric elements in the list
    for item in nums:
        if not isinstance(item, (int, float)):
            raise TypeError(f"All elements in the list must be numeric. Found: {type(item).__name__}")

    # 4. Handle the logic
    # To find the kth smallest element, we need to identify the value at the 
    # (k-1)th index of a sorted version of the input array.

    # We create a copy of the list to avoid mutating the original input list
    # (Side-effect free programming).
    sorted_list = list(nums)

    # Sort the list in ascending order.
    # This is an O(N log N) operation.
    sorted_list.sort()

    # Since 'k' is 1-indexed (1 = smallest), the index in the list is k - 1.
    target_index = k - 1
    result = sorted_list[target_index]

    return result