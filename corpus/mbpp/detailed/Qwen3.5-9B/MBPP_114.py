from typing import List, Tuple, Any, Dict

def _validate_tuple_list(input_list: List[Tuple[Any, ...]]) -> List[Tuple[Any, ...]]:
    """
    Validates that the input is a list of tuples.
    Returns the validated list. Raises a ValueError if validation fails.
    """
    if not isinstance(input_list, list):
        raise ValueError("Input must be a list.")

    for index, item in enumerate(input_list):
        if not isinstance(item, tuple):
            raise ValueError(f"Element at index {index} is not a tuple. It is {type(item).__name__}.")

    return input_list

def _count_occurrences(tuple_list: List[Tuple[Any, ...]]) -> Dict[Tuple[Any, ...], int]:
    """
    Counts the frequency of each unique tuple in the list.
    Returns a dictionary mapping the tuple to its count.
    """
    frequency_map: Dict[Tuple[Any, ...], int] = {}

    for item in tuple_list:
        if item in frequency_map:
            current_count = frequency_map[item]
            new_count = current_count + 1
            frequency_map[item] = new_count
        else:
            frequency_map[item] = 1

    return frequency_map

def _enhance_tuple(tuple_item: Tuple[Any, ...], count: int) -> Tuple[Any, ...]:
    """
    Appends the frequency count to the given tuple.
    Returns a new tuple with the count added at the end.
    """
    if not isinstance(tuple_item, tuple):
        raise TypeError("Input to _enhance_tuple must be a tuple.")

    count_as_int = int(count)
    enhanced_tuple = tuple_item + (count_as_int,)
    return enhanced_tuple

def _format_output(enhanced_list: List[Tuple[Any, ...]]) -> str:
    """
    Formats the list of enhanced tuples into the specific string representation required.
    The format mimics: '[(a, b, c, count), ...]'
    """
    string_parts = []

    for item in enhanced_list:
        # Convert the tuple to its string representation manually to ensure consistency
        # with the problem's expected output style (e.g., handling single element tuples like (9, 1))
        if len(item) == 0:
            part = "()"
        else:
            # Join elements with comma and space, wrapping in parentheses
            elements_str = ", ".join(str(elem) for elem in item)
            part = "(" + elements_str + ")"

        string_parts.append(part)

    result_string = "[" + ", ".join(string_parts) + "]"
    return result_string

def assign_freq(tuple_list: List[Tuple[Any, ...]]) -> str:
    """
    Assigns a frequency count to each unique tuple in the given list.

    The function counts how many times each tuple appears in the input list.
    It then creates a new list of tuples where the count is appended to each original tuple.
    Finally, it returns a string representation of this new list.

    Edge cases handled:
    - Empty input list: Returns "[]".
    - Single element list: Returns "[(element, 1)]".
    - All elements identical: Returns "[(element, count)]".
    - Tuples with single elements: Handled correctly.
    - Negative numbers and zero: Handled as standard elements.

    Args:
        tuple_list: A list containing tuples of any hashable elements.

    Returns:
        A string representing the list of tuples with appended frequencies.

    Raises:
        ValueError: If the input is not a list or contains non-tuple elements.
    """
    # Step 1: Validate input
    validated_list = _validate_tuple_list(tuple_list)

    # Step 2: Handle empty input explicitly
    if not validated_list:
        return "[]"

    # Step 3: Count frequencies
    frequency_counts = _count_occurrences(validated_list)

    # Step 4: Build the list of enhanced tuples
    enhanced_tuples: List[Tuple[Any, ...]] = []

    for original_tuple in validated_list:
        original_tuple_key = original_tuple
        count_value = frequency_counts[original_tuple_key]

        enhanced_item = _enhance_tuple(original_tuple_key, count_value)
        enhanced_tuples.append(enhanced_item)

    # Step 5: Format the output into a string
    final_string = _format_output(enhanced_tuples)

    return final_string