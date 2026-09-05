import re
from typing import List, Tuple, Optional


def is_balanced(s: str) -> bool:
    """
    Determines if a string of parentheses is balanced.

    Args:
        s (str): The string to check. Must contain only '(' and ')' characters.

    Returns:
        bool: True if the string is balanced, False otherwise.

    Raises:
        ValueError: If the input string contains characters other than '(' or ')'.
    """
    balance_counter = 0
    for i, char in enumerate(s):
        if char == '(':
            balance_counter += 1
        elif char == ')':
            balance_counter -= 1
        else:
            # Input validation: only parentheses are allowed
            raise ValueError(f"Invalid character found at index {i}: {char!r}. Only '(' and ')' are allowed.")

        # If balance drops below zero at any point, it's unbalanced
        if balance_counter < 0:
            return False

    # A balanced string must have a net balance of zero
    return balance_counter == 0


def validate_input(lst: List[str]) -> Tuple[str, str]:
    """
    Validates the input list and its contents.

    Args:
        lst (List[str]): The list of strings to validate.

    Returns:
        Tuple[str, str]: A tuple containing (string0, string1) if valid.

    Raises:
        ValueError: If the list length is not 2, or elements are not strings, 
                    or elements are empty or contain invalid characters.
    """
    # Check if the list has exactly two elements
    if not isinstance(lst, list):
        raise TypeError("Input must be a list.")

    if len(lst) != 2:
        raise ValueError(f"Input list must contain exactly two strings, found {len(lst)}.")

    s1, s2 = lst[0], lst[1]

    # Check if elements are strings
    if not isinstance(s1, str) or not isinstance(s2, str):
        raise ValueError("Both elements must be strings.")

    # Check for empty strings (though problem implies non-empty, handling for robustness)
    if len(s1) == 0:
        raise ValueError("First string cannot be empty.")
    if len(s2) == 0:
        raise ValueError("Second string cannot be empty.")

    # Validate characters in s1
    if not re.match(r'^[\(\)]+$', s1):
        raise ValueError(f"First string contains invalid characters: {s1!r}")

    # Validate characters in s2
    if not re.match(r'^[\(\)]+$', s2):
        raise ValueError(f"Second string contains invalid characters: {s2!r}")

    return s1, s2


def concatenate_and_check(a: str, b: str) -> bool:
    """
    Concatenates string a and b, then checks if the result is balanced.

    Args:
        a (str): First string.
        b (str): Second string.

    Returns:
        bool: True if concatenated string is balanced, False otherwise.
    """
    combined = a + b
    return is_balanced(combined)


def match_parens(lst: List[str]) -> str:
    """
    Checks if two strings of parentheses can be concatenated (in any order)
    to form a balanced string.

    Args:
        lst (List[str]): A list of exactly two strings containing only '(' or ')'.

    Returns:
        str: 'Yes' if a balanced combination exists, 'No' otherwise.

    Raises:
        TypeError: If input is not a list.
        ValueError: If input list doesn't have exactly two elements, elements aren't 
                     strings, are empty, or contain invalid characters.
    """
    # Step 1: Validate the input structure and contents
    if lst is None:
        raise TypeError("Input cannot be None.")

    s1, s2 = validate_input(lst)

    # Step 2: Check first permutation (s1 followed by s2)
    result_1 = concatenate_and_check(s1, s2)

    # Step 3: Check second permutation (s2 followed by s1)
    result_2 = concatenate_and_check(s2, s1)

    # Step 4: Determine final result
    if result_1 or result_2:
        return 'Yes'
    else:
        return 'No'