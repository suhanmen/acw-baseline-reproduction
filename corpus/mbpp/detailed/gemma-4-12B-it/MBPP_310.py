from typing import Tuple

def string_to_tuple(input_string: str) -> Tuple[str, ...]:
    """
    Converts a given string into a tuple of its characters.

    As per the provided assertions, space characters are omitted from the result.
    """
    # Check if the input is valid (not None and is a string)
    if input_string is None:
        raise ValueError("The input string cannot be None.")

    if not isinstance(input_string, str):
        raise TypeError(f"Input must be of type 'str', not {type(input_string).__name__}.")

    # Initialize an empty list to store characters
    # We use a list because it is mutable, allowing us to build the sequence.
    character_list = []

    # Iterate through the input string character by character
    for character in input_string:
        # Based on the specific requirement: 
        # string_to_tuple("python 3.0") == ('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0')
        # The space character is intentionally skipped.
        if character == " ":
            continue

        # Append the character to our temporary list
        character_list.append(character)

    # Convert the list of characters to a tuple
    # Tuples are the required return type for the function.
    result_tuple = tuple(character_list)

    return result_tuple