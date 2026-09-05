from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    # Input Validation: Ensure numbers is a list and threshold is a number
    if not isinstance(numbers, list):
        raise TypeError("The 'numbers' argument must be a list of floats/integers.")

    if not isinstance(threshold, (int, float)):
        raise TypeError("The 'threshold' argument must be a float or an integer.")

    # Handle degenerate cases:
    # If the list has 0 or 1 elements, there are no "two" numbers to compare.
    if len(numbers) < 2:
        return False

    # Sort the numbers to allow for a single-pass O(n log n) comparison.
    # Sorting ensures that the closest neighbors are adjacent in the list.
    # We create a copy to avoid mutating the original input list (defensive programming).
    sorted_numbers = sorted(numbers)

    # Iterate through the sorted list and compare adjacent elements.
    # We stop at len - 1 because we check the current element against the next one.
    for i in range(len(sorted_numbers) - 1):
        current_value = sorted_numbers[i]
        next_value = sorted_numbers[i + 1]

        # Calculate the absolute difference between adjacent numbers.
        # Since the list is sorted, next_value >= current_value, 
        # but we use abs() for absolute robustness.
        difference = abs(current_value - next_value)

        # Check if the difference is strictly less than the threshold.
        if difference < threshold:
            # Return True immediately upon finding the first pair that satisfies the condition.
            return True

    # If the loop completes without returning True, no two elements are closer than threshold.
    return False