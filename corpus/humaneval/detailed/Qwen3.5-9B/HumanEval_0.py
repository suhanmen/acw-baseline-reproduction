from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """

    # Helper function to validate the input list
    def _validate_numbers(nums: List[float]) -> None:
        if not isinstance(nums, list):
            raise TypeError(f"Expected a list, but received {type(nums).__name__}")
        for idx, val in enumerate(nums):
            if not isinstance(val, (int, float)) or isinstance(val, bool):
                raise TypeError(f"Element at index {idx} is not a number: {type(val).__name__}")
        if len(nums) < 2:
            raise ValueError(f"List must contain at least two elements to compare distances, but received {len(nums)}")

    # Helper function to validate the threshold
    def _validate_threshold(th: float) -> None:
        if not isinstance(th, (int, float)) or isinstance(th, bool):
            raise TypeError(f"Threshold must be a number, but received {type(th).__name__}")

    # Helper function to sort the list while keeping track of original indices (though indices don't matter for distance)
    def _get_sorted_numbers(unsorted: List[float]) -> List[float]:
        return sorted(unsorted)

    # Helper function to calculate absolute difference between two numbers
    def _calculate_distance(a: float, b: float) -> float:
        return abs(a - b)

    # Helper function to check if any pair in a sorted list is within threshold
    def _find_close_pair(sorted_nums: List[float], threshold: float) -> bool:
        # In a sorted list, the minimum distance between any two elements must be between adjacent elements
        for i in range(len(sorted_nums) - 1):
            current_num = sorted_nums[i]
            next_num = sorted_nums[i + 1]
            distance = _calculate_distance(current_num, next_num)
            if distance < threshold:
                return True
        return False

    # --- Main Logic ---

    # Step 1: Validate inputs
    _validate_numbers(numbers)
    _validate_threshold(threshold)

    # Step 2: Handle the edge case where list has less than 2 elements (should be caught by validation, but explicit check for clarity)
    # The validation function above raises ValueError, so we proceed to sort.

    # Step 3: Sort the numbers to efficiently find the closest pair
    sorted_numbers = _get_sorted_numbers(numbers)

    # Step 4: Iterate through the sorted list to find if any adjacent pair is within the threshold
    # We rely on the mathematical property that in a sorted list, the minimum distance between any two numbers
    # must exist between some adjacent pair. If no adjacent pair is within the threshold, no pair is.
    if _find_close_pair(sorted_numbers, threshold):
        return True
    else:
        return False