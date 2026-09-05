def check(binary_string: str) -> str:
    """
    Determines whether a given string is a valid binary string.
    A valid binary string is defined as a string that contains only 
    the characters '0' and '1'.

    Args:
        binary_string (str): The input string to evaluate.

    Returns:
        str: "Yes" if the string is binary, "No" otherwise.
    """

    # Step 1: Validate that the input is indeed a string.
    # While the type hint suggests str, production code should guard against other types.
    if not isinstance(binary_string, str):
        return "No"

    # Step 2: Handle the edge case of an empty string.
    # Depending on the definition, an empty string might be considered binary 
    # (containing no non-binary chars) or not. In most context-free 
    # grammar contexts, a binary string must have at least one digit.
    # However, looking at standard "is binary" logic, we check for content.
    if len(binary_string) == 0:
        # If an empty string should be "No", we return "No". 
        # Given the assertions, "101" is Yes. We will treat empty as "No"
        # because a string with no characters doesn't represent a binary number.
        return "No"

    # Step 3: Define the set of allowed characters.
    allowed_chars = {'0', '1'}

    # Step 4: Iterate through every character in the input string.
    # We do this explicitly to ensure each step of the logic is visible.
    is_binary = True

    for character in binary_string:
        # Check if the current character is in the allowed set.
        if character not in allowed_chars:
            # If any character is found that is not '0' or '1', 
            # the string is not binary.
            is_binary = False
            # We can break early as soon as we find a non-binary character.
            break

    # Step 5: Return the final result based on the flag.
    if is_binary:
        return "Yes"
    else:
        return "No"

# The following assertions are included for completeness to ensure the 
# function behaves as required by the problem description.
if __name__ == "__main__":
    assert check("01010101010") == "Yes"
    assert check("name0") == "No"
    assert check("101") == "Yes"
    assert check("") == "No"
    assert check("2") == "No"
    assert check("000") == "Yes"
    assert check("111") == "Yes"
    assert check(" ") == "No"