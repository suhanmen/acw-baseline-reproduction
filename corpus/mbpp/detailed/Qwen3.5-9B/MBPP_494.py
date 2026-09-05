def _validate_tuple(input_tuple, error_message="Input must be a tuple of integers"):
    """
    Validates that the input is a tuple and that every element within it
    is an integer representing a binary digit (0 or 1).

    Raises:
        TypeError: If the input is not a tuple.
        ValueError: If the tuple is empty, contains non-integer elements,
                    or contains elements other than 0 or 1.
    """
    # Check if the input is a tuple
    if not isinstance(input_tuple, tuple):
        raise TypeError(error_message)

    # Check for empty tuple
    if len(input_tuple) == 0:
        raise ValueError("The binary tuple cannot be empty.")

    # Iterate through each element to validate type and value
    for index, element in enumerate(input_tuple):
        # Validate that the element is an integer
        if not isinstance(element, int):
            raise TypeError(
                f"Element at index {index} is not an integer: {type(element).__name__}. "
                f"Expected integer."
            )

        # Validate that the integer is either 0 or 1
        if element not in (0, 1):
            raise ValueError(
                f"Element at index {index} has value {element}. "
                f"Binary digits must be 0 or 1."
            )


def _convert_binary_tuple_to_integer(binary_digits):
    """
    Converts a validated tuple of binary digits (0s and 1s) into its integer representation.

    The conversion is done using the standard positional notation:
    Sum of (digit * 2^position), where position increases from left to right starting at 0.
    Alternatively, iteratively: result = (result * 2) + digit.

    Args:
        binary_digits (tuple[int]): A tuple containing only 0s and 1s.

    Returns:
        int: The integer value represented by the binary tuple.
    """
    result = 0
    current_power_of_two = 1

    # Iterate backwards through the tuple to treat the last element as the least significant bit (2^0)
    # We start from the end of the tuple and move towards the beginning.
    for i in range(len(binary_digits) - 1, -1, -1):
        current_digit = binary_digits[i]
        result += current_digit * current_power_of_two
        current_power_of_two *= 2

    return result


def binary_to_integer(binary_tuple):
    """
    Converts a binary tuple to its corresponding integer value.
    Handles validation, edge cases, and performs the conversion.

    Args:
        binary_tuple (tuple[int]): A tuple where each element is an integer (0 or 1).

    Returns:
        int: The integer representation of the binary sequence.

    Raises:
        TypeError: If the input is not a tuple or contains non-integer elements.
        ValueError: If the tuple is empty or contains elements other than 0 or 1.
    """
    # Step 1: Validate the input structure and contents
    _validate_tuple(binary_tuple)

    # Step 2: Perform the conversion
    integer_value = _convert_binary_tuple_to_integer(binary_tuple)

    return integer_value