from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    paren_string = paren_string.replace(" ", "")
    result = []
    current_group = []
    depth = 0

    for char in paren_string:
        current_group.append(char)
        if char == '(':
            depth += 1
        elif char == ')':
            depth -= 1

        # When depth returns to 0, a complete top-level group is formed
        if depth == 0 and current_group:
            result.append("".join(current_group))
            current_group = []

    return result