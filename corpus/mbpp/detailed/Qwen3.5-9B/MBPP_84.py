def sequence(n):
    """
    Computes the n-th number in the Newman-Conway Sequence.

    The Newman-Conway Sequence is defined recursively as follows:
      P(1) = 1
      P(2) = 1
      P(n) = P(P(n-1)) + P(n - P(n-1)) for n > 2

    This function implements the recursive definition using an iterative approach
    with dynamic programming (memoization via a list) to avoid exponential recursion.

    Parameters:
    n (int): The position in the sequence (1-based index).

    Returns:
    int: The n-th number in the Newman-Conway Sequence.

    Raises:
    TypeError: If n is not an integer.
    ValueError: If n is less than 1.
    """

    # Helper function to validate input type and range
    def _validate_input(value):
        if not isinstance(value, int):
            raise TypeError(f"Input must be an integer, got {type(value).__name__}")
        if value < 1:
            raise ValueError(f"Input must be a positive integer (>= 1), got {value}")
        return value

    # Step 1: Validate the input using the helper
    validated_n = _validate_input(n)

    # Step 2: Handle the degenerate case where n is 1
    if validated_n == 1:
        return 1

    # Step 3: Handle the specific base case where n is 2
    # Although the loop below can handle this, explicit checks are clearer for edge cases.
    if validated_n == 2:
        return 1

    # Step 4: Initialize the sequence list.
    # We need indices from 1 to validated_n. 
    # We will create a list of size (validated_n + 1) so index 0 is unused.
    # Initialize all values to 0 as placeholders.
    sequence_list = [0] * (validated_n + 1)

    # Step 5: Set the known base values based on the sequence definition
    # P(1) = 1
    sequence_list[1] = 1

    # P(2) = 1
    sequence_list[2] = 1

    # Step 6: Iteratively compute values from 3 up to validated_n
    # We use an explicit loop to ensure every step is visible and named.
    for current_index in range(3, validated_n + 1):
        # Retrieve the previously calculated value at (current_index - 1)
        # This is crucial for the recursive definition P(n) depends on P(n-1)
        prev_term_value = sequence_list[current_index - 1]

        # Calculate the first part of the recurrence: P(P(n-1))
        # Since we are building the list, the index we access here
        # must have already been computed.
        # P(n-1) is stored at index 'prev_term_value'.
        first_sub_term = sequence_list[prev_term_value]

        # Calculate the second part of the recurrence: P(n - P(n-1))
        # The index is (current_index - prev_term_value).
        # This index is guaranteed to be less than current_index,
        # meaning it has already been computed in this loop or earlier.
        second_sub_term_index = current_index - prev_term_value
        second_sub_term = sequence_list[second_sub_term_index]

        # Step 7: Apply the recurrence relation: P(n) = P(P(n-1)) + P(n - P(n-1))
        current_value = first_sub_term + second_sub_term

        # Step 8: Store the computed value in our list at the current index
        sequence_list[current_index] = current_value

    # Step 9: Return the value at the requested index
    return sequence_list[validated_n]