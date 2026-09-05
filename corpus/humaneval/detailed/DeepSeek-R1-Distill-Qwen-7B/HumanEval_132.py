def is_nested(string):
    """
    Create a function that takes a string as input which contains only square brackets.
    The function should return True if and only if there is a valid subsequence of brackets 
    where at least one bracket in the subsequence is nested.

    Args:
        string (str): The input string containing only square brackets.

    Returns:
        bool: True if a nested valid subsequence exists, False otherwise.
    """
    # Check if the string is empty
    if len(string) == 0:
        return False

    # Check if the string has any characters other than '[' or ']'
    if any(c not in ('[', ']') for c in string):
        return False

    # If the string has an odd number of brackets, it's impossible to have a valid pair
    if len(string) % 2 != 0:
        return False

    stack = []

    for char in string:
        if char == '(':
            stack.append(char)
        else:
            if not stack:
                return False  # closing bracket without corresponding opening
            last_opening = stack[-1]
            if last_opening != '(':
                return False  # mismatched brackets

    # If we have exactly 0 pairs, then no nested subsequence exists
    return len(stack) < 2