from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    if not paren_string or not paren_string.strip():
        return []

    # Split the input string into individual groups by whitespace.
    # We use split() without arguments to handle multiple spaces or tabs.
    raw_groups: List[str] = paren_string.split()

    results: List[int] = []

    for group in raw_groups:
        # Calculate the depth for each specific group.
        max_depth = _calculate_max_nesting(group)
        results.append(max_depth)

    return results


def _calculate_max_nesting(paren_group: str) -> int:
    """
    Calculates the maximum depth of nested parentheses for a single string.
    Validates that parentheses are balanced and correctly closed.

    Returns:
        int: The maximum nesting depth encountered.

    Raises:
        ValueError: If parentheses are unbalanced or contain invalid characters.
    """
    current_depth: int = 0
    max_depth_reached: int = 0

    # Track the balance to ensure every open paren is closed correctly.
    # If balance < 0 at any point, a closing paren appeared without an opener.
    balance: int = 0

    for char in paren_group:
        if char == '(':
            balance += 1
            current_depth += 1

            # Update the peak depth encountered so far.
            if current_depth > max_depth_reached:
                max_depth_reached = current_depth

        elif char == ')':
            balance -= 1
            current_depth -= 1

            # If balance drops below zero, we have a ')' without a preceding '('.
            if balance < 0:
                raise ValueError(f"Invalid parenthesis group: '{paren_group}'. "
                                 f"Closing parenthesis found without opening one.")

        else:
            # Depending on requirements, non-paren characters could be ignored
            # or raise an error. Here we ignore them to be robust.
            continue

    # If balance is not zero, there are unclosed opening parentheses.
    if balance != 0:
        raise ValueError(f"Invalid parenthesis group: '{paren_group}'. "
                         f"Parentheses are not balanced.")

    return max_depth_reached