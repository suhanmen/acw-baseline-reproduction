from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Validate input type
    if not isinstance(paren_string, str):
        raise TypeError("Input must be a string.")

    # Step 1: Clean the input string
    # We remove all whitespace characters as specified in the requirements.
    cleaned_string = "".join(char for char in paren_string if not char.isspace())

    # Handle empty input case
    if not cleaned_string:
        return []

    result_groups: List[str] = []
    current_group_chars: List[str] = []

    # counter tracks the depth of nesting.
    # When counter is 0, we are outside of any group.
    # When counter > 0, we are inside a group.
    nesting_depth: int = 0

    # Step 2: Iterate through each character to identify group boundaries
    for char in cleaned_string:
        if char == '(':
            # Entering a deeper level of nesting
            nesting_depth += 1
            current_group_chars.append(char)
        elif char == ')':
            # Leaving a level of nesting
            nesting_depth -= 1
            current_group_chars.append(char)

            # If nesting_depth returns to 0, it means we have closed 
            # the outermost parenthesis of a top-level group.
            if nesting_depth == 0:
                # Construct the string for the group found
                group_string = "".join(current_group_chars)
                result_groups.append(group_string)

                # Reset the buffer for the next group
                current_group_chars = []
        else:
            # If the problem guarantees only parentheses and spaces, 
            # any other character is technically invalid based on the prompt.
            # However, we simply ignore non-parenthesis characters to be robust.
            continue

    # Step 3: Final Validation
    # If nesting_depth is not zero at the end, the input was unbalanced (e.g., "(()")
    # The prompt implies groups are balanced, but we check to ensure production safety.
    if nesting_depth != 0:
        # Depending on requirements, we could raise an error or return what we have.
        # Given "Separate groups are balanced", an unbalanced input is invalid.
        raise ValueError("The provided string contains unbalanced parentheses.")

    return result_groups