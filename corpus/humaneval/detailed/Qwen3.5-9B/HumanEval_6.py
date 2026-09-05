from typing import List
import re


def _calculate_max_nesting_level(group: str) -> int:
    """
    Calculates the maximum depth of nesting for a single group of parentheses.

    Args:
        group: A string containing only valid parentheses (e.g., '(()())').

    Returns:
        The integer representing the maximum nesting level.

    Raises:
        ValueError: If the string contains invalid characters or is malformed.
    """
    current_level = 0
    max_level = 0

    # Iterate through each character in the string explicitly
    for char in group:
        if char == '(':
            current_level += 1
            # Update max_level immediately when we find a deeper level
            if current_level > max_level:
                max_level = current_level
        elif char == ')':
            current_level -= 1
            # Defensive check: current_level should never be negative
            # in a valid sequence. If it is, the sequence is invalid.
            if current_level < 0:
                raise ValueError(f"Invalid parenthesis sequence: unbalanced closing parenthesis encountered.")
        else:
            # Any character that is not '(' or ')' is considered invalid for this problem context
            raise ValueError(f"Invalid character encountered in group: '{char}'. Expected only parentheses.")

    # Final validation: current_level must return to zero
    if current_level != 0:
        raise ValueError(f"Invalid parenthesis sequence: unbalanced parentheses in group.")

    return max_level


def _parse_and_validate_group(group_str: str) -> int:
    """
    Parses a single group string and returns its max nesting level.
    This function wraps the calculation and handles the empty string case explicitly.

    Args:
        group_str: The string representing one group of parentheses.

    Returns:
        The maximum nesting level as an integer.
    """
    # Handle empty string explicitly as an edge case
    if group_str == "":
        return 0

    return _calculate_max_nesting_level(group_str)


def parse_nested_parens(paren_string: str) -> List[int]:
    """ 
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    result: List[int] = []

    # Check for the empty input string case immediately
    if not paren_string:
        return result

    # Split the input string by whitespace to separate the groups.
    # This handles multiple spaces between groups automatically.
    raw_groups = paren_string.split()

    # Iterate over each raw group extracted from the split
    for group_index, group in enumerate(raw_groups):
        # Defensive check: Ensure the group is not empty after split (shouldn't happen with split(), but good for safety)
        if len(group) == 0:
            continue

        try:
            # Calculate the max nesting level for the current valid group
            depth = _parse_and_validate_group(group)
            result.append(depth)
        except ValueError as e:
            # Re-raise with context about which group failed
            raise ValueError(f"Error in group at index {group_index}: {str(e)}") from e

    return result