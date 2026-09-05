def count_occurance(s):
    """
    Counts the number of exact 'std' occurrences in the input string.

    Args:
        s: The input string to search for 'std'.

    Returns:
        The count of 'std' occurrences as an integer.
    """
    # Input validation
    if not isinstance(s, str) or len(s) < 3:
        return 0

    count = 0
    for i in range(len(s) - 2):
        substring = s[i:i+3]
        if substring == 'std':
            count += 1

    return count

# Test the function with provided examples
assert count_occurance("letstdlenstdporstd") == 3
assert count_occurance("truststdsolensporsd") == 1
assert count_occurance("makestdsostdworthit") == 2