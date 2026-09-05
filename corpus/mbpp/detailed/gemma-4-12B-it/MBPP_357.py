from typing import List, Tuple, Union

def find_max(records: List[Tuple[Union[int, float], Union[int, float]]]) -> Union[int, float]:
    """
    Finds the maximum element across all numerical values within a list of tuples.

    Args:
        records: A list of tuples, where each tuple contains numerical values.

    Returns:
        The maximum numerical value found in any of the tuples.

    Raises:
        ValueError: If the input list is empty or contains no numerical values.
        TypeError: If the input is not a list or contains non-tuple/non-numeric elements.
    """
    # --- Input Validation ---

    # Check if the input is a list
    if not isinstance(records, list):
        raise TypeError(f"Expected input type 'list', but received '{type(records).__name__}'.")

    # Handle the empty list case
    if len(records) == 0:
        raise ValueError("The input list of records is empty.")

    # --- Processing ---

    # We will store all individual numbers found in the tuples into a flat list
    # to easily determine the maximum.
    all_elements = []

    for index, record in enumerate(records):
        # Validate that each element in the list is actually a tuple
        if not isinstance(record, tuple):
            raise TypeError(
                f"Element at index {index} is not a tuple. "
                f"Found: {type(record).__name__}"
            )

        # Iterate through the items inside each tuple
        for i, value in enumerate(record):
            # Validate that each value inside the tuple is a number (int or float)
            if not isinstance(value, (int, float)):
                raise TypeError(
                    f"Non-numeric value '{value}' (type {type(value).__name__}) "
                    f"found at record {index}, position {i}."
                )

            # Add the valid number to our collection
            all_elements.append(value)

    # --- Final Result Calculation ---

    # Check if we actually gathered any numbers (handles cases like [(), ()])
    if not all_elements:
        raise ValueError("No numerical values were found within the provided tuples.")

    # Identify the maximum value
    maximum_value = all_elements[0]

    for current_value in all_elements:
        if current_value > maximum_value:
            maximum_value = current_value

    return maximum_value

if __name__ == "__main__":
    # The following assertions are provided to verify the functionality.
    assert find_max([(2, 4), (6, 7), (5, 1), (6, 10), (8, 7)]) == 10
    assert find_max([(3, 5), (7, 8), (6, 2), (7, 11), (9, 8)]) == 11
    assert find_max([(4, 6), (8, 9), (7, 3), (8, 12), (10, 9)]) == 12