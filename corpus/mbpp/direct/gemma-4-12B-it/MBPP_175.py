def is_valid_parenthese(s: str) -> bool:
    """
    Verifies the validity of a string of parentheses.

    Args:
        s (str): A string containing characters '(', ')', '{', '}', '[', ']'.

    Returns:
        bool: True if the string is valid, False otherwise.
    """
    stack = []
    mapping = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for char in s:
        if char in mapping:
            # Pop the top element if stack is not empty, else use a dummy value
            top_element = stack.pop() if stack else '#'
            # If the popped element doesn't match the mapping, it's invalid
            if mapping[char] != top_element:
                return False
        else:
            # It's an opening bracket, push it onto the stack
            stack.append(char)

    # If the stack is empty, all brackets were matched correctly
    return not stack

if __name__ == "__main__":
    assert is_valid_parenthese("(){}[]") == True
    assert is_valid_parenthese("()[{)}") == False
    assert is_valid_parenthese("()") == True