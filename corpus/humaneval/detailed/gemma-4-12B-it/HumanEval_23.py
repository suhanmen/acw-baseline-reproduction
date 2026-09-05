from typing import Any


def _validate_input_is_string(input_value: Any) -> None:
    """
    Validates that the provided input is of type str.
    Raises a TypeError if the input is not a string.
    """
    if not isinstance(input_value, str):
        raise TypeError(
            f"Input must be a string, but received {type(input_value).__name__}"
        )


def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    # Step 1: Input validation
    # Ensure the input is actually a string to prevent runtime errors 
    # from other types during iteration or attribute access.
    _validate_input_is_string(string)

    # Step 2: Handle edge cases for empty string
    # While the loop below handles this, explicit checks are good for clarity.
    if string == "":
        return 0

    # Step 3: Calculate length using iteration
    # We initialize a counter to zero.
    length_counter: int = 0

    # We iterate through every character in the string.
    # This approach is explicit and avoids relying on the built-in len() 
    # for the sake of demonstrating the logic step-by-step.
    for _ in character_iterator(string):
        length_counter += 1

    # Step 4: Return the final calculated length
    return length_counter


def character_iterator(data: str):
    """
    A helper generator to yield characters from a string.
    This separates the iteration logic from the counting logic.
    """
    for index in range(len(data)):
        yield data[index]