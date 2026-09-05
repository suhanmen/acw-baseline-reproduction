from typing import Any, Iterable, List, Tuple, Optional, Union

# Define specific type alias for clarity in function signatures
TupleOfStr = Tuple[str, ...]
ListOfTupleOfStr = List[TupleOfStr]

def _validate_input_list(
    input_list: Optional[Iterable[Any]],
    source_name: str = "input_list"
) -> List[Tuple]:
    """
    Validates that the input is an iterable (but not a string) and contains only tuples.
    Returns a list of tuples if valid.
    Raises TypeError if validation fails.
    """
    if input_list is None:
        raise TypeError(f"{source_name} cannot be None. It must be an iterable of tuples.")

    # Check if the input is actually an iterable
    try:
        iter(input_list)
    except TypeError:
        raise TypeError(f"{source_name} must be an iterable.")

    # Special check to exclude strings, which are iterable but usually not intended here
    if isinstance(input_list, str):
        raise TypeError(f"{source_name} must be an iterable of tuples, not a string.")

    result_list: List[Tuple] = []

    for index, item in enumerate(input_list):
        # Check if the item is a tuple
        if not isinstance(item, tuple):
            raise TypeError(
                f"All elements in {source_name} must be tuples. "
                f"Index {index}: {type(item).__name__} ({item!r}) is not a tuple."
            )
        result_list.append(item)

    return result_list

def _get_key_from_tuple(t: Tuple) -> Any:
    """
    Helper to extract the first element of a tuple to be used as a grouping key.
    """
    if len(t) == 0:
        raise ValueError("Tuple must not be empty to extract the first element as a key.")
    return t[0]

def _group_tuples_by_first_element(
    tuple_list: List[Tuple]
) -> List[Tuple[List[Tuple]]]:
    """
    Groups the provided list of tuples based on their first element.
    Returns a list where each item is a list of tuples sharing the same first element.

    Logic:
    1. Initialize a dictionary to hold groups.
    2. Iterate through each tuple in the list.
    3. Extract the first element (the key).
    4. If the key exists, append the tuple to its list; otherwise, create a new list.
    """
    groups_map: dict[Any, List[Tuple]] = {}

    for current_tuple in tuple_list:
        key = _get_key_from_tuple(current_tuple)

        # Check if key exists in dictionary
        if key in groups_map:
            groups_map[key].append(current_tuple)
        else:
            # Create new list for this key
            new_list_for_key: List[Tuple] = [current_tuple]
            groups_map[key] = new_list_for_key

    # Convert dictionary items to a list of lists
    result: List[List[Tuple]] = [group_list for group_list in groups_map.values()]
    return result

def _flatten_and_transform_tuples(
    groups: List[List[Tuple]]
) -> List[Tuple[str, ...]]:
    """
    Transforms the grouped structure into the final output format.

    For each group of tuples:
    1. If the group has only one tuple, return it as-is.
    2. If the group has multiple tuples:
       - Create a new tuple.
       - First element: The common key (first element of the tuples).
       - Subsequent elements: The second elements of all tuples in the group.
       - Note: Based on the problem examples, even if the second elements repeat, 
         they are all included. E.g., [('f','g'), ('f','g')] -> ('f', 'g', 'g').
    """
    final_output: List[Tuple[str, ...]] = []

    for group in groups:
        # Determine the number of tuples in this group
        group_size = len(group)

        if group_size == 1:
            # Edge case: Single element group.
            # Return the tuple exactly as it is.
            # We assume elements are strings based on the problem context.
            final_output.append(group[0])
        else:
            # Multiple elements group.
            # We need to construct a new tuple.

            # 1. Get the common first element (the key) from the first tuple in the group.
            # Since they are grouped by key, any tuple in the group has this key.
            common_key: str = group[0][0]

            # 2. Collect the second elements from all tuples in the group.
            second_elements: List[str] = []
            for item_tuple in group:
                # Defensive check: ensure tuples have at least 2 elements for this logic
                if len(item_tuple) < 2:
                    raise ValueError(
                        f"All tuples in a shared-group must have at least 2 elements "
                        f"to be grouped by first element and compared by second. "
                        f"Found tuple with length {len(item_tuple)}: {item_tuple}"
                    )
                second_elements.append(item_tuple[1])

            # 3. Construct the new combined tuple.
            # Structure: (common_key, second_element_1, second_element_2, ...)
            combined_elements: List[Any] = [common_key]
            combined_elements.extend(second_elements)

            new_combined_tuple: Tuple[str, ...] = tuple(combined_elements)
            final_output.append(new_combined_tuple)

    return final_output

def group_tuples(input_data: Any) -> List[Tuple[str, ...]]:
    """
    Finds common first elements in a given list of tuples and groups them.

    If tuples share the same first element, it creates a new tuple containing:
    - The shared first element.
    - Followed by the second elements of all tuples in that group.

    If a first element is unique (appears in only one tuple), that tuple is returned unchanged.

    Args:
        input_data: An iterable of tuples (strings).

    Returns:
        A list of tuples representing the grouped results.

    Raises:
        TypeError: If input is None, not iterable, or contains non-tuples/strings.
        ValueError: If a tuple is empty.
    """
    # Step 1: Validate and convert input to a list of tuples
    validated_list = _validate_input_list(input_data)

    # Handle edge case: Empty input list
    if len(validated_list) == 0:
        return []

    # Step 2: Group tuples by their first element
    grouped_groups = _group_tuples_by_first_element(validated_list)

    # Step 3: Transform the groups into the specific output format
    result = _flatten_and_transform_tuples(grouped_groups)

    return result