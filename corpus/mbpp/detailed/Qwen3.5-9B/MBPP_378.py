from typing import List, Any

def move_first(input_list: List[Any]) -> List[Any]:
    """
    Shifts the last element of the given list to the first position.

    This function performs the following steps explicitly:
    1. Validates that the input is a list.
    2. Validates that the list is not empty (as there is no "last" element in an empty list).
    3. Extracts the last element.
    4. Removes the last element from the list.
    5. Creates a new list with the extracted last element at the front.
    6. Appends the remaining elements to this new list.
    7. Returns the new list.

    Edge cases handled:
    - Empty list: Raises a ValueError.
    - Single element list: Returns the same list (logically shifting one element to the front).
    - Lists with all equal elements: Handled correctly by the shifting logic.
    - Lists with zero, negative, or non-numeric elements: Handled generically.
    - Modifiable vs immutable elements: The original list is not modified; a new list is returned.

    Args:
        input_list (List[Any]): The list to be shifted.

    Returns:
        List[Any]: A new list with the last element moved to the first position.

    Raises:
        TypeError: If the input is not a list.
        ValueError: If the input list is empty.
    """

    # Step 1: Type validation - ensure the input is indeed a list
    if not isinstance(input_list, list):
        raise TypeError(f"Expected a list, but received {type(input_list).__name__}")

    # Step 2: Empty list validation - an empty list has no last element
    if len(input_list) == 0:
        raise ValueError("Cannot shift the last element to the first position of an empty list.")

    # Step 3: Define a variable to hold the count of elements for clarity
    count = len(input_list)

    # Step 4: Extract the last element explicitly using the calculated count
    # The last element is at index count - 1
    last_element = input_list[count - 1]

    # Step 5: Create a slice of the list that excludes the last element.
    # This slice goes from index 0 up to (but not including) the index of the last element.
    remaining_elements = input_list[0 : count - 1]

    # Step 6: Construct the result list by placing the last element first, followed by the remaining elements
    result_list = [last_element]
    result_list.extend(remaining_elements)

    # Step 7: Return the constructed new list
    # Note: We return a new list to avoid side effects on the caller's original list.
    return result_list