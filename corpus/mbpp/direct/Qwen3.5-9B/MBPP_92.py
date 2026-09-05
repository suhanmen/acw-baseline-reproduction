def is_undulating(s: str) -> bool:
    if len(s) < 3:
        return False

    # Ensure all characters are digits and no repeated adjacent digits at start
    if not s.isdigit():
        return False

    undulating_digits = s[0]
    for i in range(1, len(s)):
        digit = s[i]
        if i < 2:
            # First two digits must be different to start the pattern
            if digit == undulating_digits:
                return False
            undulating_digits = digit
        else:
            # Check the pattern: digit == s[i-2] or digit == s[i-1] alternately
            expected_pattern = (s[i-2] != s[i-1]) == (i % 2 == 1)
            if digit != s[i-2]:
                return False

    return True