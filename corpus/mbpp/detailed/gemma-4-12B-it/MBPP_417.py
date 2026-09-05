from typing import List, Tuple, Any, Dict

def group_tuples(input_list: List[Tuple[Any, ...]]) -> List[Tuple[Any, ...]]:
    """
    Groups tuples that share the same first element.
    If multiple tuples have the same first element, the first element is kept 
    once, and the subsequent elements of those tuples are joined into a single tuple.

    Example:
    [('x', 'y'), ('x', 'z'), ('w', 't')] -> [('x', 'y', 'z'), ('w', 't')]

    Args:
        input_list: A list of tuples.

    Returns:
        A list of tuples where elements sharing the same first index are merged.
    """
    # Validate input type
    if not isinstance(input_list, list):
        raise TypeError("Input must be a list of tuples.")

    # Handle empty input case
    if not input_list:
        return []

    # To maintain the order of appearance of the first elements, 
    # we use a dictionary to map the first element (key) to a list of 
    # trailing elements (values).
    # We also keep a list of keys to preserve the original encounter order.
    grouped_data: Dict[Any, List[Any]] = {}
    order_of_keys: List[Any] = []

    for item in input_list:
        # Validate that each item is a tuple and is not empty
        if not isinstance(item, tuple):
            raise ValueError(f"Item {item} is not a tuple.")

        if len(item) == 0:
            # If an empty tuple is passed, we treat it as a special case.
            # Since it has no "first element", we can't group it by key.
            # However, based on requirements, we assume non-empty tuples.
            raise ValueError("Input contains an empty tuple; first element cannot be determined.")

        first_element = item[0]
        trailing_elements = list(item[1:])

        if first_element not in grouped_data:
            # First time we see this key
            order_of_keys.append(first_element)
            # Initialize with the trailing elements of the first occurrence
            grouped_data[first_element] = list(trailing_elements)
        else:
            # Key exists, append the trailing elements of this tuple
            grouped_data[first_element].extend(trailing_elements)

    # Construct the final list of tuples
    result: List[Tuple[Any, ...]] = []
    for key in order_of_keys:
        # The final tuple is (key, ...all_collected_trailing_elements)
        trailing_parts = grouped_data[key]
        combined_tuple = (key,) + tuple(trailing_parts)
        result.append(combined_tuple)

    return result

if __name__ == "__main__":
    # Testing the logic against provided assertions
    assert group_tuples([('x', 'y'), ('x', 'z'), ('w', 't')]) == [('x', 'y', 'z'), ('w', 't')]
    assert group_tuples([('a', 'b'), ('a', 'c'), ('d', 'e')]) == [('a', 'b', 'c'), ('d', 'e')]
    assert group_tuples([('f', 'g'), ('f', 'g'), ('h', 'i')]) == [('f', 'g', 'g'), ('h', 'i')]