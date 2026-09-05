from typing import Any


def correct_bracketing(brackets: str) -> bool:
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("<")
    False
    >>> correct_bracketing("<>")
    True
    >>> correct_bracketing("<<><>>")
    True
    >>> correct_bracketing("><<>")
    False
    """
    # Validate that the input is actually a string.
    if not isinstance(brackets, str):
        raise TypeError(f"Input must be a string, not {type(brackets).__name__}")

    # An empty string is technically balanced as there are no unmatched brackets.
    if not brackets:
        return True

    # Use a counter to track the depth of open brackets.
    # A positive number means we have open brackets waiting to be closed.
    # A zero means all brackets are currently balanced.
    # A negative number means a closing bracket appeared without an opening one.
    current_depth: int = 0

    for index, char in enumerate(brackets):
        # Validate that the string only contains the allowed characters.
        if char == "<":
            # Increment depth for every opening bracket.
            current_depth += 1
        elif char == ">":
            # Decrement depth for every closing bracket.
            current_depth -= 1
        else:
            # If the string contains characters other than < or >, 
            # we treat the input as invalid or ignore it based on requirements.
            # Given the prompt, we treat non-bracket characters as invalid types.
            raise ValueError(f"Invalid character '{char}' found at index {index}. "
                             "Only '<' and '>' are allowed.")

        # Optimization/Check: If depth goes negative, it means a '>' 
        # appeared before a matching '<' (e.g., "><").
        if current_depth < 0:
            return False

    # After processing the entire string, the depth must be exactly 0.
    # If depth > 0, there are unclosed "<" brackets.
    is_balanced: bool = (current_depth == 0)

    return is_balanced