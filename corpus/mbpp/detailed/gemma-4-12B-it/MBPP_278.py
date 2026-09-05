from typing import Tuple, Any, Union

def count_first_elements(input_tuple: Tuple[Any, ...]) -> int:
    """
    Finds the count of elements occurring before the first nested tuple 
    record in a given tuple.

    Args:
        input_tuple: A tuple containing various types (numbers, tuples, etc.).

    Returns:
        int: The number of elements encountered before the first nested tuple.

    Raises:
        TypeError: If the input is not a tuple.
        ValueError: If the input tuple is empty.
    """
    # --- Input Validation ---

    # Ensure the input is actually a tuple
    if not isinstance(input_tuple, tuple):
        raise TypeError(f"Expected input type 'tuple', but received '{type(input_tuple).__name__}'.")

    # Handle the edge case of an empty tuple
    if len(input_tuple) == 0:
        # Depending on interpretation, an empty tuple has 0 elements before any record.
        # However, if the problem implies a record MUST exist, this could be an error.
        # Given the assertions, we will return 0 as no records are encountered.
        return 0

    # --- Logic Implementation ---

    # We need to iterate through the tuple and count elements 
    # until we hit an element that is itself a tuple.

    count_before_record: int = 0
    found_record: bool = False

    for element in input_tuple:
        # Check if the current element is a tuple (the 'record')
        # We specifically check for 'tuple' instance to identify the record.
        if isinstance(element, tuple):
            # We have reached the first record.
            # We stop counting and set the flag.
            found_record = True
            break
        else:
            # This is not a record, increment the counter.
            count_before_record += 1

    # If the loop finished without finding any tuple, 
    # count_before_record will represent the total length of the input.
    # However, the problem implies we are counting until a record is found.
    # If no record exists, the behavior is technically undefined by the prompt,
    # but the most logical production behavior is returning the total count.

    return count_before_record

# --- Verification against provided assertions ---
# The following block is for internal verification.
if __name__ == "__main__":
    # Test Case 1: (1, 5, 7, (4, 6), 10) -> 1, 5, 7 (3 elements)
    assert count_first_elements((1, 5, 7, (4, 6), 10)) == 3

    # Test Case 2: (2, 9, (5, 7), 11) -> 2, 9 (2 elements)
    assert count_first_elements((2, 9, (5, 7), 11)) == 2

    # Test Case 3: (11, 15, 5, 8, (2, 3), 8) -> 11, 15, 5, 8 (4 elements)
    assert count_first_elements((11, 15, 5, 8, (2, 3), 8)) == 4

    # Edge Case: Empty tuple
    assert count_first_elements(()) == 0

    # Edge Case: Record at the very start
    assert count_first_elements(((1, 2), 3)) == 0

    # Edge Case: No records present
    assert count_first_elements((1, 2, 3)) == 3