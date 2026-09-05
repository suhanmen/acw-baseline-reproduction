from typing import List

def _validate_input(arr: list, k_times: int) -> None:
    """
    Validates the input arguments to ensure they meet the requirements.

    Args:
        arr (list): The input array of numbers.
        k_times (int): The number of times to repeat the array.

    Raises:
        TypeError: If arr is not a list or k_times is not an integer.
        ValueError: If arr is empty or k_times is less than or equal to zero.
    """
    # Check if arr is a list
    if not isinstance(arr, list):
        raise TypeError("The input array must be a list.")

    # Check if array is empty
    if len(arr) == 0:
        raise ValueError("The input array cannot be empty.")

    # Check if all elements in the array are numbers
    for i, element in enumerate(arr):
        if not isinstance(element, (int, float)):
            raise TypeError(f"All elements in the array must be numbers. Found element at index {i}: {element!r} which is of type {type(element).__name__}.")

    # Check if k_times is an integer
    if not isinstance(k_times, int) or isinstance(k_times, bool):
        raise TypeError("The repetition count must be an integer.")

    # Check if k_times is positive
    if k_times <= 0:
        raise ValueError("The repetition count must be greater than zero.")


def _kadane_algorithm(arr: List[float]) -> float:
    """
    Computes the maximum subarray sum using Kadane's Algorithm for a single array.

    Args:
        arr (List[float]): The input array of numbers.

    Returns:
        float: The maximum sum of a contiguous subarray within the array.
    """
    # Initialize current_sum and max_sum with the first element
    current_sum = arr[0]
    max_sum = arr[0]

    # Iterate through the array starting from the second element
    for i in range(1, len(arr)):
        element = arr[i]

        # Decide whether to start a new subarray at the current element
        # or to continue the existing subarray
        if current_sum > 0:
            # If current_sum is positive, add it to the current element
            new_current_sum = current_sum + element
        else:
            # If current_sum is negative or zero, start a new subarray
            new_current_sum = element

        # Update current_sum
        current_sum = new_current_sum

        # Update max_sum if current_sum is greater
        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum


def _compute_max_sum_repeated(arr: List[float], k_times: int) -> float:
    """
    Computes the maximum subarray sum for the array repeated k times.

    This handles the logic where the maximum subarray might span across the
    boundaries of the repeated arrays.

    Args:
        arr (List[float]): The original array.
        k_times (int): Number of times to repeat the array.

    Returns:
        float: The maximum subarray sum.
    """
    n = len(arr)
    total_sum = sum(arr)

    # Case 1: k_times == 1
    if k_times == 1:
        return _kadane_algorithm(arr)

    # Case 2: k_times == 2
    if k_times == 2:
        # Construct the doubled array explicitly
        doubled_arr = arr + arr
        return _kadane_algorithm(doubled_arr)

    # Case 3: k_times >= 3
    if k_times >= 3:
        # The maximum subarray in a repeated array (k >= 3) is either:
        # 1. Entirely within one instance of the array (handled by single kadane)
        # 2. Spans across the boundary of two adjacent arrays (handled by 2x kadane)
        # 3. Spans across all k arrays. This is possible if the total sum of the array is positive.
        #    In this case, the max sum is (sum of all elements) + (max suffix of first copy) + (max prefix of last copy).
        #    However, a simpler way to think about it for k >= 3:
        #    If total_sum > 0, we can take the middle (k-2) copies fully, plus the max suffix of the first,
        #    and max prefix of the last.
        #    Actually, the standard solution for k >= 3 is:
        #    max(kadane on 2*arr, total_sum + max_suffix_of_arr + max_prefix_of_arr)
        #    BUT, if total_sum <= 0, we can't include full middle copies beneficially.
        #    So we just take the max of (kadane on 2*arr, kadane on arr).
        #    Wait, if total_sum > 0, the formula is:
        #    (k-2) * total_sum + max_suffix + max_prefix.
        #    However, if k=3, (3-2)*total + suffix + prefix = total + suffix + prefix.
        #    Does this cover everything? Yes, for k>=3.
        #    If total_sum <= 0, the term (k-2)*total_sum is negative or zero.
        #    We should just rely on the max of kadane(2*arr) and kadane(arr).
        #    Actually, if total_sum <= 0, the optimal strategy never involves taking more than 2 copies
        #    fully because adding more copies just adds negative value.
        #    So for k >= 3:
        #    If total_sum > 0: result = (k-2) * total_sum + max_suffix + max_prefix
        #    Else: result = max(kadane(2*arr), kadane(arr)) -> effectively just max(kadane(2*arr)) usually,
        #            but technically if the array is all negative, kadane(arr) might be "less negative" than kadane(2*arr)
        #            if the single element max is in the middle? No, kadane on 2*arr covers any span.
        #            If all negative, kadane returns max single element. kadane on 2*arr also returns max single element.
        #            So just max(kadane(2*arr), kadane(arr)) is safe, but kadane(2*arr) dominates unless n=1.
        #            If n=1, kadane(2*arr) = 2*val, kadane(arr)=val.
        #            So we just need to handle the total_sum > 0 case specially.

        # Calculate max suffix sum (maximum sum ending at the last element)
        max_suffix_sum = _compute_max_suffix(arr)

        # Calculate max prefix sum (maximum sum starting at the first element)
        max_prefix_sum = _compute_max_prefix(arr)

        # Calculate max subarray sum for 2 repetitions
        doubled_arr_max = _kadane_algorithm(arr + arr)

        # Calculate max subarray sum for 1 repetition
        single_arr_max = _kadane_algorithm(arr)

        # Determine base max from 2 repetitions
        base_max = doubled_arr_max

        # If total sum is positive, we can extend the solution to k repetitions
        if total_sum > 0:
            # Formula: (k-2) * total_sum + max_suffix + max_prefix
            # This represents taking the full (k-2) middle arrays and the best prefix/suffix from the ends
            extended_max = (k_times - 2) * total_sum + max_suffix_sum + max_prefix_sum
            return max(base_max, extended_max)
        else:
            # If total sum is not positive, we can't benefit from more than 2 arrays
            # (or even 1 if 2 covers less, but 2 usually covers more or equal).
            # However, we must ensure we don't miss the case where the single array has a higher max
            # than the doubled one (e.g., specific negative patterns, though unlikely for contiguous).
            # Actually, kadane on 2*arr always >= kadane on arr because the single array is a subset of 2*arr.
            # So base_max is sufficient.
            return base_max


def _compute_max_suffix(arr: List[float]) -> float:
    """
    Computes the maximum suffix sum of the array (maximum sum of a subarray ending at the last element).

    Args:
        arr (List[float]): The input array.

    Returns:
        float: The maximum suffix sum.
    """
    current_suffix_sum = 0
    max_suffix_sum = float('-inf')

    # Iterate backwards from the last element to the first
    for i in range(len(arr) - 1, -1, -1):
        element = arr[i]

        # Add current element to the suffix sum
        current_suffix_sum += element

        # Update max_suffix_sum
        if current_suffix_sum > max_suffix_sum:
            max_suffix_sum = current_suffix_sum

    return max_suffix_sum


def _compute_max_prefix(arr: List[float]) -> float:
    """
    Computes the maximum prefix sum of the array (maximum sum of a subarray starting at the first element).

    Args:
        arr (List[float]): The input array.

    Returns:
        float: The maximum prefix sum.
    """
    current_prefix_sum = 0
    max_prefix_sum = float('-inf')

    # Iterate forwards from the first element to the last
    for i in range(len(arr)):
        element = arr[i]

        # Add current element to the prefix sum
        current_prefix_sum += element

        # Update max_prefix_sum
        if current_prefix_sum > max_prefix_sum:
            max_prefix_sum = current_prefix_sum

    return max_prefix_sum


def max_sub_array_sum_repeated(arr: list, k: int, _dummy: int = None) -> float:
    """
    Finds the largest sum of a contiguous subarray in the array formed by repeating the given array k times.

    Note: The function signature includes a _dummy parameter to match a potential specific calling convention
    if k is expected to be passed as a positional argument and there's a mismatch, but based on the problem
    "repeating the given array k times" and the assertions `max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3)`,
    the arguments are: (array, k_times, something_else?).

    Let's re-read the assertions carefully:
    assert max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) == 30

    Input: [10, 20, -30, -1]
    Arg 2: 4
    Arg 3: 3

    Usually, this function is `max_sub_array_sum_repeated(arr, k)`.
    If the signature in the problem description implies 3 arguments, what are they?
    Perhaps the third argument is not used? Or maybe the problem description has a typo in the example calls?
    OR, maybe the function is meant to be `max_sub_array_sum_repeated(arr, k_times, something)`.

    Let's look at the example logic manually.
    Array: [10, 20, -30, -1]
    Sum = 19.
    If k=3 (the 3rd argument in the call is 3?), then repeated array is 3 times.
    Repeated: [10, 20, -30, -1, 10, 20, -30, -1, 10, 20, -30, -1]
    Max subarray?
    Positives: 10+20 = 30. Then -30, -1. Then 10+20 = 30.
    If we take 10, 20 from first copy: sum 30.
    If we take 10, 20 from second copy: sum 30.
    Can we bridge? 10, 20, -30, -1, 10, 20. Sum = 19 + 30 = 49? No.
    10, 20, -30, -1 (sum 19) + 10, 20 (sum 30) = 49? No, contiguous.
    20, -30, -1, 10, 20 -> -30 + -1 + 10 + 20 = -1.
    Sequence: 10, 20, (sum 30). Next -30 (drops to 0). Next -1 (-1). Next 10 (9). Next 20 (29).
    So max is 30.

    What if k is the 2nd argument (4) and 3rd is something else?
    If k=4, and 3rd arg is ignored or used differently?
    But the assertion says `max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) == 30`.
    If k=4, total sum = 19 * 4 = 76.
    Max suffix = 20-30-1 = -11? No.
    Suffixes:
    [-1