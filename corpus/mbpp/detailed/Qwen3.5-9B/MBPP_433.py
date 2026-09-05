from typing import List, Union


def check_greater(input_array: List[Union[int, float]], number_to_check: Union[int, float]) -> str:
    """
    Checks whether the entered number is strictly greater than all elements of the given array.

    The logic is as follows:
    1. If the array is empty, the condition is considered True (a number is greater than all zero elements).
    2. If the number_to_check is greater than or equal to any single element in the array, 
       the condition fails.
    3. If the number_to_check is strictly greater than every single element, the condition holds.

    Returns:
    - "Yes, the entered number is greater than those in the array" if the condition holds.
    - "No, entered number is less than those in the array" otherwise.

    Args:
        input_array: A list of numbers (integers or floats).
        number_to_check: The number to compare against the elements of the array.

    Raises:
        TypeError: If input_array is not a list or if any element in input_array is not a number,
                   or if number_to_check is not a number.
        ValueError: If input_array contains non-numeric values.

    Examples:
        >>> check_greater([1, 2, 3, 4, 5], 4)
        'No, entered number is less than those in the array'
        >>> check_greater([2, 3, 4, 5, 6], 8)
        'Yes, the entered number is greater than those in the array'
        >>> check_greater([9, 7, 4, 8, 6, 1], 11)
        'Yes, the entered number is greater than those in the array'
    """

    # Step 1: Validate the type of the input array
    if not isinstance(input_array, list):
        raise TypeError(f"Expected input_array to be a list, but got {type(input_array).__name__}.")

    # Step 2: Validate the type of the number to check
    if not isinstance(number_to_check, (int, float)):
        raise TypeError(f"Expected number_to_check to be a number (int or float), but got {type(number_to_check).__name__}.")

    # Step 3: Initialize the result flag
    # We assume the condition is True until we find evidence to the contrary.
    is_greater_than_all_elements = True

    # Step 4: Iterate through each element in the array
    for index, current_element in enumerate(input_array):
        # Step 5: Validate the type of the current element
        if not isinstance(current_element, (int, float)):
            raise TypeError(f"Element at index {index} is not a number, but {type(current_element).__name__}.")

        # Step 6: Compare the number_to_check with the current element
        # If number_to_check is less than OR EQUAL to the current element, the condition fails.
        if number_to_check <= current_element:
            is_greater_than_all_elements = False
            break  # No need to check further if we found a violation

    # Step 7: Construct the response based on the flag
    if is_greater_than_all_elements:
        return "Yes, the entered number is greater than those in the array"
    else:
        return "No, entered number is less than those in the array"