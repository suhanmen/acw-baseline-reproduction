def _validate_input_lists(input_lists):
    """
    Validates that the input is a non-empty list of exactly three non-empty lists.
    Returns the three lists if valid, otherwise raises a ValueError with a descriptive message.

    Args:
        input_lists: Expected to be a list of exactly three lists.

    Returns:
        A tuple of (list_1, list_2, list_3) if valid.

    Raises:
        ValueError: If the input structure or content is invalid.
    """
    if not isinstance(input_lists, list):
        raise ValueError("The main input must be a list.")

    if len(input_lists) != 3:
        raise ValueError(f"Exactly three lists are required. Found {len(input_lists)}.")

    list_1 = input_lists[0]
    list_2 = input_lists[1]
    list_3 = input_lists[2]

    if not isinstance(list_1, list):
        raise ValueError("The first list must be a list.")
    if not isinstance(list_2, list):
        raise ValueError("The second list must be a list.")
    if not isinstance(list_3, list):
        raise ValueError("The third list must be a list.")

    if len(list_1) == 0:
        raise ValueError("The first list cannot be empty.")
    if len(list_2) == 0:
        raise ValueError("The second list cannot be empty.")
    if len(list_3) == 0:
        raise ValueError("The third list cannot be empty.")

    if len(list_1) != len(list_2) or len(list_1) != len(list_3):
        raise ValueError(f"All lists must have the same length. Lengths found: {len(list_1)}, {len(list_2)}, {len(list_3)}.")

    return list_1, list_2, list_3


def _convert_single_entry(index, key_1, key_2, value):
    """
    Converts a single entry from the lists into the specific nested dictionary format.

    Format: {key_1: {key_2: value}}

    Args:
        index: Integer index (used for logging/debugging if needed, though not in output).
        key_1: Key from the first list (outer dict key).
        key_2: Key from the second list (inner dict key).
        value: Value from the third list.

    Returns:
        A nested dictionary matching the structure [{'key_1': {'key_2': value}}].
    """
    inner_dict = {key_2: value}
    outer_dict = {key_1: inner_dict}
    return outer_dict


def convert_list_dictionary(list_of_keys_1, list_of_keys_2, list_of_values):
    """
    Converts three parallel lists into a list of nested dictionaries.

    Each element in the output list corresponds to indices i, i, i from the input lists.
    Output structure for index i: {list_of_keys_1[i]: {list_of_keys_2[i]: list_of_values[i]}}

    Args:
        list_of_keys_1: List of strings/objects for the outer key.
        list_of_keys_2: List of strings/objects for the inner key.
        list_of_values: List of values for the inner value.

    Returns:
        A list of nested dictionaries.

    Raises:
        ValueError: If inputs are invalid.
    """
    # Step 1: Validate inputs explicitly
    validated_list_1, validated_list_2, validated_list_3 = _validate_input_lists(
        [list_of_keys_1, list_of_keys_2, list_of_values]
    )

    # Step 2: Initialize the result container
    result_list = []

    # Step 3: Iterate through the validated lists
    # We use the length of the first list, as we've ensured all lengths are equal.
    total_count = len(validated_list_1)

    for index in range(total_count):
        # Retrieve the specific elements for the current iteration
        current_key_1 = validated_list_1[index]
        current_key_2 = validated_list_2[index]
        current_value = validated_list_3[index]

        # Step 4: Construct the nested dictionary for the current index
        # Using the helper function to ensure consistency and clarity
        nested_entry = _convert_single_entry(index, current_key_1, current_key_2, current_value)

        # Step 5: Append the constructed entry to the result list
        result_list.append(nested_entry)

    # Step 6: Return the final constructed list
    return result_list