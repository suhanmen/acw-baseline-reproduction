import copy


def _validate_dictionary(input_dict, index: int) -> None:
    """
    Validates that the provided item is a dictionary.

    If the item is not a dictionary, raises a TypeError with a message
    indicating which argument (by 1-based index) failed validation.

    Args:
        input_dict: The item to validate.
        index: The 1-based argument index for error messages.

    Raises:
        TypeError: If input_dict is not a dictionary.
    """
    if not isinstance(input_dict, dict):
        raise TypeError(
            f"Argument #{index} must be a dictionary, but got '{type(input_dict).__name__}'."
        )


def _merge_two_dicts(
    base_dict: dict, 
    overlay_dict: dict
) -> dict:
    """
    Merges two dictionaries, returning a new dictionary.

    The overlay_dict takes precedence over the base_dict for any 
    colliding keys. This function does not modify either input.

    Args:
        base_dict: The first dictionary.
        overlay_dict: The second dictionary.

    Returns:
        A new dictionary containing all keys from both inputs, 
        with overlay values overwriting base values.
    """
    result = {}

    # Step 1: Copy all items from the base dictionary
    for key, value in base_dict.items():
        result[key] = value

    # Step 2: Overlay all items from the second dictionary
    for key, value in overlay_dict.items():
        result[key] = value

    return result


def merge_dictionaries_three(
    dict_one: dict, 
    dict_two: dict, 
    dict_three: dict
) -> dict:
    """
    Merges three dictionaries into a single dictionary.

    The merge order is: dict_three -> dict_two -> dict_one.
    This means values from dict_three have the highest precedence,
    followed by dict_two, then dict_one. Keys present in multiple
    dictionaries will have their value from the last dictionary 
    processed (highest index) in the final result.

    Args:
        dict_one: The first dictionary (lowest precedence).
        dict_two: The second dictionary (medium precedence).
        dict_three: The third dictionary (highest precedence).

    Returns:
        A new dictionary containing the merged values.

    Raises:
        TypeError: If any argument is not a dictionary.
    """
    # Explicit validation of all inputs
    _validate_dictionary(dict_one, 1)
    _validate_dictionary(dict_two, 2)
    _validate_dictionary(dict_three, 3)

    # Handle edge case where one of the dictionaries is empty
    # The logic below handles this naturally, but we ensure deep copy safety
    # if inputs were lists (not applicable here as inputs are dicts), 
    # but we do create an explicit deep copy to ensure immutability of inputs.

    # Step 1: Deep copy the first dictionary to ensure we don't mutate it
    merged_result = copy.deepcopy(dict_one)

    # Step 2: Merge the second dictionary into the result
    # We use a temporary variable to hold the intermediate state
    intermediate_result = _merge_two_dicts(merged_result, dict_two)

    # Step 3: Merge the third dictionary into the intermediate result
    final_result = _merge_two_dicts(intermediate_result, dict_three)

    return final_result