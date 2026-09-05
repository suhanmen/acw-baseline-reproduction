def common_prefix(strings):
    """
    Finds the longest common prefix among a set of strings.

    Args:
        strings (list of str): The list of strings to find the common prefix of.

    Returns:
        str: The longest common prefix of the input strings.

    Raises:
        ValueError: If the input list is empty or contains empty strings.
    """
    if not strings:
        raise ValueError("Input list is empty.")

    if not all(s for s in strings):
        raise ValueError("Input contains empty strings.")

    if len(strings) == 1:
        return strings[0]

    # Determine the minimum length to check
    min_length = min(len(s) for s in strings)

    # Early exit if min_length is 0 or all strings are empty
    if min_length == 0:
        return ""

    prefix = []
    # Compare each character position
    for i in range(min_length):
        current_char = strings[0][i]
        for s in strings[1:]:
            if s[i] != current_char:
                return ''.join(prefix)
        prefix.append(current_char)

    return ''.join(prefix)

# Example usage
print(common_prefix(["tablets", "tables", "taxi", "tamarind"]))  # Output: 'ta'
print(common_prefix(["apples", "ape", "april"]))  # Output: 'ap'
print(common_prefix(["teens", "teenager", "teenmar"]))  # Output: 'teen'