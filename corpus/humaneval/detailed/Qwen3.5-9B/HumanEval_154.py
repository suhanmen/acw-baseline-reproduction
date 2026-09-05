# Explicit import not needed for this task, but we keep the wrapper structure clean.

def is_rotated_string(target: str, candidate: str) -> bool:
    """
    Checks if a 'candidate' string is a rotation of the 'target' string.

    A string 'candidate' is a rotation of 'target' if:
    1. They have the same length.
    2. 'candidate' appears as a substring within 'target' + 'target'.

    This logic relies on the fact that any rotation of a string S can be found
    as a substring in S concatenated with itself (S + S), excluding the trivial
    full match which is handled by the length check.

    Args:
        target (str): The string to check against (must contain the rotation).
        candidate (str): The string that might be a rotation.

    Returns:
        bool: True if candidate is a rotation of target, False otherwise.
    """
    # Helper to handle the length constraint immediately.
    if len(candidate) != len(target):
        return False

    # If the strings are empty, an empty string is trivially a rotation of an empty string.
    if len(candidate) == 0:
        return True

    # Create the concatenated string to allow checking all rotations.
    doubled_target = target + target

    # Search for the candidate within the doubled target.
    return candidate in doubled_target


def is_valid_string(text: str, description: str = "Input text") -> str:
    """
    Validates that the input is a string. Returns the cleaned string if valid.
    If invalid, raises a ValueError with a descriptive message.

    Args:
        text (any): The input to validate.
        description (str): Human-readable description for error messages.

    Returns:
        str: The validated input string.

    Raises:
        ValueError: If the input is not a string.
        TypeError: If the input is explicitly not a string type (though isinstance covers this).
    """
    if not isinstance(text, str):
        raise TypeError(f"Expected a string for {description}, but got {type(text).__name__}")

    return text


def contains_rotation_or_substring(main_text: str, pattern_text: str) -> bool:
    """
    Main logic helper.
    Returns True if the main_text contains the pattern_text OR any rotation of the pattern_text.

    Args:
        main_text (str): The larger string to search within.
        pattern_text (str): The string to check or rotate.

    Returns:
        bool: True if found directly or as a rotation, False otherwise.
    """
    # Direct check first
    if pattern_text in main_text:
        return True

    # Check all rotations
    # Generate a candidate rotation. The method is_rotated_string handles the logic internally,
    # but here we need to generate the specific rotations to check if any match.
    # However, the helper is_rotated_string checks if the pattern IS a rotation of main_text logic reversed?
    # No, the requirement is: "second word or any of its rotations is a substring in the first word".
    # So we need to generate rotations of 'pattern_text' and check if they are in 'main_text'.

    length = len(pattern_text)

    # Edge case: empty pattern text
    if length == 0:
        return True # An empty string is a substring of any string

    # Generate all unique rotations of pattern_text
    # There are 'length' possible rotations.
    rotations_generated = []
    for i in range(length):
        # Rotate pattern_text by i positions: take slice [i:] + slice [:i]
        current_rotation = pattern_text[i:] + pattern_text[:i]
        rotations_generated.append(current_rotation)

    # Check if any generated rotation exists in main_text
    for rotation in rotations_generated:
        if rotation in main_text:
            return True

    return False


def cycpattern_check(a: any, b: any) -> bool:
    """
    You are given 2 words. You need to return True if the second word or any of its 
    rotations is a substring in the first word.

    Args:
        a: The main word (string) to search within.
        b: The pattern word (string) to search for (directly or as a rotation).

    Returns:
        bool: True if found, False otherwise.

    Raises:
        TypeError: If either argument is not a string.
        ValueError: If the inputs are explicitly None (though isinstance covers None check usually,
                     we add explicit logic for clarity on degenerate cases).
    """
    # Validate inputs explicitly
    try:
        validated_a = is_valid_string(a, "argument 'a'")
        validated_b = is_valid_string(b, "argument 'b'")
    except TypeError as e:
        raise TypeError(str(e)) from e

    # Explicitly check for None if required by specific defensive coding standards,
    # though isinstance(str) returns False for None.
    if a is None or b is None:
        raise ValueError("Input arguments cannot be None.")

    # Handle degenerate case where the main string is empty
    if len(validated_a) == 0:
        # An empty main string can only contain an empty pattern.
        return len(validated_b) == 0

    # Handle degenerate case where the pattern is longer than the main string
    # (It cannot be a substring unless it's equal length and identical, which the loop handles,
    #  but logically a longer string cannot be a substring of a shorter one).
    if len(validated_b) > len(validated_a):
        return False

    # Delegate to the robust logic helper
    return contains_rotation_or_substring(validated_a, validated_b)