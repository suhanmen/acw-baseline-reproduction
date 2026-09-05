def text_match_two_three(s):
    # Check if the string has at least 4 characters
    if len(s) < 4:
        return ('Not matched!')

    # Extract the first character
    first_char = s[0]

    # Check if the first character is 'a'
    if first_char != 'a':
        return ('Not matched!')

    # Extract the substring after the first character
    rest_of_string = s[1:]

    # Check if the rest of the string has exactly 2 or 3 'b's
    if rest_of_string.count('b') not in (2, 3):
        return ('Not matched!')

    # Check if the rest of the string consists only of 'b's
    if not rest_of_string.replace('b', '').strip():
        return ('Not matched!')

    # If all checks passed
    return ('Found a match!')