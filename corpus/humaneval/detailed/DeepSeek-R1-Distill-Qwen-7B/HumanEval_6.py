from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # Split the input string into groups
    groups = paren_string.split(' ') if paren_string else []

    result = []
    for group in groups:
        if not group:
            result.append(0)
            continue

        max_depth = 0
        current_depth = 0
        valid = True

        # Iterate through each character in the group
        for char in group:
            if char == '(':
                current_depth += 1
                if current_depth > max_depth:
                    max_depth = current_depth
            elif char == ')':
                current_depth -= 1
            else:
                valid = False
                break

        if valid and max_depth > 0:
            result.append(max_depth)
        else:
            result.append(0)

    return result