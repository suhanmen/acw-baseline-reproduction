from typing import List

def counting_sort(nums: List[int]) -> List[int]:
    """
    Sorts an array of non-negative integers using the Counting Sort algorithm.

    Counting sort is a non-comparative sorting algorithm that works by 
    counting the number of occurrences of each unique element in the input.
    Time Complexity: O(n + k) where n is the number of elements and k is the range.
    Space Complexity: O(k) to store the count array.

    Args:
        nums: A list of integers.

    Returns:
        A new list containing the elements of the input sorted in ascending order.

    Raises:
        ValueError: If the list contains negative integers, as standard counting 
                    sort requires non-negative indices.
        TypeError: If the input is not a list or contains non-integer elements.
    """
    # --- Input Validation ---

    # Check if the input is actually a list
    if not isinstance(nums, list):
        raise TypeError(f"Input must be a list, got {type(nums).__name__}")

    # Handle the empty list edge case immediately
    if len(nums) == 0:
        return []

    # Validate that all elements are integers and are non-negative
    for item in nums:
        if not isinstance(item, int):
            raise TypeError(f"All elements in the list must be integers. Found: {type(item).__name__}")
        if item < 0:
            # Counting sort usually requires non-negative values to map to array indices.
            # If negative values are required, an offset (min_val) would be needed.
            raise ValueError("Counting sort is implemented here for non-negative integers only.")

    # --- Algorithm Implementation ---

    # Find the maximum value in the list to determine the size of the counting array.
    # This is necessary because we need to know how many "buckets" to create.
    max_value = nums[0]
    for num in nums:
        if num > max_value:
            max_value = num

    # The range of values is from 0 to max_value.
    # Therefore, we need a count array of size (max_value + 1).
    # Example: if max_value is 5, we need indices 0, 1, 2, 3, 4, 5.
    count_range = max_value + 1

    # Initialize the count array with zeros.
    # Each index 'i' will store the frequency of the value 'i' in the input list.
    counts = [0] * count_range

    # Step 1: Populate the count array.
    # Iterate through the input list and increment the count at the corresponding index.
    for value in nums:
        counts[value] += 1

    # Step 2: Reconstruct the sorted list.
    # We iterate through the counts array and append the value to the result
    # as many times as it appeared in the input.
    sorted_list = []
    for actual_value in range(count_range):
        occurrence_count = counts[actual_value]

        # Add the value to the result list 'occurrence_count' times.
        for _ in range(occurrence_count):
            sorted_list.append(actual_value)

    return sorted_list