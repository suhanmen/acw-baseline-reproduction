def get_equal(input_list, expected_length):
    """
    Determines whether all tuples in the given list have the same length as the expected_length.

    Parameters:
    input_list (list): A list of tuples.
    expected_length (int): The length that all tuples are expected to have.

    Returns:
    str: A message indicating if all tuples have the same length or not.

    Raises:
    TypeError: If input_list is not a list or expected_length is not an integer.
    ValueError: If input_list is not a list of tuples or expected_length is negative.
    """

    # Validate input_list type
    if not isinstance(input_list, list):
        raise TypeError("The input_list must be a list.")

    # Validate expected_length type
    if not isinstance(expected_length, int) or isinstance(expected_length, bool):
        raise TypeError("The expected_length must be an integer.")

    # Validate expected_length value (negative length doesn't make sense for this context)
    if expected_length < 0:
        raise ValueError("The expected_length cannot be negative.")

    # Handle the edge case where the input list is empty
    if len(input_list) == 0:
        # Based on the logic of the assertions, an empty list implies no tuples to violate the condition,
        # but usually in strict logic "all" over an empty set is vacuously true.
        # However, without a target length defined, we cannot verify "same length as expected_length".
        # Given the problem context of checking against 'expected_length', returning False or a specific message
        # is safer. Let's assume if no tuples are provided, we cannot confirm they match the expected length.
        # But looking at standard behavior for "all X have property P", it is true.
        # However, if the requirement is "check if they have length N", and we have nothing, 
        # the strict interpretation is we cannot verify. 
        # Let's re-evaluate based on the provided assertions: none cover empty list.
        # A safe production stance: if the list is empty, there are no tuples to compare, 
        # so they trivially satisfy "all have length X" if we consider the set of mismatches empty.
        # BUT, practically, if a user asks "do all these have length 3", and shows 0, 
        # it's ambiguous. Let's stick to the logical mathematical truth: universal quantifier over empty set is True.
        return 'All tuples have same length'

    # Initialize a flag to track if any tuple matches the expected length
    # We will also validate each element is a tuple.
    first_tuple_validated = False
    all_match_expected = False

    # Iterate through each item in the input list
    for current_item in input_list:
        # Validate that each item in the list is a tuple
        if not isinstance(current_item, tuple):
            raise TypeError("All elements in input_list must be tuples.")

        # Validate that each item is actually a tuple (handling empty tuples correctly)
        current_length = len(current_item)

        # Check if the current tuple's length matches the expected length
        if current_length == expected_length:
            if not first_tuple_validated:
                # This is the first tuple we've seen that matches (or is the first valid check)
                # We need to see if ALL match.
                # If the first one matches, we tentatively say yes, but must check others.
                all_match_expected = True
                first_tuple_validated = True
            else:
                # Subsequent tuples match. Continue checking.
                all_match_expected = True
        else:
            # The current tuple does not match the expected length.
            # Therefore, not all tuples have the same length (as expected_length).
            all_match_expected = False
            # We can break early here because the condition is already violated.
            break

    # Construct the return message based on the validation result
    if all_match_expected:
        return 'All tuples have same length'
    else:
        return 'All tuples do not have same length'