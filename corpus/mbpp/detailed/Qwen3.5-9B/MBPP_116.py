from typing import Tuple, Union

def validate_tuple_of_positive_integers(data: object) -> Tuple[bool, str, Union[Tuple[int, ...], None]]:
    """
    Validates that the input is a tuple containing only positive integers.

    Returns a tuple: (is_valid, error_message, cleaned_data_or_original).
    - If valid: (True, "", original_tuple)
    - If invalid: (False, "description of error", None)
    """

    # Check if the input is exactly a tuple
    if not isinstance(data, tuple):
        return False, f"Input must be a tuple, but received type: {type(data).__name__}", None

    # Check if the tuple is empty
    if len(data) == 0:
        return False, "Input tuple cannot be empty", None

    # Iterate through each element to check its type and value
    for index, element in enumerate(data):
        # Check if element is an integer (excluding booleans which are technically int subclass in Python)
        if type(element) is not int:
            return False, f"Element at index {index} is not an integer, it is {type(element).__name__}", None

        # Check for boolean explicitly (booleans are ints in Python but not positive integers in this context)
        if isinstance(element, bool):
            return False, f"Element at index {index} is a boolean (not allowed), found value: {element}", None

        # Check if the integer is positive (greater than 0)
        if element <= 0:
            return False, f"Element at index {index} is not a positive integer, found value: {element}", None

    # If we reach here, all validations passed
    return True, "", data


def convert_tuple_to_string_representation(valid_tuple: Tuple[int, ...]) -> str:
    """
    Converts a validated tuple of integers into a single concatenated string representation.
    Does not perform validation here as it is assumed to be handled by the caller.
    """
    result_chars = []

    for number in valid_tuple:
        result_chars.append(str(number))

    return "".join(result_chars)


def convert_tuple_to_int_tuple_to_int(input_data: object) -> Union[int, str]:
    """
    Main function to convert a tuple of positive integers into a single integer.

    Returns the integer if successful, or an error message string if validation fails.
    """

    # Step 1: Validate the input
    is_valid, error_message, validated_data = validate_tuple_of_positive_integers(input_data)

    if not is_valid:
        return f"Validation Error: {error_message}"

    # Step 2: Convert the validated tuple of integers into a string representation
    # We assume validated_data is safe at this point due to previous check
    intermediate_string = convert_tuple_to_string_representation(validated_data)

    # Step 3: Convert the resulting string into a final integer
    final_integer = int(intermediate_string)

    return final_integer