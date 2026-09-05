from typing import List

def position_max(nums: List[int]) -> List[int]:
    """
    Identifies all index positions where the maximum value occurs in a list.

    Args:
        nums (List[int]): A list of integers.

    Returns:
        List[int]: A list of indices where the maximum value is located.

    Raises:
        ValueError: If the input list is empty.
        TypeError: If the input is not a list or contains non-integer elements.
    """
    # --- Input Validation ---

    # Check if input is actually a list
    if not isinstance(nums, list):
        raise TypeError(f"Expected input type 'list', but received '{type(nums).__name__}'")

    # Handle the empty list case explicitly
    if len(nums) == 0:
        raise ValueError("Input list cannot be empty.")

    # Validate that all elements are integers to ensure robust behavior
    for item in nums:
        if not isinstance(item, int):
            raise TypeError(f"All elements in the list must be integers. Found: {type(item).__name__}")

    # --- Logic Implementation ---

    # Step 1: Find the maximum value in the list.
    # Python's built-in max() is efficient and handles negatives/positives correctly.
    max_value: int = max(nums)

    # Step 2: Iterate through the list to collect indices of occurrences.
    # Using a list comprehension or a manual loop ensures clarity.
    # Here we use a manual loop to satisfy the "explicit control flow" requirement.
    indices_of_max: List[int] = []

    for current_index in range(len(nums)):
        current_element = nums[current_index]

        # Check if the current element matches the identified maximum
        if current_element == max_value:
            indices_of_max.append(current_index)

    return indices_of_max

# The assertions provided in the problem description are satisfied:
# assert position_max([12,33,23,10,67,89,45,667,23,12,11,10,54]) == [7]
# assert position_max([1,2,2,2,4,4,4,5,5,5,5]) == [7,8,9,10]
# assert position_max([2,1,5,6,8,3,4,9,10,11,8,12]) == [11]