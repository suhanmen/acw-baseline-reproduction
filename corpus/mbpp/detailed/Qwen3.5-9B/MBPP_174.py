from typing import Any, Dict, Iterable, List, Tuple, Union

Key = Any
Value = Any

# Type alias for a single key-value pair tuple
Pair = Tuple[Key, Value]

def _validate_input_pairs(pairs: Iterable[Any]) -> Iterable[Pair]:
    """
    Validates that the input is an iterable of exactly 2-element tuples/lists.
    Returns the validated iterable.

    Raises:
        TypeError: If the input is not iterable.
        TypeError: If any element is not a sequence or a tuple/list of length 2.
    """
    try:
        pair_iter = iter(pairs)
    except TypeError as e:
        raise TypeError(f"Input must be iterable of pairs, got: {type(pairs).__name__}") from e

    for index, item in enumerate(pair_iter):
        # Check if the item is a sequence (tuple, list, etc.)
        if not isinstance(item, (tuple, list)):
            raise TypeError(
                f"Each item in the input sequence must be a tuple or list "
                f"of key-value pairs, but item at index {index} is: {type(item).__name__}"
            )

        # Check length of the pair
        if len(item) != 2:
            raise TypeError(
                f"Each item must be a pair (length 2), but item at index {index} "
                f"has length {len(item)}: {item}"
            )

        # Extract key and value explicitly
        k, v = item[0], item[1]
        yield k, v

def _initialize_output_structure() -> Dict[Key, List[Value]]:
    """
    Initializes and returns an empty dictionary intended to hold the result.
    The value type of the dictionary will be a list.
    """
    return {}

def _ensure_list_exists(key: Key, existing_dict: Dict[Key, List[Value]]) -> List[Value]:
    """
    Ensures that the list for the given key exists in the dictionary.
    If it does not exist, creates a new empty list and assigns it.
    Returns the reference to the list.
    """
    if key not in existing_dict:
        existing_dict[key] = []
    return existing_dict[key]

def group_keyvalue(pairs: Iterable[Any]) -> Dict[Key, List[Value]]:
    """
    Groups a sequence of key-value pairs into a dictionary of lists.

    This function performs the following steps:
    1. Validates that the input is an iterable.
    2. Validates that every element in the iterable is a 2-tuple or 2-list.
    3. Initializes an empty dictionary to store the results.
    4. Iterates through the validated pairs.
    5. For each pair, ensures the key has an associated list in the dictionary.
    6. Appends the value to the corresponding list.

    Args:
        pairs: An iterable of (key, value) tuples or lists.

    Returns:
        A dictionary where each key maps to a list of values.

    Raises:
        TypeError: If the input structure is invalid.
    """
    # Step 1: Validate and convert the input into a concrete list of validated pairs
    # We convert to a list here to ensure we can iterate safely and handle generator inputs.
    # Validation happens within the generator _validate_input_pairs.
    validated_pairs_list = list(_validate_input_pairs(pairs))

    # Step 2: Initialize the output structure
    result_dict: Dict[Key, List[Value]] = _initialize_output_structure()

    # Step 3: Process each validated pair
    # If the list is empty (edge case: empty input), this loop simply won't execute,
    # and an empty dictionary is returned, which is correct.
    for pair in validated_pairs_list:
        # Explicitly unpack the pair for clarity and error checking (though already validated)
        current_key: Key = pair[0]
        current_value: Value = pair[1]

        # Step 4: Get or create the list for the current key
        target_list = _ensure_list_exists(current_key, result_dict)

        # Step 5: Append the value to the list
        target_list.append(current_value)

    return result_dict