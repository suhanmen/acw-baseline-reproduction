from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    groups = paren_string.split()
    result = []
    current_depth = 0
    max_depth = 0

    for group in groups:
        depth = 0
        stack = []
        for char in group:
            if char == '(':
                stack.append(char)
                depth += 1
            elif char == ')':
                if stack:
                    stack.pop()
                    depth -= 1
            current_depth = max(current_depth, depth)
        result.append(current_depth)

    return result