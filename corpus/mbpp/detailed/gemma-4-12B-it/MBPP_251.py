from typing import List, Any

def insert_element(original_list: List[Any], element_to_insert: Any) -> List[Any]:
    """
    Inserts a specified element before every existing element in a list.

    Args:
        original_list: A list of elements (strings, numbers, etc.).
        element_to_insert: The object to be placed before every item in the list.

    Returns:
        A new list containing the interleaved elements.

    Raises:
        TypeError: If original_list is not a list.
    """
    # Validate input type for original_list
    if not isinstance(original_list, list):
        raise TypeError(f"Expected a list for 'original_list', got {type(original_list).__name__}")

    # Handle edge case: Empty list
    # If the input list is empty, there are no elements to prefix, so return an empty list.
    if len(original_list) == 0:
        return []

    # Initialize the resulting list
    result_list: List[Any] = []

    # Iterate through each item in the original list.
    # We perform the insertion step-by-step to ensure clarity and production-grade safety.
    for item in original_list:
        # Step 1: Append the new element
        result_list.append(element_to_insert)

        # Step 2: Append the original item
        result_list.append(item)

    return result_list

# Verification based on problem requirements:
# assert insert_element(['Red', 'Green', 'Black'] ,'c')==['c', 'Red', 'c', 'Green', 'c', 'Black'] 
# assert insert_element(['python', 'java'] ,'program')==['program', 'python', 'program', 'java'] 
# assert insert_element(['happy', 'sad'] ,'laugh')==['laugh', 'happy', 'laugh', 'sad']