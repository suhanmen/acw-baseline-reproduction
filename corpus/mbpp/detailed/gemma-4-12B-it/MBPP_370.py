from typing import List, Tuple, Union

def float_sort(data: List[Tuple[str, str]]) -> List[Tuple[str, str]]:
    """
    Sorts a list of tuples by the numeric value of the second element (a string 
    representing a float) in descending order.

    Args:
        data: A list of tuples where each tuple contains a label and a float-string.

    Returns:
        A new list of tuples sorted by the float value in descending order.

    Raises:
        TypeError: If the input is not a list.
        ValueError: If any element in the tuple cannot be converted to a float.
        AttributeError: If the input structure is not a list of tuples.
    """
    # --- Input Validation ---

    if not isinstance(data, list):
        raise TypeError(f"Expected input type 'list', but got '{type(data).__name__}'")

    # Handle the empty input case explicitly
    if len(data) == 0:
        return []

    # Verify that every item in the list is a tuple of appropriate length
    for index, item in enumerate(data):
        if not isinstance(item, tuple):
            raise AttributeError(f"Item at index {index} is not a tuple.")
        if len(item) < 2:
            raise ValueError(f"Tuple at index {index} does not have at least 2 elements.")

    # --- Internal Logic ---

    def get_float_value(entry: Tuple[str, str]) -> float:
        """
        Helper function to extract and convert the float value from a tuple.
        """
        raw_value = entry[1]
        try:
            converted_value = float(raw_value)
            return converted_value
        except (ValueError, TypeError) as e:
            raise ValueError(
                f"Could not convert string '{raw_value}' to float. "
                f"Error: {e}"
            ) from e

    # We use a stable sort. Python's sorted() uses Timsort, which is stable.
    # We want descending order (highest value first).

    # To keep the code highly explicit and avoid complex lambdas, 
    # we create a temporary list of (float_value, original_index, original_tuple).
    # The index ensures we maintain stability if values are equal (though not required 
    # by the prompt, it's best practice).

    decorated_list = []
    for i, entry in enumerate(data):
        numeric_val = get_float_value(entry)
        # We store the numeric value, the original index to maintain stability, 
        # and the original tuple.
        decorated_list.append((numeric_val, i, entry))

    # Sort the decorated list. 
    # Since we want descending order, we sort by the numeric_val (the first element of the sub-tuple).
    # Python's sort is ascending by default, so we use reverse=True.
    decorated_list.sort(key=lambda x: x[0], reverse=True)

    # Extract the original tuples back from the decorated list.
    result = []
    for decorated_item in decorated_list:
        original_tuple = decorated_item[2]
        result.append(original_tuple)

    return result