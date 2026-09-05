from collections import defaultdict
from typing import List, Tuple, Dict, Union


def check_occurrences(data: Union[List[Tuple], None]) -> Dict[Tuple, int]:
    """
    Validates input data and returns a dictionary mapping each unique tuple to 
    its frequency count. Tuples are sorted internally before counting to handle
    order-agnostic comparisons if required by business logic (though current
    examples suggest direct matching).

    Input:
        data - A list of tuples, where each tuple contains two integers.

    Output:
        A dictionary with tuples as keys and their counts as values.

    Raises:
        TypeError: If the input is not a list or contains invalid elements.
    """
    # Validate the input type: must be a list.
    if not isinstance(data, list):
        raise TypeError("Input must be a list of tuples.")

    # Edge case: Handle empty input explicitly.
    if len(data) == 0:
        return {}

    # Validate each element in the list is a tuple.
    for index, item in enumerate(data):
        if not isinstance(item, tuple):
            raise TypeError(f"Element at index {index} is not a tuple.")

    # Optional: Validate tuple length (though problem implies pairs).
    for index, item in enumerate(data):
        if len(item) != 2:
            raise ValueError(f"Tuple at index {index} must contain exactly two elements.")

    # Validate that elements within tuples are integers (based on problem context).
    for index, item in enumerate(data):
        try:
            int(item[0])
            int(item[1])
        except TypeError:
            raise ValueError(f"Tuple elements at index {index} must be convertible to integers.")

    frequency_map = defaultdict(int)

    # Iterate through the data and count occurrences of each tuple.
    for current_tuple in data:
        frequency_map[current_tuple] += 1

    # Convert defaultdict to a standard dict for the final return.
    return dict(frequency_map)