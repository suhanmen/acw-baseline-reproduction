def count_occurrences_in_tuple(input_tuple, target_element):
    """
    Counts the number of occurrences of a specific element within a given tuple.

    Parameters:
    input_tuple (tuple): The tuple in which to search for the element.
    target_element: The element to count within the tuple. Can be any hashable type.

    Returns:
    int: The number of times target_element appears in input_tuple.

    Raises:
    TypeError: If input_tuple is not a tuple.
    ValueError: If the input tuple is empty and a count is somehow expected (though count is 0, this is a defensive check for future logic expansion if needed, but here we just return 0 for empty tuples as per standard behavior).
    """
    # Validate that the first argument is actually a tuple
    if not isinstance(input_tuple, tuple):
        raise TypeError(f"Expected the first argument to be a tuple, but received {type(input_tuple).__name__}.")

    # Validate that the target element is hashable (required for tuple membership/iteration checks in some contexts, 
    # though Python allows any object to be compared, we ensure type safety for robustness).
    # Note: In Python, you can technically have unhashable types in a tuple if they are mutable, 
    # but usually, tuples contain hashable items. However, the parameter 'target_element' could be anything.
    # We do not strictly enforce hashability of the target element unless it affects logic, 
    # but we do check if the input tuple itself is valid (which it is by the first check).

    # Handle the empty tuple edge case explicitly
    if len(input_tuple) == 0:
        return 0

    # Initialize a counter variable explicitly to track occurrences
    occurrence_count = 0

    # Iterate through each element in the tuple using explicit indexing or enumeration
    # We will use a simple for-loop to ensure every step is visible.
    for current_element in input_tuple:
        # Explicit comparison check
        if current_element is target_element:
            # We use 'is' for identity check if we want to be strict about object identity,
            # but the problem implies value equality. Usually, for counting in a general sense,
            # '==' is preferred unless the problem specifies identity. 
            # However, looking at the examples (integers), == and is behave similarly.
            # To be safe and standard for "counting occurrences" in data structures, we use '=='.
            # Let's re-evaluate: If the input is (10, 10) and target is 10, they are equal.
            # If the input is (a, b) where a and b are different objects with same value, == is better.
            # The problem statement implies value equality based on the integer examples.
            pass

        # Perform the value equality check
        if current_element == target_element:
            # Increment the counter only when a match is found
            occurrence_count += 1

    return occurrence_count


# Re-aliasing the function to match the specific name required by the problem's assertions
# to ensure the provided assertions work exactly as requested.
count_X = count_occurrences_in_tuple