from typing import List
from collections import deque

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Remove all spaces from the string
    cleaned = paren_string.replace(' ', '')

    result = []
    stack = []
    current = []

    for char in cleaned:
        if char == '(':
            stack.append(char)
            current.append(char)
        elif char == ')':
            if stack:
                stack.pop()
                current.append(char)
            else:
                # This should not happen as per problem constraints
                current.append(char)

        # When we have a closing bracket after an opening, we can form a group
        if stack and stack[-1] == '(' and current and current[-1] == ')':
            result.append(''.join(current))
            current = []

    # After processing all characters, if there's remaining current, append it
    if current:
        result.append(''.join(current))

    return result