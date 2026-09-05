def drop_empty(data: dict) -> dict:
    """
    Drops all key-value pairs from the input dictionary where the value is None (empty).

    This function performs defensive programming by:
    1. Validating that the input is indeed a dictionary.
    2. Iterating through all items explicitly.
    3. Constructing a new dictionary containing only non-empty items.

    Parameters:
    data (dict): The input dictionary to process.

    Returns:
    dict: A new dictionary with all entries where value is None removed.

    Raises:
    TypeError: If the input is not a dictionary.
    """

    # Step 1: Input Validation
    if not isinstance(data, dict):
        raise TypeError(
            f"Input must be a dictionary. Received type: {type(data).__name__}"
        )

    # Initialize an empty dictionary to store the result
    result_dictionary = {}

    # Step 2: Iterate through each key-value pair explicitly
    for current_key in data.keys():
        # Retrieve the value associated with the current key
        current_value = data[current_key]

        # Step 3: Check if the value is None (empty)
        if current_value is None:
            # If the value is None, skip this entry (do not add to result)
            continue
        else:
            # If the value is not None, add the pair to the result dictionary
            result_dictionary[current_key] = current_value

    # Return the constructed result dictionary
    return result_dictionary