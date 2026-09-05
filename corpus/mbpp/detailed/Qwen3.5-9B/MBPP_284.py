from typing import Any, List

def is_valid_string_input(input_value: Any) -> bool:
    """
    Validates that the given input is a string.

    Parameters:
    input_value (Any): The value to check.

    Returns:
    bool: True if the value is a string, False otherwise.
    """
    return isinstance(input_value, str)

def raise_type_error(message: str) -> None:
    """
    Raises a TypeError with the provided message.

    Parameters:
    message (str): The error message to include in the exception.

    Raises:
    TypeError: Always raised with the provided message.
    """
    raise TypeError(message)

def are_all_items_equal_to_string(items: List[Any], target_string: str) -> bool:
    """
    Checks whether all items in a list are equal to a given string.

    Parameters:
    items (List[Any]): The list of items to check.
    target_string (str): The string value that all items must equal.

    Returns:
    bool: True if all items are equal to target_string, False otherwise.

    Raises:
    TypeError: If target_string is not a string.
    """
    # Validate the target string input explicitly
    if not is_valid_string_input(target_string):
        raise_type_error("The target value must be a string.")

    # Handle empty list case: by definition, all elements (zero of them) are equal
    if len(items) == 0:
        return True

    # Check the first element against the target string
    first_item = items[0]

    # If the first item is not equal to the target, return False immediately
    if first_item != target_string:
        return False

    # Iterate through the rest of the list (starting from the second element)
    # We explicitly check each element one by one
    for index in range(1, len(items)):
        current_item = items[index]

        # Check if the current item matches the target string
        if current_item != target_string:
            return False

    # If we have reached this point, all items matched the target string
    return True

def check_element(items: List[Any], value: str) -> bool:
    """
    Public wrapper function to check if all elements in a list equal a given string.
    Delegates the core logic to are_all_items_equal_to_string for clarity and separation of concerns.

    Parameters:
    items (List[Any]): The list of items to evaluate.
    value (str): The string value to compare all items against.

    Returns:
    bool: True if all items are equal to the value, False otherwise.

    Raises:
    TypeError: If 'value' is not a string.
    """
    return are_all_items_equal_to_string(items, value)