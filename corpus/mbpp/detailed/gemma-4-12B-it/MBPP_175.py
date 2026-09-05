from typing import List, Dict

def is_valid_parenthese(s: str) -> bool:
    """
    Verifies the validity of a string containing parentheses, brackets, and braces.

    A string is valid if:
    1. Open brackets are closed by the same type of brackets.
    2. Open brackets are closed in the correct order.
    3. Every closing bracket has a corresponding opening bracket of the same type.

    Args:
        s (str): The string to be validated.

    Returns:
        bool: True if the string is valid, False otherwise.

    Raises:
        TypeError: If the input is not a string.
    """
    # Input Validation
    if not isinstance(s, str):
        raise TypeError(f"Expected input of type str, but received {type(s).__name__}")

    # Edge Case: Empty string is considered valid in most formal definitions
    # (nothing is unbalanced).
    if s == "":
        return True

    # Mapping of closing brackets to their corresponding opening brackets
    # This allows for O(1) lookup and easy extensibility.
    bracket_map: Dict[str, str] = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    # Set of characters that are considered opening brackets
    opening_brackets_set: set = set(bracket_map.values())

    # Set of characters that are considered closing brackets
    closing_brackets_set: set = set(bracket_map.keys())

    # The stack will store the opening brackets as we encounter them.
    # Using a list as a stack (LIFO).
    stack: List[str] = []

    # Iterate through every character in the input string
    for char in s:
        # Case 1: Character is an opening bracket
        if char in opening_brackets_set:
            stack.append(char)

        # Case 2: Character is a closing bracket
        elif char in closing_brackets_set:
            # If the stack is empty, there is a closing bracket without 
            # a preceding opening bracket (e.g., "())" or ")]").
            if not stack:
                return False

            # Pop the last opening bracket from the stack
            last_opening_bracket = stack.pop()

            # Check if the popped bracket matches the current closing bracket
            expected_opening = bracket_map[char]
            if last_opening_bracket != expected_opening:
                # Mismatch found (e.g., "(]" or "{)")
                return False

        # Case 3: Character is not a bracket (optional handling)
        # The problem context implies strings of brackets, but we ignore
        # other characters to stay robust.
        else:
            continue

    # After processing the entire string, the stack must be empty.
    # If it is not empty, there was an opening bracket that was never closed.
    if len(stack) == 0:
        return True
    else:
        return False

# The following assertions ensure the requirements are met.
if __name__ == "__main__":
    assert is_valid_parenthese("(){}[]") == True
    assert is_valid_parenthese("()[{)}") == False
    assert is_valid_parenthese("()") == True

    # Additional edge case tests
    assert is_valid_parenthese("") == True           # Empty string
    assert is_valid_parenthese("(") == False          # Single opening
    assert is_valid_parenthese(")") == False          # Single closing
    assert is_valid_parenthese("((()))") == True      # Nested
    assert is_valid_parenthese("()[]{}") == True      # Sequential
    assert is_valid_parenthese("(([" == False         # Incomplete