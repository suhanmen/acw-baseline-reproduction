from typing import List, Tuple, Union

Number = Union[int, float]

def max_sum_bi_tonic_subsequence(arr: List[Number]) -> Number:
    """
    Calculates the maximum sum of a bi-tonic subsequence for the given array.

    A bi-tonic subsequence is defined as a subsequence that:
    1. First increases (strictly)
    2. Then decreases (strictly)
    The peak element is part of both the increasing and decreasing parts.

    Note: A monotonically increasing subsequence is considered bi-tonic (decreasing part is just one element).
    A monotonically decreasing subsequence is NOT considered bi-tonic per standard definitions requiring an increase phase.
    However, based on the provided test cases, we must handle cases where the optimal solution might be just an increase.

    Args:
        arr: A list of numbers.

    Returns:
        The maximum sum of a bi-tonic subsequence.

    Raises:
        ValueError: If the input list is empty.
    """

    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list.")

    if len(arr) == 0:
        raise ValueError("Input list cannot be empty.")

    # Validate element types
    for i, element in enumerate(arr):
        if not isinstance(element, (int, float)):
            raise TypeError(f"Element at index {i} is not a number.")

    n: int = len(arr)

    # Handle single element case
    if n == 1:
        return float(arr[0])

    # dp_incre[i] will store the maximum sum of an increasing subsequence ending at index i
    dp_incre: List[Number] = [0.0] * n
    # dp_decr[i] will store the maximum sum of a decreasing subsequence starting at index i
    dp_decr: List[Number] = [0.0] * n

    # Base case for increasing subsequences: each element itself
    for i in range(n):
        dp_incre[i] = float(arr[i])

    # Base case for decreasing subsequences: each element itself
    for i in range(n):
        dp_decr[i] = float(arr[i])

    # Fill dp_incre array
    for i in range(1, n):
        current_val: Number = float(arr[i])
        for j in range(i):
            if arr[j] < current_val:
                if dp_incre[j] + current_val > dp_incre[i]:
                    dp_incre[i] = dp_incre[j] + current_val

    # Fill dp_decr array (iterate backwards)
    for i in range(n - 2, -1, -1):
        current_val: Number = float(arr[i])
        for j in range(i + 1, n):
            if arr[j] < current_val:
                if dp_decr[j] + current_val > dp_decr[i]:
                    dp_decr[i] = dp_decr[j] + current_val

    # Calculate maximum bi-tonic sum
    # A bi-tonic subsequence is formed by an increasing part ending at i and a decreasing part starting at i.
    # The sum is dp_incre[i] + dp_decr[i] - arr[i] (since arr[i] is counted in both)

    max_total_sum: Number = float('-inf')

    for i in range(n):
        # Only consider valid increasing subsequences (length at least 1, which is always true here as base case)
        # For a valid bi-tonic, we typically need at least one increase and one decrease, 
        # BUT the problem constraints and examples suggest that a purely increasing sequence 
        # is acceptable if no better bi-tonic exists (or it's treated as increasing then plateau/decrease of length 1).
        # Let's follow the standard interpretation: max(increasing_sum[i], decreasing_sum[i]) is not quite right.
        # The peak is included in both.
        # Sum = (sum of increasing up to i) + (sum of decreasing from i) - (value at i)

        # Check if there was any increase before i (strictly greater sum than just arr[i])
        has_increased: bool = (dp_incre[i] > float(arr[i]))

        # Check if there was any decrease after i (strictly greater sum than just arr[i])
        has_decreased: bool = (dp_decr[i] > float(arr[i]))

        current_total: Number = dp_incre[i] + dp_decr[i] - float(arr[i])

        # Decision logic based on problem type:
        # If the problem strictly requires BOTH an increasing part and a decreasing part:
        # We would only take current_total if has_increased AND has_decreased.
        # However, looking at the first test case: [1, 15, 51, 45, 33, 100, 12, 18, 9]
        # If we MUST have both up and down, the path 1->15->51->45->33 is increasing, then 51->45...
        # Wait, the sequence 1, 15, 51, 45, 33, 100... 
        # Let's trace the first example manually to determine strictness.
        # Array: [1, 15, 51, 45, 33, 100, 12, 18, 9]
        # Indices: 0, 1, 2, 3, 4, 5, 6, 7, 8

        # Possible Bi-tonic (Up then Down):
        # Option 1: 1, 15, 51 (Peak 51), then 45, 33? Sum: 1+15+51+45+33 = 145.
        # Option 2: ... 51, 100? No, 51 < 100, so 100 would be the new peak.
        # Let's try peak at 100 (index 5).
        # Increasing to 100: 1, 15, 51, 100 (Sum = 167) OR 1, 15, 51, 33, 100 (No, 33<100 but 33<51, not increasing).
        # Increasing to 100: 1, 15, 51, 100. Sum = 167.
        # Decreasing from 100: 12, 9? (100 -> 12 -> 9). Sum = 100+12+9 = 121.
        # Total for peak 100: 167 + 121 - 100 = 188.

        # What about peak at 51 (index 2)?
        # Inc: 1, 15, 51 (Sum 67).
        # Dec: 51 -> 45 -> 33 (Sum 51+45+33=129).
        # Total: 67 + 129 - 51 = 145.

        # What about peak at 18 (index 7)?
        # Inc: 1, 15, 18? Or 1, 15, 51 (No), 1, 15, 45 (No)...
        # Inc ending at 18: 1, 15, 18 (Sum 34). (15 < 18).
        # Dec from 18: 18 -> 9 (Sum 27).
        # Total: 34 + 27 - 18 = 43.

        # Is there a sum of 194?
        # 1 + 15 + 51 + 45 + 33 + 100 = 245? No, must go up then down.
        # Maybe the definition allows purely increasing?
        # If purely increasing [1, 15, 51, 100] -> Sum 167.
        # If [1, 15, 51, 45, 33] -> Sum 145.
        # How to get 194?
        # 15 + 51 + 45 + 33 + 100 + 12 + 18 + 9? No.
        # Let's re-read the array: [1, 15, 51, 45, 33, 100, 12, 18, 9]
        # Sum of all: 1+15+51+45+33+100+12+18+9 = 284.
        # Maybe 1, 15, 51, 100, 12, 9? 188.
        # Maybe the sequence 1, 15, 51, 45, 33, 12, 18? No, 33>12<18 (down then up).

        # Re-evaluating the target 194.
        # Could it be 15 + 51 + 45 + 33 + 100 + 12 + 18 + 9? No.
        # Maybe 1, 15, 51, 100, 12, 18? (Up to 100, Down to 18). 
        # Inc: 1, 15, 51, 100 (Sum 167).
        # Dec: 100, 12, 18? No, 12 < 18 is up.
        # Dec: 100, 12, 9 (Sum 121). Total 188.

        # Is it possible the array in the prompt has a typo or my manual trace is missing something?
        # Let's look at 1, 15, 51, 45, 33, 100...
        # What if we skip 100? 1, 15, 51, 45, 33. Sum 145.
        # What if we take 1, 15, 51, 45, 33, 12, 9? Down after 51.
        # 1+15+51 = 67. 45+33+12+9 = 99. Total 67+99-51 = 115.

        # Wait, what if the sequence is 1, 15, 51, 100, 12, 18 is invalid.
        # What if the sequence is 1, 15, 51, 45, 33, 100 is invalid (up then down then up).

        # Let's reconsider the "Bi-tonic" definition in this specific context.
        # Often in these coding challenges, "Bi-tonic" means increasing OR decreasing is NOT enough, 
        # it must be Up then Down. But sometimes it includes Up only.
        # If Up only is allowed: Max is 1+15+51+100 = 167. Still not 194.
        # If Down only is allowed: Max is 51+45+33+12+9 = 150.

        # How to get 194?
        # 15 + 51 + 45 + 33 + 12 + 18 + 9 = 183.
        # 1 + 15 + 51 + 45 + 33 + 100 = 245.
        # Is it possible the array is 1, 15, 51, 45, 33, 100, 12, 18, 9?
        # Maybe the peak is not an element in the array? No, subsequences must use elements.
        # Maybe I am misinterpreting the array values?
        # [1, 15, 51, 45, 33, 100, 12, 18, 9]
        # Sum = 1+15+51+45+33+100+12+18+9 = 284.
        # Excluding 1: 15+51+45+33+100+12+18+9 = 283.
        # Excluding 1, 15: 51+45+33+100+12+18+9 = 268.

        # Is it possible the problem allows "Up then Flat then Down"? No, strictly increasing/decreasing usually.
        # Let's look at the second example: [80,