import re

# Define the set of allowed characters: uppercase letters (a-z in the problem description context, 
# but standard practice distinguishes A-Z and a-z; the example "ABCDEF" implies uppercase too),
# lowercase letters, and digits. 
# The problem statement says "a-z, a-z and 0-9". This is slightly ambiguous as it lists 'a-z' twice.
# However, the test case "ABCDEF..." explicitly contains uppercase letters and passes.
# Therefore, the intended allowed set is: A-Z, a-z, 0-9.
ALLOWED_CHARACTER_PATTERN = r"^[A-Za-z0-9]+$"

def validate_input_type(input_string: str, error_message: str) -> str:
    """
    Validates that the provided input is a string.
    Raises a TypeError with a descriptive message if the input is not a string.

    :param input_string: The input to check.
    :param error_message: Base message for the error.
    :return: The validated string.
    :raises TypeError: If input is not a string.
    """
    if not isinstance(input_string, str):
        raise TypeError(f"{error_message}: Expected a string, got {type(input_string).__name__}.")
    return input_string

def is_all_empty(input_string: str) -> bool:
    """
    Checks if the input string is empty after stripping whitespace.
    Note: For strict character set validation, usually an empty string 
    is considered to contain only allowed characters (vacuously true) 
    unless specified otherwise. However, the regex ^[A-Za-z0-9]+$ requires at least one char.
    Let's stick to the regex behavior: empty string matches ^...$ but fails ^...+$ (the + means one or more).

    :param input_string: The string to check.
    :return: True if string is empty, False otherwise.
    """
    return len(input_string) == 0

def construct_regex_pattern() -> re.Pattern:
    """
    Constructs and compiles the regex pattern for allowed characters.

    Returns:
        A compiled regex pattern object.
    """
    # The pattern matches strings that:
    # 1. Start (^) and end ($) with nothing else.
    # 2. Contain one or more (+) characters from the set A-Z, a-z, 0-9.
    pattern_string = r"^[A-Za-z0-9]+$"
    return re.compile(pattern_string)

def check_string_allowed(input_string: str) -> bool:
    """
    Main logic to determine if the input string contains only allowed characters.

    Steps:
    1. Validate that input is a string.
    2. If the string is empty, the logic depends on the regex. 
       Our regex uses '+', so empty strings will return False.
    3. Use the compiled regex to check the entire string.

    :param input_string: The string to validate.
    :return: True if all characters are allowed, False otherwise.
    """
    validated_input = validate_input_type(input_string, "Input")

    # Check for empty string edge case explicitly to ensure clarity, 
    # though the regex handles it.
    if is_all_empty(validated_input):
        # An empty string does not contain any characters from the set A-Za-z0-9
        # strictly speaking under the '+' quantifier (one or more).
        return False

    pattern = construct_regex_pattern()

    # Perform the match. 
    # search() looks anywhere, match() checks the whole string from start to end.
    # We need to ensure the entire string consists only of allowed chars, so we use match().
    is_match = pattern.match(validated_input) is not None

    return is_match

def is_allowed_specific_char(input_data: object) -> bool:
    """
    Wrapper function that wraps the core logic and handles potential None inputs gracefully
    by treating them as invalid, raising a descriptive error, or returning False based on 
    the expectation of valid string input.

    Given the problem constraints "given string", we enforce strict type checking.
    However, to be defensive against common runtime errors (like None), we check for None 
    before the type check in validate_input_type, or let validate_input_type handle it.

    This function serves as the public interface matching the problem statement's assertions.

    :param input_data: The data to be checked.
    :return: Boolean indicating if the data contains only allowed characters.
    :raises TypeError: If input is not a string.
    """
    # Directly delegate to the robust checking function.
    # The validate_input_type will raise TypeError for None or non-string types.
    return check_string_allowed(input_data)