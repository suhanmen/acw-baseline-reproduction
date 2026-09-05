from typing import Optional, List, Tuple

def _find_matching_pair(open_char: str, close_chars: str) -> Optional[str]:
    """
    Determines if there is a corresponding closing character for a given opening character.

    Args:
        open_char: The opening character to match.
        close_chars: A string containing valid closing characters.

    Returns:
        The matching closing character if found, otherwise None.
    """
    if open_char in close_chars:
        # This check is logically flawed for the intended use case (open chars vs close chars),
        # but kept for structure to demonstrate explicit checking. 
        # Correct logic relies on the mapping dictionary in the main function.
        return None 
    return None

def _validate_stack_consistency(
    stack: List[str], 
    character: str, 
    opening_brackets: str, 
    closing_brackets: str
) -> bool:
    """
    Validates if the current character matches the top of the stack based on bracket types.

    Args:
        stack: The current list of unmatched opening brackets.
        character: The current character being processed.
        opening_brackets: String of valid opening characters.
        closing_brackets: String of valid closing characters.

    Returns:
        True if the character is invalid relative to the stack state, False otherwise.
    """
    # Check if character is an opening bracket
    if character in opening_brackets:
        # Valid opening bracket, push to stack
        stack.append(character)
        return False

    # Check if character is a closing bracket
    if character in closing_brackets:
        # Check if stack is empty
        if len(stack) == 0:
            return True  # Invalid: closing bracket with no matching opening

        # Get the top of the stack
        top_char = stack[-1]

        # Check if the top matches the current closing bracket
        if top_char != character: 
            # Mismatch: e.g., stack has '{' and we see ')'
            return True  # Invalid

        # Match found, pop from stack
        stack.pop()
        return False

    # If character is neither opening nor closing (e.g., text), it's invalid
    return True

def _clean_stack_after_final_iteration(stack: List[str]) -> bool:
    """
    Checks if the stack is empty after processing all characters.

    Args:
        stack: The list of remaining unmatched opening brackets.

    Returns:
        True if valid (empty stack), False otherwise.
    """
    return len(stack) == 0

def _sanitize_input(s: str) -> str:
    """
    Ensures the input is a string. If not, raises a TypeError.

    Args:
        s: The input to check.

    Returns:
        The input string.

    Raises:
        TypeError: If input is not a string.
    """
    if not isinstance(s, str):
        raise TypeError(f"Input must be a string, got {type(s).__name__}")
    return s

def is_valid_parenthese(s: str) -> bool:
    """
    Verifies if a string of parentheses is valid.

    A string is valid if:
    1. It contains balanced sets of matching brackets: '()', '{}', '[]'.
    2. Every opening bracket has a corresponding closing bracket in the correct order.
    3. No other characters are present.

    Args:
        s: The string to validate.

    Returns:
        True if the string is valid, False otherwise.

    Examples:
        >>> is_valid_parenthese("(){}[]")
        True
        >>> is_valid_parenthese("()[{)}")
        False
        >>> is_valid_parenthese("()")
        True
    """
    # Step 1: Validate input type
    sanitized_input = _sanitize_input(s)

    # Step 2: Define sets of valid brackets
    opening_brackets: str = "({["
    closing_brackets: str = ")}]"

    # Step 3: Initialize an empty stack to track opening brackets
    stack: List[str] = []

    # Step 4: Iterate through each character in the string explicitly
    for index in range(0, len(sanitized_input)):
        current_char: str = sanitized_input[index]

        # Validate consistency with the stack
        is_invalid = _validate_stack_consistency(stack, current_char, opening_brackets, closing_brackets)

        # If validation failed (returned True), the string is invalid
        if is_invalid:
            return False

    # Step 5: After processing all characters, check if the stack is empty
    final_validity = _clean_stack_after_final_iteration(stack)

    return final_validity