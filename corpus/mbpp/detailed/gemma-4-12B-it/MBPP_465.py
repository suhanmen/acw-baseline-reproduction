from typing import Dict, Any

def drop_empty(data_dict: Dict[Any, Any]) -> Dict[Any, Any]:
    """
    Takes a dictionary and returns a new dictionary containing only the items 
    where the value is not 'None'.

    Args:
        data_dict (Dict[Any, Any]): The input dictionary to process.

    Returns:
        Dict[Any, Any]: A new dictionary with items having None values removed.

    Raises:
        TypeError: If the input is not a dictionary.
    """
    # Validate input type
    if not isinstance(data_dict, dict):
        raise TypeError(f"Expected input of type 'dict', but received '{type(data_dict).__name__}'")

    # Handle the edge case of an empty dictionary immediately
    if not data_dict:
        return {}

    # Initialize a new dictionary to store the results.
    # We create a new dictionary instead of modifying the input in-place 
    # to ensure functional purity and avoid side effects.
    result_dict: Dict[Any, Any] = {}

    # Iterate through the key-value pairs of the input dictionary
    for key, value in data_dict.items():
        # Explicitly check if the value is None.
        # Note: We are looking specifically for None, not "falsy" values 
        # (like 0, empty strings, or empty lists), as per the problem requirements.
        is_value_none = (value is None)

        if not is_value_none:
            # If the value is not None, add it to our result dictionary.
            result_dict[key] = value
        else:
            # The value is None, so we skip adding it to result_dict.
            pass

    return result_dict

# Test assertions to verify behavior
if __name__ == "__main__":
    # Test Case 1: None at the end
    assert drop_empty({'c1': 'Red', 'c2': 'Green', 'c3': None}) == {'c1': 'Red', 'c2': 'Green'}

    # Test Case 2: Multiple None values in the middle and end
    assert drop_empty({'c1': 'Red', 'c2': None, 'c3': None}) == {'c1': 'Red'}

    # Test Case 3: None at the beginning and end
    assert drop_empty({'c1': None, 'c2': 'Green', 'c3': None}) == {'c2': 'Green'}

    # Additional Edge Cases
    # Empty dictionary
    assert drop_empty({}) == {}

    # All None values
    assert drop_empty({'a': None, 'b': None}) == {}

    # No None values
    assert drop_empty({'x': 1, 'y': 2}) == {'x': 1, 'y': 2}

    # Falsy values that are NOT None (should be kept)
    assert drop_empty({'a': 0, 'b': '', 'c': False}) == {'a': 0, 'b': '', 'c': False}