def _validate_input_element(element, context=""):
    """
    Validates that a single element is either an integer or a list of valid elements.
    Raises a ValueError if the element is of an invalid type.

    Args:
        element: The element to validate.
        context: A string describing the position/context of the element for error messages.

    Returns:
        None if the element is valid.

    Raises:
        ValueError: If the element is neither an int nor a list, or if the list contains invalid items.
    """
    if isinstance(element, int):
        return

    if isinstance(element, list):
        for index, sub_element in enumerate(element):
            context_detail = f"{context} (element at index {index})" if context else f"element at index {index}"
            _validate_input_element(sub_element, context_detail)
        return

    raise ValueError(f"Invalid type encountered: {type(element).__name__}. "
                     f"Expected int or list of ints. "
                     f"Invalid value found at: {context or 'root'} = {element}")


def _sum_integer_list_helper(integers):
    """
    Helper function to sum a list of integers using a simple loop.
    This avoids recursion depth issues for the final summation step of large lists.

    Args:
        integers (list[int]): A list of integers to sum.

    Returns:
        int: The sum of the integers.
    """
    total_sum = 0
    for number in integers:
        total_sum = total_sum + number
    return total_sum


def _validate_and_convert_list_to_integers(lst):
    """
    Validates a list and converts it into a tuple of integers (for immutability and speed)
    if it is purely integer elements. If it contains nested lists, it recurses.
    However, for the top-level sum, we expect a flat list of ints based on helper usage.

    Actually, the problem is recursive. The helper above is for the base case of summing a flat list.
    The main logic will handle the recursion of lists within lists.

    This function is a placeholder to ensure we have a robust validation step before summation.
    """
    _validate_input_element(lst, "root list")


def _recursive_sum_list(current_list, current_path_index=0):
    """
    Recursively calculates the sum of a list which may contain nested lists.

    Strategy:
    1. Validate the input structure.
    2. Initialize a total sum variable.
    3. Iterate through each element in the list.
    4. Check the type of the element:
       - If it is an integer, add it to the total.
       - If it is a list, recursively call this function to get its sum and add that result to the total.
    5. Return the accumulated total.

    Args:
        current_list (list): The list to process.
        current_path_index (int): Internal counter for error messages.

    Returns:
        int: The total sum of all integers found in the structure.
    """
    # Validate the entire list structure first
    _validate_input_element(current_list, f"root")

    total_sum = 0

    # Iterate explicitly over each item
    for index, item in enumerate(current_list):
        # Define the specific context for this item's index in the error message
        item_context = f"index {index}"

        if isinstance(item, int):
            # Base case: the item is an integer
            total_sum = total_sum + item
        elif isinstance(item, list):
            # Recursive case: the item is a list, so we sum it internally
            nested_sum = _recursive_sum_list(item)
            total_sum = total_sum + nested_sum
        else:
            # This case should theoretically be caught by _validate_input_element,
            # but we add a safety check here for explicit error handling.
            raise ValueError(f"Unexpected type at {item_context}: {type(item).__name__}. "
                           f"Only integers and lists of integers are allowed.")

    return total_sum


def recursive_list_sum(input_list):
    """
    Main function to compute the sum of a list containing integers and sub-lists.
    Handles arbitrary levels of nesting.

    Input:
        input_list (list): A list containing integers and/or nested lists of integers.

    Output:
        int: The sum of all integer values in the structure.

    Raises:
        ValueError: If the input is not a list, contains non-integer/non-list items,
                    or is empty in a way that violates constraints (though empty lists sum to 0).
    """
    # Check for basic type validity immediately
    if not isinstance(input_list, list):
        raise ValueError(f"Input must be a list, but got {type(input_list).__name__}: {input_list}")

    # Call the recursive helper to perform the computation
    result = _recursive_sum_list(input_list)

    return result