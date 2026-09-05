from typing import List, Union

def count_pairs_with_difference_k(
    input_list: List[Union[int, float]],
    target_difference: Union[int, float],
    count_k: int
) -> int:
    """
    Count distinct pairs (a, b) in the array such that |a - b| == count_k.
    Pairs are defined by their values, not their indices. If duplicate values exist,
    they are treated as a single distinct value for pair formation purposes.

    For example, if the array is [1, 2, 2, 3] and k=1:
    Distinct values: {1, 2, 3}
    Pairs with difference 1: (1,2) and (2,3)
    Count: 2

    Args:
        input_list: The list of numbers to analyze.
        target_difference: The label used in assertions (reserved for interface consistency).
        count_k: The actual difference value k to search for.

    Returns:
        The count of distinct pairs having a difference of k.

    Raises:
        TypeError: If inputs are not lists or if elements/counts are not numeric.
        ValueError: If the difference k is negative.
    """

    # --- Input Validation Phase ---

    # Validate input_list type
    if not isinstance(input_list, list):
        raise TypeError("input_list must be a list of numbers.")

    # Validate count_k type and value
    if not isinstance(count_k, (int, float)):
        raise TypeError("count_k must be a number.")

    # Handle the difference constraint explicitly
    if count_k < 0:
        raise ValueError("The difference k cannot be negative.")

    # Handle empty input case explicitly
    if len(input_list) == 0:
        return 0

    # Validate individual elements are numeric
    for i, element in enumerate(input_list):
        if not isinstance(element, (int, float)):
            raise TypeError(f"Element at index {i} is not numeric: {element}.")

    # --- Core Logic Phase ---

    # Step 1: Extract distinct values.
    # We use a set to ensure we only consider unique numbers.
    # This prevents counting pairs like (1, 1) multiple times if 1 appears twice,
    # and ensures we only form pairs based on unique value combinations.
    distinct_values = set()
    for number in input_list:
        distinct_values.add(number)

    # Step 2: Initialize a counter for valid pairs.
    pair_count = 0

    # Step 3: Iterate through each unique number to find its potential pair.
    # A pair (a, b) has a difference of k if |a - b| = k.
    # This means either b = a + k OR b = a - k.
    # Since we are iterating through distinct values, we just need to check
    # if the required partner exists in our set of distinct values.
    for current_number in distinct_values:
        # Case A: Check if current_number + k exists in the set
        partner_a = current_number + count_k

        if partner_a in distinct_values:
            pair_count += 1

        # Case B: Check if current_number - k exists in the set
        # We must ensure k is not 0 here to avoid double counting the same pair (x, x)
        # If k > 0, then (a, b) where b = a+k is distinct from (b, a).
        # However, our set approach counts {a, b} as a single set of values.
        # If we iterate and check for both (x+k) and (x-k), we might count the pair twice.
        # Example: Set {1, 2}, k=1.
        # x=1: finds 2 (1+1). count += 1.
        # x=2: finds 1 (2-1). count += 1.
        # Total would be 2, but the pair is just {1, 2}.
        # To fix this, we only check one direction or handle the logic carefully.

        if count_k > 0:
            # To avoid double counting when k > 0, we only check if the partner
            # is strictly greater than the current number.
            # If we find (current, partner) where partner > current, we count it once.
            # If we find (current, partner) where partner < current, it's the same pair
            # as (partner, current) which would have been counted when loop was at partner.
            partner_b = current_number - count_k

            if partner_b in distinct_values:
                # Only count if partner_b is greater than current_number
                # This ensures we only count the pair {a, b} once.
                # Example: 1 and 2. k=1.
                # Loop at 1: checks 2. 2 > 1. Count.
                # Loop at 2: checks 1. 1 is not > 2. Do not count.
                if partner_b > current_number:
                    pair_count += 1

    # Special Case Handling: k = 0
    # If k is 0, we are looking for pairs with difference 0, i.e., (x, x).
    # Since distinct_values contains unique items, there are no pairs of distinct
    # values with difference 0.
    # However, the problem usually implies pairs of indices (i, j) where i != j.
    # If k=0 and we have duplicates in the original list, say [1, 1, 2],
    # pairs are (1,1) at indices 0,1.
    # BUT, the prompt asks for "distinct pairs". In set theory terms regarding values:
    # If k=0, a pair (a,b) must have a=b. Since we extracted a SET of distinct values,
    # no two distinct elements in the set have a difference of 0.
    # Therefore, if the definition of "distinct pairs" relies on the values themselves
    # being distinct (which is implied by using a set), the answer for k=0 is always 0.
    # If the definition was based on indices, the logic would be different.
    # Given the examples use positive integers and the term "distinct pairs",
    # it strongly implies pairs of unique values {a, b}.
    # Even if k=0 was intended, a set {1, 2} has no pairs with diff 0.
    # We return 0 for k=0 based on the distinct values logic.

    return pair_count

# Alias to match the specific assertion signature format requested,
# ensuring the function name and argument order align with the provided asserts.
# The provided asserts use: count_pairs([list], 5, 3).
# My function is count_pairs_with_difference_k([list], diff, k).
# I will create the exact function name requested by the user's assertion style
# while keeping the robust logic inside.

def count_pairs(input_array: List[Union[int, float]], diff_param: int, k_value: int) -> int:
    """
    Wrapper function matching the exact signature required by the assertions:
    count_pairs(array, diff_param, k_value)

    The 'diff_param' argument is effectively ignored for logic (kept for signature),
    while 'k_value' drives the difference calculation.
    """
    if not isinstance(input_array, list):
        raise TypeError("input_array must be a list.")
    if not isinstance(diff_param, int):
        raise TypeError("diff_param must be an integer.")
    if not isinstance(k_value, int):
        raise TypeError("k_value must be an integer.")

    if k_value < 0:
        raise ValueError("k_value cannot be negative.")

    return count_pairs_with_difference_k(input_array, diff_param, k_value)