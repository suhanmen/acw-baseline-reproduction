from typing import List

def sum_Pairs(arr: List[int], n: int) -> int:
    """
    Calculates the sum of absolute differences for all possible pairs (i, j) 
    where 0 <= i < j < n.

    The absolute difference for a pair (arr[i], arr[j]) is |arr[i] - arr[j]|.
    The goal is to compute: sum_{i=0}^{n-2} sum_{j=i+1}^{n-1} |arr[i] - arr[j]|

    Complexity Analysis:
    - Time Complexity: O(n log n) due to sorting.
    - Space Complexity: O(n) or O(1) depending on sort implementation.
    """
    # --- Input Validation ---
    if not isinstance(arr, list):
        raise ValueError("Input 'arr' must be a list of integers.")

    if not isinstance(n, int):
        raise ValueError("Input 'n' must be an integer.")

    if n <= 0:
        return 0

    # Ensure we do not process elements beyond the provided 'n' 
    # or if the list is smaller than 'n', we handle the bounds safely.
    # Usually, 'n' is expected to be len(arr), but we follow the signature.
    actual_n = min(len(arr), n)

    if actual_n < 2:
        # A single element or empty list has no pairs to compare.
        return 0

    # Create a copy of the relevant slice to avoid mutating the original input list.
    # We work with a sorted list to use a linear-time summation logic.
    working_data = sorted(arr[:actual_n])

    # --- Mathematical Logic ---
    # For a sorted array, the sum of absolute differences can be calculated 
    # efficiently by observing how many times each element is added or subtracted.
    # For a sorted array: |arr[i] - arr[j]| where j > i is simply (arr[j] - arr[i]).
    #
    # Total Sum = sum over all j of (j * arr[j] - (count_of_elements_before_j) * arr[j] 
    #             - sum_of_elements_before_j) is not the simplest way.
    #
    # The standard optimized formula for sorted array is:
    # Sum = sum_{i=0}^{n-1} ( (2*i + 1 - n) * arr[i] ) 
    # Wait, let's derive it carefully:
    # Each arr[i] is subtracted by all elements to its right (n - 1 - i elements)
    # and added by all elements to its left (i elements).
    # Contribution of arr[i] = arr[i] * (i - (n - 1 - i))
    # Contribution of arr[i] = arr[i] * (2*i - n + 1)

    total_sum = 0
    # Use the derived contribution formula for O(n) after sorting.
    for i in range(actual_n):
        current_element = working_data[i]

        # Number of elements to the left of index i
        elements_to_left = i

        # Number of elements to the right of index i
        elements_to_right = actual_n - 1 - i

        # The net contribution of this element to the total sum of differences:
        # It is added for every element smaller than it and subtracted for every element larger.
        multiplier = elements_to_left - elements_to_right

        contribution = current_element * multiplier
        total_sum += contribution

    return total_sum

# The following logic is an alternative O(n^2) approach for verification 
# if the O(n log n) logic were not used, but O(n log n) is standard for production.