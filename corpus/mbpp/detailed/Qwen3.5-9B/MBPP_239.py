def _count_valid_sequences_recursive(target_length: int, current_value: int, max_value: int) -> int:
    """
    Recursively counts the number of valid sequences of a given target length.

    Parameters
    ----------
    target_length : int
        The remaining number of elements to place in the sequence (including the current position).
    current_value : int
        The value of the previously placed element. This is used to determine the lower bound 
        for the next element (which must be >= 2 * current_value).
    max_value : int
        The upper bound (inclusive) for any element in the sequence.

    Returns
    -------
    int
        The count of valid sequences that can be formed from the current state.
    """

    # Base Case 1: If the target length is 0, we have successfully formed a sequence
    # (of the original length) by making valid choices for all positions.
    if target_length == 0:
        return 1

    # Base Case 2: If the target length is negative, we have placed too many elements,
    # which is impossible given the initial call logic. This acts as a safeguard.
    if target_length < 0:
        return 0

    # Determine the minimum allowed value for the next element.
    # Constraint: next_element >= 2 * previous_element
    min_next_value = current_value * 2

    # Determine the range of valid values for the next element.
    # Constraint: min_next_value <= next_element <= max_value
    # If the minimum required value exceeds the maximum allowed value,
    # no valid next element exists.
    if min_next_value > max_value:
        return 0

    # Initialize a counter for the total ways to complete the sequence.
    total_ways = 0

    # Determine the maximum possible value we can pick for the next position
    # while still being able to potentially fill the remaining (target_length - 1) spots.
    # Optimization: If we pick a value too large, we might not be able to pick
    # the next value (since it must be >= 2 * current and <= max_value).
    # However, the recursive structure naturally handles this by returning 0 
    # if the next step is invalid. We iterate from the smallest valid value up to max_value.

    # Note: Since n (target_length) decreases by 1 each step and the values grow exponentially,
    # the search space is small enough for this explicit recursion to be efficient 
    # without needing dynamic programming or memoization for typical inputs 
    # (given the constraints implied by the problem type).

    # Iterate through every possible candidate for the next element.
    # We start from min_next_value and go up to max_value inclusive.
    candidate_next_value = min_next_value

    while candidate_next_value <= max_value:
        # Recursively call the function for the next position.
        # target_length decreases by 1.
        # candidate_next_value becomes the "current_value" for the next iteration.
        ways_for_this_candidate = _count_valid_sequences_recursive(
            target_length - 1, 
            candidate_next_value, 
            max_value
        )

        # Add the results of the recursive call to our running total.
        total_ways += ways_for_this_candidate

        # Move to the next candidate value.
        candidate_next_value += 1

    return total_ways


def get_total_number_of_sequences(n: int, m: int) -> int:
    """
    Calculates the total number of sequences of length n such that each element is 
    greater than or equal to twice the previous element and less than or equal to m.

    Constraints Logic:
    - Length of sequence: n
    - Elements must be: prev * 2 <= current <= m

    Parameters
    ----------
    n : int
        The length of the sequence to form.
    m : int
        The maximum allowed value for any element in the sequence.

    Returns
    -------
    int
        The total count of valid sequences.
    """

    # --- Input Validation ---

    # Validate that n is an integer.
    if not isinstance(n, int):
        raise TypeError(f"Expected 'n' to be an integer, got {type(n).__name__}.")

    # Validate that m is an integer.
    if not isinstance(m, int):
        raise TypeError(f"Expected 'm' to be an integer, got {type(m).__name__}.")

    # Validate that n is non-negative. Sequence length cannot be negative.
    if n < 0:
        raise ValueError(f"Expected 'n' to be non-negative, got {n}.")

    # Validate that m is non-negative. A maximum bound less than zero makes sense only 
    # if the numbers themselves can be negative, but the recurrence (x*2) implies 
    # positive growth from non-negative starts, or simply no solutions if m < 0.
    # Given the problem context of "numbers" usually implying natural numbers in this specific combinatorial 
    # context (and the test cases use positive integers), we treat m < 0 as yielding 0 sequences 
    # because the first element must be >= 2 * previous. If there is no "previous", 
    # usually the first element just needs to be <= m. 
    # However, looking at the recurrence: min_next = current * 2.
    # If we start with a hypothetical "previous" of 0 (which is common in such problems 
    # to allow the first element to be >= 0), then first element >= 0.
    # If m < 0, no element >= 0 can exist <= m.
    if m < 0:
        return 0

    # Special Case: n = 0
    # A sequence of length 0 is technically one valid sequence (the empty sequence).
    # However, based on typical combinatorial problem interpretations and the provided test cases,
    # if the user asks for a sequence of length 0, the answer is usually 1.
    # Let's verify with the logic:
    # If n=0, the recursive call gets target_length=0 immediately and returns 1.
    # This is mathematically consistent.
    if n == 0:
        return 1

    # Define the starting value for the first element.
    # The problem states: "each of the next element is ...". This implies a constraint applies
    # between element i and element i+1.
    # What about the first element (element 1)?
    # It must satisfy: 2 * (previous) <= element_1 <= m.
    # Since there is no previous element, we assume the implicit previous value for the 
    # first element is 0 (or -infinity, but practically 0 fits the "greater than or equal to twice"
    # pattern starting from non-negative numbers).
    # Thus, first element >= 2 * 0 = 0.
    # Combined with first element <= m.

    # If m < 0, we already returned 0 above.
    # If m >= 0, the first element can be any integer from 0 to m.
    # Wait, are we dealing with positive integers only? 
    # The test cases:
    # get_total_number_of_sequences(10, 4) == 4
    # If we allow 0:
    # Sequence starting with 0: next >= 0. 0,0,0... works?
    # Let's trace the test case get_total_number_of_sequences(10, 4) == 4.
    # If we allow 0, we could have (0,0,0,0,0,0,0,0,0,0).
    # Then (1,2,4,8...) -> 8 > 4, so (1,2,4) len 3.
    # If 0 is allowed, the number of sequences would likely be much higher.
    # This suggests the domain might be POSITIVE integers only (1 to m), OR 
    # the recurrence implies strict growth from a specific start.
    # Let's re-read: "each of the next element is greater than or equal to twice of the previous".
    # If the domain is positive integers:
    # First element >= 1 (implied domain constraint).
    # First element <= m.
    # Next >= 2 * prev.

    # Let's test the hypothesis: Domain is Positive Integers [1, m].
    # Case n=10, m=4.
    # Start with 1: 1, 2, 4 (next >= 8 > 4, stop). Len 3.
    # Start with 2: 2, 4 (next >= 8). Len 2.
    # Start with 3: 3 (next >= 6). Len 1.
    # Start with 4: 4 (next >= 8). Len 1.
    # If the question implies sequences MUST be of length n.
    # Then starting with 1: 1, 2, 4 (fail, need len 10).
    # Starting with any number >= 1, the sequence dies out quickly.
    # How can we get length 10 with m=4?
    # Only if 0 is allowed and 0*2=0 allows repeating zeros?
    # If 0,0,0... is valid.
    # 0,0,0,0,0,0,0,0,0,0 (Valid)
    # 1,2,4... fails length.
    # 0,1,2,4... fails.
    # Is there another interpretation?
    # Maybe "next element is greater than or equal to twice the previous" applies only if the previous is non-zero?
    # Or maybe the sequence is circular? No.
    # Let's look at the second case: get_total_number_of_sequences(5, 2) == 6.
    # If domain is [0, 2]:
    # All zeros: 0,0,0,0,0 (1)
    # Start 1: 1, 2, 4(x)... Max len 2.
    # Start 2: 2, 4(x)... Max len 1.
    # Total len 5? Impossible if growth is exponential.

    # RE-EVALUATION OF THE PROBLEM STATEMENT
    # "each of the next element is greater than or equal to twice of the previous element"
    # Is it possible the problem means "less than or equal to TWICE" (<= 2 * prev)?
    # If x_{i+1} <= 2 * x_i and x_{i+1} >= x_i (implied by "sequences" often being non-decreasing? No, prompt says >= 2*prev).

    # Let's reconsider the "0" hypothesis.
    # If the condition is x_{i+1} >= 2 * x_i.
    # If x_i = 0, then x_{i+1} >= 0.
    # If we pick 0, we can pick 0 again forever.
    # Sequence: 0,0,0,0,0,0,0,0,0,0. (Length 10, max 4). Count = 1.
    # Sequence: 0,0,0,0,0,0,0,0,1... -> 1 >= 0. Next >= 2.
    # 0,0,0,0,0,0,0,0,1,2. (Length 10, max 4).
    # How many such sequences?
    # This seems complex to enumerate mentally.

    # Let's look at the third case: n=16, m=3 -> 84.
    # If domain is [0, 3].
    # If we treat this as a variation of "Partitions into distinct powers of 2" or similar?
    # Or maybe the first element doesn't have the "x * 2" constraint relative to a "phantom 0".
    # Constraint: x_1 <= m.
    # Constraint: x_{i+1} >= 2 * x_i for i > 1?
    # No, "each of the next element". Usually implies all transitions.

    # Let's try a different angle. What if the numbers are NOT integers but the count is small?
    # What if the problem implies x_{i+1} >= x_i (non-decreasing) AND x_{i+1} <= 2 * x_i?
    # Prompt: "greater than or equal to twice of the previous element" -> x_{i+1} >= 2 * x_i.
    # This is unambiguous.

    # Let's re-read the test cases carefully.
    # 1. n=10, m=4 => 4
    # 2. n=5, m=2 => 6
    # 3. n=16, m=3 => 84

    # Hypothesis A: The sequence elements must be strictly positive (1..m).
    # With growth >= 2, max length for m=4 is 3 (1,2,4). We need 10. Impossible.
    # Hypothesis B: The sequence elements can be 0. And 0 allows infinite extension.
    # Let's calculate for n=10, m=4, allowing 0.
    # Let f(k, min_val) be the number of sequences of length k starting with min_val.
    # This is getting complicated to derive mentally.

    # Wait