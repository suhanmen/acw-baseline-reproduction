from typing import Dict, List, Tuple, Any

def _validate_input(data: Any) -> Dict[str, int]:
    """
    Validates that the input is a dictionary where:
    - Keys are non-empty strings.
    - Values are non-negative integers.

    Raises:
        TypeError: If input is not a dict or contains invalid key/value types.
        ValueError: If any key is not a string, empty string, or any value is not a non-negative int.
    """
    if not isinstance(data, dict):
        raise TypeError(f"Expected a dictionary, but received {type(data).__name__}")

    for key in data:
        if not isinstance(key, str):
            raise TypeError(f"All keys must be strings. Found key of type {type(key).__name__}: '{key}'")
        if len(key) == 0:
            raise ValueError(f"All keys must be non-empty strings. Found empty key: '{key}'")

    for key, value in data.items():
        if not isinstance(value, int):
            raise TypeError(f"All values must be integers. Found value of type {type(value).__name__} for key '{key}'")
        if value < 0:
            raise ValueError(f"All values must be non-negative. Found negative value {value} for key '{key}'")

    return data


def _create_sorting_key_item(key: str, value: int) -> Tuple[Any, int]:
    """
    Creates a tuple suitable for sorting that prioritizes the integer value.
    This ensures stable sorting if we were to use Python's sort with a key lambda,
    but here we will return a tuple directly for sorting.
    We want to sort primarily by value.
    """
    return (value, key)


def _sort_items_list(items: List[Tuple[str, int]]) -> List[Tuple[str, int]]:
    """
    Takes a list of (key, value) tuples and sorts them by the value (index 1) in ascending order.
    Uses a stable sort algorithm provided by Python's Timsort.

    Args:
        items: List of tuples where each tuple is (string_key, integer_value).

    Returns:
        A new list of tuples sorted by integer_value in ascending order.
    """
    sorted_items = []
    # We perform a stable sort to ensure consistent results for equal values (though problem implies unique or no specific tie-break rule other than value).
    # The requirement is to sort by value. If values are equal, standard stable sort preserves original relative order.
    # However, looking at the problem, it doesn't specify tie-breaking for equal values.
    # We will sort by value primarily.

    # We create a copy to avoid modifying the input list during sorting (defensive programming)
    items_copy = list(items)

    # Define a key function for the sort: we want to sort by the second element (the score)
    def get_value_to_sort(item_tuple: Tuple[str, int]) -> int:
        return item_tuple[1]

    items_copy.sort(key=get_value_to_sort)

    return items_copy


def sort_counter(input_data: Dict[str, Any]) -> List[Tuple[str, int]]:
    """
    Sorts a dictionary by its values in ascending order and returns a list of tuples.

    The function performs the following steps:
    1. Validates the input to ensure it is a dictionary with string keys and non-negative integer values.
    2. Converts the dictionary into a list of tuples ((key, value)).
    3. Sorts the list of tuples based on the value (the second element of each tuple).
    4. Returns the sorted list.

    Edge cases handled:
    - Empty dictionary: Returns an empty list.
    - Single element: Returns a list with that single element.
    - All equal values: Maintains relative order (stable sort) or sorts by key if stable sort behavior allows (Python sort is stable).
    - Negative values: Explicitly rejected by validation.
    - Non-integer values: Explicitly rejected by validation.

    Args:
        input_data: A dictionary mapping string keys to non-negative integer values.

    Returns:
        A list of tuples sorted by value in ascending order.

    Raises:
        TypeError: If input is not a dict, keys are not strings, or values are not integers.
        ValueError: If any key is empty or any value is negative.
    """

    # Step 1: Validate Input
    validated_dict = _validate_input(input_data)

    # Step 2: Convert Dictionary to List of Tuples
    # We explicitly iterate to construct the list to ensure we handle the data structure correctly.
    items_list: List[Tuple[str, int]] = []

    for key in validated_dict:
        value = validated_dict[key]
        # Type safety check again after validation passed (defensive layer)
        if not isinstance(key, str) or not isinstance(value, int):
            # This part should theoretically never be reached due to _validate_input,
            # but included for explicit logic flow clarity in this defensive wrapper.
            raise TypeError("Internal error: Type mismatch in validated data.")

        items_list.append((key, value))

    # Step 3: Handle Empty Input Explicitly
    if len(items_list) == 0:
        return []

    # Step 4: Handle Single Element Explicitly (No sort needed, but sorting handles it safely)
    if len(items_list) == 1:
        return items_list

    # Step 5: Sort the List
    # We sort by the second element (the value) of each tuple.
    # Using a separate helper function for the key makes the logic explicit.
    sorted_items = _sort_items_list(items_list)

    return sorted_items