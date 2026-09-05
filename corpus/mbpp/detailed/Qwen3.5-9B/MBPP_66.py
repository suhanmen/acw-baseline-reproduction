from typing import List, Optional, Union

def validate_input_list(data: object) -> Optional[List[int]]:
    """
    Validates that the input is a list and that all elements are integers.

    Args:
        data: The input object to validate.

    Returns:
        The validated list of integers if successful, None if validation fails.
    """
    if not isinstance(data, list):
        return None

    for index, element in enumerate(data):
        if not isinstance(element, int) or isinstance(element, bool):
            # Explicitly exclude booleans as they are subclasses of int in Python
            return None

    return data

def is_positive_number(value: int) -> bool:
    """
    Checks if a single integer value is strictly greater than zero.

    Args:
        value: The integer to check.

    Returns:
        True if the value is positive (> 0), False otherwise.
    """
    return value > 0

def count_positive_numbers(input_list: List[int]) -> int:
    """
    Counts the number of strictly positive integers in a validated list.

    This function iterates through the provided list, checks each element
    to see if it is a positive number (greater than zero), and maintains
    a running count of such elements.

    Args:
        input_list: A list of integers to be analyzed.

    Returns:
        An integer representing the count of positive numbers in the list.
        Returns 0 if the list is empty.
    """
    positive_count = 0

    # Explicit iteration over the list with index and value
    for index, number in enumerate(input_list):
        # Apply the positivity check to the current number
        if is_positive_number(number):
            # Increment the counter for every positive number found
            positive_count += 1

    return positive_count

def pos_count(data: object) -> int:
    """
    Public interface to count positive numbers in a list.

    This function serves as the main entry point. It first validates the input
    to ensure it meets the strict requirements (a list of integers). If the
    input is invalid, it raises a ValueError with a descriptive message.

    Requirements:
    - Must accept a list of integers.
    - Must handle empty lists, single elements, all-equal elements, 
      boundary values (0, 1), negative numbers, and positive numbers.
    - Returns the count of numbers strictly greater than zero.

    Args:
        data: The input data expected to be a list of integers.

    Returns:
        The count of positive numbers.

    Raises:
        TypeError: If data is not a list.
        ValueError: If data contains non-integer elements or is None.
    """
    # Step 1: Validate the input structure and content
    validated_data = validate_input_list(data)

    if validated_data is None:
        # If validation fails at any point, raise a specific error
        if not isinstance(data, list):
            raise TypeError(f"Expected a list of integers, but received type: {type(data).__name__}")
        else:
            raise ValueError("Expected a list of integers, but the list contains non-integer elements.")

    # Step 2: Proceed with the counting logic using the validated data
    return count_positive_numbers(validated_data)