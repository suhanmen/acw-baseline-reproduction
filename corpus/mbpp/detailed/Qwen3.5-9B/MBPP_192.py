def check_string_has_letter_and_number(input_string: str) -> bool:
    """
    Determines if the input string contains at least one alphabetic character
    and at least one numeric digit.

    This function performs the following steps:
    1. Validates that the input is a string instance.
    2. Handles the edge case where the string is empty.
    3. Iterates through each character in the string.
    4. Tracks separately whether an alphabetic letter has been found.
    5. Tracks separately whether a numeric digit has been found.
    6. Returns True only if both conditions (letter found AND digit found) are met.

    :param input_string: The string to be checked.
    :return: True if the string has at least one letter and one number, False otherwise.
    """
    # Step 1: Validate input type explicitly
    if not isinstance(input_string, str):
        return False

    # Step 2: Handle the empty input edge case
    # An empty string cannot contain a letter or a number.
    if len(input_string) == 0:
        return False

    has_letter = False
    has_number = False

    # Step 3: Iterate through each character in the string
    # Using explicit iteration for clarity rather than list comprehensions or one-liners.
    for character in input_string:
        # Step 4: Check if the current character is an alphabetic letter
        if character.isalpha():
            has_letter = True

        # Check if the current character is a numeric digit
        if character.isdigit():
            has_number = True

        # Optional Optimization: If both flags are True, we can stop early
        # However, to maintain explicit logic flow and handle edge cases uniformly,
        # we could continue, but breaking here is safe and efficient.
        # Given the requirement for explicit steps, we will allow the loop to finish
        # or break only if we are certain about the result. 
        # For maximum clarity and robustness against any weird character ordering,
        # we will let the loop finish or break only when both are found.
        if has_letter and has_number:
            # We have satisfied both conditions. We can safely return True.
            # This avoids unnecessary iteration over remaining characters.
            break

    # Step 5 & 6: Return the result based on the two accumulated flags
    if has_letter and has_number:
        return True
    else:
        return False