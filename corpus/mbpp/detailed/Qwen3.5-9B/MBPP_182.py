import re
from typing import Tuple, List, Union

def _validate_string_input(input_value: Union[str, None]) -> str:
    """
    Validates that the input is a string.
    Raises a TypeError if the input is None or not a string.

    :param input_value: The input to validate.
    :return: The validated input string.
    :raises TypeError: If input is not a string.
    :raises ValueError: If input is None.
    """
    if input_value is None:
        raise ValueError("Input cannot be None.")

    if not isinstance(input_value, str):
        raise TypeError(f"Input must be a string, got {type(input_value).__name__} instead.")

    return input_value

def _extract_uppercase_characters(text: str) -> List[str]:
    """
    Extracts all uppercase alphabetic characters from the given text.

    :param text: The input string to scan.
    :return: A list of uppercase characters found.
    """
    pattern = re.compile(r'[A-Z]', re.UNICODE)
    matches = pattern.findall(text)
    return matches

def _extract_lowercase_characters(text: str) -> List[str]:
    """
    Extracts all lowercase alphabetic characters from the given text.

    :param text: The input string to scan.
    :return: A list of lowercase characters found.
    """
    pattern = re.compile(r'[a-z]', re.UNICODE)
    matches = pattern.findall(text)
    return matches

def _extract_numeric_characters(text: str) -> List[str]:
    """
    Extracts all numeric digits from the given text.

    :param text: The input string to scan.
    :return: A list of digit characters found.
    """
    pattern = re.compile(r'\d', re.UNICODE)
    matches = pattern.findall(text)
    return matches

def _extract_special_characters(text: str) -> List[str]:
    """
    Extracts all non-alphanumeric characters (special characters) from the given text.

    This uses a negative lookahead/lookbehind conceptually by matching 
    anything that is NOT a letter (a-z, A-Z) and NOT a digit (0-9).

    :param text: The input string to scan.
    :return: A list of special characters found.
    """
    # Pattern explanation:
    # [^a-zA-Z0-9] matches any character that is not in the set of uppercase letters,
    # lowercase letters, or digits.
    # \w matches alphanumeric + underscore, so we must be careful. 
    # The regex [^a-zA-Z0-9] specifically excludes underscores if they appear, 
    # treating them as special characters based on strict alphanumeric definition.
    # If the requirement implies standard 'special' (symbols) but allows underscore as word char,
    # one might adjust. However, based on standard "character class" subtraction:
    # Letters: a-z A-Z
    # Numbers: 0-9
    # Everything else (including space, underscore, punctuation) is returned here.
    pattern = re.compile(r'[^a-zA-Z0-9]', re.UNICODE)
    matches = pattern.findall(text)
    return matches

def find_character(input_text: Union[str, None]) -> Tuple[List[str], List[str], List[str], List[str]]:
    """
    Analyzes an input string to categorize characters into uppercase, lowercase,
    numeric, and special character lists.

    The function uses regular expressions to identify character types.
    It returns a tuple containing four lists in the following order:
    (uppercase_chars, lowercase_chars, numeric_chars, special_chars)

    :param input_text: The string to analyze. Can be None to trigger validation error.
    :return: A tuple of four lists:
             [uppercase_list, lowercase_list, numeric_list, special_list]
    :raises TypeError: If input is not a string.
    :raises ValueError: If input is None.
    """

    # Step 1: Validate the input explicitly
    validated_string = _validate_string_input(input_text)

    # Step 2: Prepare empty lists to hold results
    uppercase_list: List[str] = []
    lowercase_list: List[str] = []
    numeric_list: List[str] = []
    special_list: List[str] = []

    # Step 3: Extract uppercase characters
    uppercase_chars = _extract_uppercase_characters(validated_string)
    uppercase_list = uppercase_chars

    # Step 4: Extract lowercase characters
    lowercase_chars = _extract_lowercase_characters(validated_string)
    lowercase_list = lowercase_chars

    # Step 5: Extract numeric characters
    numeric_chars = _extract_numeric_characters(validated_string)
    numeric_list = numeric_chars

    # Step 6: Extract special characters
    special_chars = _extract_special_characters(validated_string)
    special_list = special_chars

    # Step 7: Return the results as a tuple of lists
    return (uppercase_list, lowercase_list, numeric_list, special_list)