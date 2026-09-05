def count_true_values(input_list):
    """
    Counts the number of True boolean values in the provided list.

    This function performs rigorous validation of the input list before
    attempting to process it. It handles various edge cases explicitly,
    including empty lists, lists with no True values, lists with all True values,
    and lists containing invalid (non-boolean) elements.

    Args:
        input_list (list): A list intended to contain boolean values.

    Returns:
        int: The count of True values found in the list.
             Returns 0 if the input is None or an empty list.

    Raises:
        TypeError: If the input is not a list.
        ValueError: If the input list contains non-boolean elements.

    Edge Cases Handled:
        - None input: Treated as invalid (raises TypeError).
        - Empty list: Returns 0 without raising an error.
        - Single element: Correctly counts if True or False.
        - All True: Correctly returns the length of the list.
        - All False: Correctly returns 0.
        - Mixed valid values: Correctly counts only Trues.
        - Invalid types: Raises ValueError for non-boolean elements.
    """

    # Step 1: Validate that the input is actually a list.
    # We check against the list type explicitly to prevent passing strings
    # (which are sequences in Python) or other iterable objects.
    if input_list is None:
        raise TypeError("Input must be a list, but received None.")

    if not isinstance(input_list, list):
        raise TypeError(f"Input must be a list, but received type: {type(input_list).__name__}.")

    # Step 2: Handle the empty list edge case explicitly.
    # This avoids unnecessary iteration and immediately returns a defined result.
    if len(input_list) == 0:
        return 0

    # Step 3: Initialize a counter variable to keep track of true values.
    # Using a named variable makes the accumulation logic explicit.
    true_count = 0

    # Step 4: Iterate through each element in the list one by one.
    for current_element in input_list:
        # Step 5: Validate that every element is a boolean.
        # If a non-boolean is found, we raise a ValueError immediately.
        if not isinstance(current_element, bool):
            raise ValueError(
                f"All elements must be booleans, but found an element of type "
                f"{type(current_element).__name__} with value '{current_element}'. "
                f"Index: {input_list.index(current_element)}"
            )

        # Step 6: Check the value of the element.
        # We explicitly check for truthiness here to count only True booleans.
        # Note: In Python, `True` is the only truthy boolean. `False` is falsy.
        # We are specifically counting boolean `True` values, not just truthy values,
        # though for pure booleans, this is equivalent.
        if current_element is True:
            # Increment our counter if the element is True.
            true_count += 1

    # Step 7: Return the final count.
    return true_count