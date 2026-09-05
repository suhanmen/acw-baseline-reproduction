from typing import List, Union

def _validate_input_is_list(input_data: any) -> None:
    """
    Validates that the provided input is indeed a list.
    Raises TypeError if input is not a list.
    """
    if not isinstance(input_data, list):
        raise TypeError(f"Expected input of type 'list', but received '{type(input_data).__name__}'.")

def _validate_elements_are_numeric(input_list: List[any]) -> None:
    """
    Validates that every element inside the list is either an int or a float.
    Raises ValueError if a non-numeric element is found.
    """
    for index, element in enumerate(input_list):
        if not isinstance(element, (int, float)):
            raise ValueError(f"Element at index {index} is not a number (type: {type(element).__name__}).")

def incr_list(l: list) -> list:
    """Return list with elements incremented by 1.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    # Step 1: Validate that the input is a list object.
    _validate_input_is_list(l)

    # Step 2: Validate that the contents are numeric.
    _validate_elements_are_numeric(l)

    # Step 3: Handle the edge case of an empty list immediately.
    if len(l) == 0:
        return []

    # Step 4: Prepare a container for the results.
    # We create a new list to ensure we do not mutate the original input list (immutability principle).
    result_list: List[Union[int, float]] = []

    # Step 5: Iterate through each element and perform the increment.
    for current_value in l:
        # Explicitly perform the increment operation.
        incremented_value = current_value + 1

        # Append the new value to the result container.
        result_list.append(incremented_value)

    # Step 6: Return the final constructed list.
    return result_list