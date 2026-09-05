from typing import List, Tuple, Any

def _validate_input(s: Any) -> str:
    """
    Validates that the input is a string.
    Raises a TypeError if the input is not a string.

    Args:
        s: The input to validate.

    Returns:
        The validated string.

    Raises:
        TypeError: If the input is not a string.
    """
    if not isinstance(s, str):
        raise TypeError(f"Expected a string, but got {type(s).__name__}")
    return s


def _check_minimum_length(s: str) -> bool:
    """
    Checks if the string length is at least 3.

    Args:
        s: The string to check.

    Returns:
        True if length is >= 3, False otherwise.
    """
    return len(s) >= 3


def _find_repeated_triplets(s: str) -> List[Tuple[int, str, str, str]]:
    """
    Identifies all positions where three consecutive characters are not distinct.

    Args:
        s: The string to analyze.

    Returns:
        A list of tuples containing the start index and the three characters
        if any triplet is not distinct. Empty list if all triplets are distinct.
    """
    issues: List[Tuple[int, str, str, str]] = []

    if len(s) < 3:
        return issues

    # Iterate through the string up to the point where a full triplet can be formed
    # Range ends at len(s) - 2 because we need indices i, i+1, i+2
    for i in range(len(s) - 2):
        char_first: str = s[i]
        char_second: str = s[i + 1]
        char_third: str = s[i + 2]

        # Check if the current triplet has any repeating characters
        # A triplet is invalid if char_first == char_second OR 
        # char_first == char_third OR char_second == char_third
        is_invalid_triplet = (
            char_first == char_second or 
            char_first == char_third or 
            char_second == char_third
        )

        if is_invalid_triplet:
            issues.append((i, char_first, char_second, char_third))

    return issues


def is_happy(s: Any) -> bool:
    """
    Checks if a string is "happy".

    A string is considered happy if:
    1. Its length is at least 3.
    2. Every sequence of 3 consecutive characters consists of distinct characters.

    Args:
        s: The input string to evaluate.

    Returns:
        True if the string is happy, False otherwise.

    Raises:
        TypeError: If the input is not a string.
    """
    # Step 1: Validate input type
    validated_s: str = _validate_input(s)

    # Step 2: Check minimum length requirement
    meets_length_requirement: bool = _check_minimum_length(validated_s)

    if not meets_length_requirement:
        return False

    # Step 3: Check for repeated triplets
    invalid_triplets: List[Tuple[int, str, str, str]] = _find_repeated_triplets(validated_s)

    # Step 4: Determine result based on findings
    # If the list of invalid triplets is empty, the string is happy
    is_happy_result: bool = len(invalid_triplets) == 0

    return is_happy_result