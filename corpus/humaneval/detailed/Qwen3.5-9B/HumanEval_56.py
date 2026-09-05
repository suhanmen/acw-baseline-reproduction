from typing import List, Optional, Set

def _is_valid_bracket_character(char: str) -> bool:
    """
    Checks if a character is either an opening '<' or a closing '>' bracket.

    This function serves as a strict validator to ensure only expected characters
    are processed, preventing silent failures or unexpected behavior on malformed input.

    Args:
        char (str): A single character string to validate.

    Returns:
        bool: True if the character is '<' or '>', False otherwise.
    """
    return char == '<' or char == '>'

def _get_expected_close(open_char: str) -> str:
    """
    Returns the corresponding closing character for a given opening bracket.

    Args:
        open_char (str): The opening bracket character ('<').

    Returns:
        str: The corresponding closing bracket character ('>').

    Raises:
        ValueError: If the provided open_char is not '<'.
    """
    if open_char != '<':
        raise ValueError(f"Unexpected opening character: {open_char!r}")
    return '>'

def _process_bracket_sequence(
    bracket_sequence: str,
    stack: List[str],
    expected_close_char: str
) -> List[str]:
    """
    Processes a sequence of brackets using a stack-based approach.

    It iterates through each character in the sequence:
    - If an opening bracket is found, it is pushed onto the stack.
    - If a closing bracket is found, it must match the top of the stack.
      If it does not match or the stack is empty, a mismatch is recorded.
    - Other characters trigger an error condition (handled by the caller).

    Args:
        bracket_sequence (str): The string of brackets to process.
        stack (List[str]): The current state of the stack (passed by reference).
        expected_close_char (str): The character representing a closing bracket.

    Returns:
        List[str]: A list of mismatch types found ('mismatch_close', 'unclosed_open', 
                   or 'extra_open'). Returns empty list if processing is successful.
    """
    errors: List[str] = []

    for i, char in enumerate(bracket_sequence):
        if char == '<':
            # Push opening bracket onto the stack
            stack.append(char)
        elif char == '>':
            # Attempt to close a bracket
            if not stack:
                # Stack is empty, but we encountered a closing bracket
                # This means there is an unmatched closing bracket at this position
                errors.append('mismatch_close')
                break
            else:
                # Check if the top of the stack matches the current closing bracket
                top_element = stack[-1]
                if top_element != '<':
                    # Should not happen if input only contains '<' and '>', 
                    # but included for defensive logic completeness
                    errors.append('mismatch_close')
                    break
                else:
                    # Correct match found, pop from stack
                    stack.pop()
        else:
            # Character is neither '<' nor '>'
            # This is an invalid input scenario for this specific validator
            errors.append(f'invalid_character_{char!r}')
            break

    if not errors:
        # Check if any opening brackets remain unclosed
        if stack:
            # There are items left in the stack, meaning opening brackets were never closed
            # We collect how many or just note the fact
            errors.append('unclosed_open')

    return errors

def correct_bracketing(brackets: str) -> bool:
    """
    Checks if a string of brackets has correct bracketing.

    Every opening bracket '<' must have a corresponding closing bracket '>' 
    that comes after it, and brackets must be properly nested.

    This function validates that the input string contains ONLY the characters 
    '<' and '>'. If any other character is present, it returns False.

    Args:
        brackets (str): A string containing '<' and '>' characters.

    Returns:
        bool: True if the bracketing is correct and no invalid characters are present,
              False otherwise.

    Examples:
        >>> correct_bracketing("<")
        False
        >>> correct_bracketing("<>")
        True
        >>> correct_bracketing("<<><>>")
        True
        >>> correct_bracketing("><<>")
        False
        >>> correct_bracketing("<<>")
        False
        >>> correct_bracketing("<<<<<>")
        False
        >>> correct_bracketing("")
        True
        >>> correct_bracketing("<<a>>")
        False
    """
    # Explicit validation: Check for None (though type hint suggests str, defensive coding)
    if brackets is None:
        return False

    # Handle empty string explicitly as per requirements
    if len(brackets) == 0:
        return True

    # Initialize a stack to keep track of opening brackets.
    # We use a list for the stack to allow push/pop operations.
    open_bracket_stack: List[str] = []

    # Flag to track if the sequence was successfully processed without errors
    is_valid_sequence: bool = True

    # Define the character that represents a closing bracket
    closing_bracket_char: str = '>'

    # Process each character in the input string
    for char_index, char in enumerate(brackets):
        # Step 1: Validate the current character
        if not _is_valid_bracket_character(char):
            is_valid_sequence = False
            # Log or handle the invalid character explicitly
            invalid_char = char
            # We do not need to check the rest of the string if invalid char is found
            # The function will return False
            break

        if char == '<':
            # Step 2: Handle opening bracket
            # Push the character onto the stack
            open_bracket_stack.append(char)
        elif char == '>':
            # Step 3: Handle closing bracket
            # Check if there is a corresponding opening bracket
            if len(open_bracket_stack) == 0:
                is_valid_sequence = False
                # No opening bracket to match this closing one
                break
            else:
                # Peek at the top of the stack
                top_element: str = open_bracket_stack[-1]

                # Check if the top element is the expected opening bracket
                if top_element != '<':
                    is_valid_sequence = False
                    # This case is technically impossible if only '<' and '>' are in input,
                    # but kept for logical completeness in helper functions context.
                    break
                else:
                    # Match found, remove the opening bracket from the stack
                    open_bracket_stack.pop()

    # After processing all characters:
    # 1. If we found an invalid character, return False immediately.
    if not is_valid_sequence:
        return False

    # 2. If there are remaining items in the stack, it means there are 
    #    opening brackets that were never closed.
    if len(open_bracket_stack) > 0:
        return False

    # If we reach here, the sequence is valid.
    return True