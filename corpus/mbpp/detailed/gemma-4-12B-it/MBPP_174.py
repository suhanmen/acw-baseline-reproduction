from typing import List, Tuple, Any, Dict


def group_keyvalue(pairs: List[Tuple[Any, Any]]) -> Dict[Any, List[Any]]:
    """
    Groups a sequence of key-value pairs into a dictionary where each key
    maps to a list of all values associated with that key in the input sequence.

    Args:
        pairs: A list of tuples, where each tuple contains a key and a value.

    Returns:
        A dictionary where keys are the first elements of the tuples and 
        values are lists of the second elements.

    Raises:
        TypeError: If the input is not a list or if elements are not tuples of length 2.
        ValueError: If the input list is null or contains malformed data.
    """
    # Validate that the input is a list
    if not isinstance(pairs, list):
        raise TypeError(f"Expected input of type list, but received {type(pairs).__name__}")

    # Handle the edge case of an empty list immediately
    if len(pairs) == 0:
        return {}

    # Initialize the resulting dictionary
    grouped_data: Dict[Any, List[Any]] = {}

    # Iterate through the sequence of pairs
    for index, item in enumerate(pairs):
        # Validate that each element is a tuple (or list) of exactly 2 elements
        if not isinstance(item, (tuple, list)):
            raise ValueError(f"Element at index {index} is not a tuple/list. Got: {item}")

        if len(item) != 2:
            raise ValueError(f"Element at index {index} must have exactly 2 items. Got length {len(item)}")

        # Extract key and value for clarity
        key = item[0]
        value = item[1]

        # Defensive check: ensure the key is hashable (since it will be a dict key)
        # Note: In Python, most basic types are hashable.
        try:
            hash(key)
        except TypeError:
            raise TypeError(f"Key at index {index} is not hashable: {key}")

        # Check if the key already exists in our result dictionary
        if key in grouped_data:
            # If it exists, append the new value to the existing list
            current_list = grouped_data[key]
            current_list.append(value)
        else:
            # If it does not exist, create a new list with the current value
            new_list = [value]
            grouped_data[key] = new_list

    return grouped_data