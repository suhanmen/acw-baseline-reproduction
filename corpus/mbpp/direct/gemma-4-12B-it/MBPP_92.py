def is_undulating(number: str) -> bool:
    """
    Checks whether a given numeric string is undulating.
    An undulating number is a number where the digits alternate between
    increasing and decreasing (e.g., high-low-high-low or low-high-low-high).
    Consecutive digits must not be equal.
    """
    if len(number) < 3:
        # A sequence of 1 or 2 digits doesn't have a pattern to "undulate" 
        # in the sense of alternating directions, but based on the assertions:
        # "121" is True (length 3).
        # We assume length < 3 are true if digits are not equal, 
        # but the problem implies a pattern of at least 3 digits.
        if len(number) == 1:
            return True
        return number[0] != number[1]

    # Check first three digits to establish the pattern
    # Must not have consecutive equal digits
    for i in range(len(number) - 1):
        if number[i] == number[i+1]:
            return False

    # Check the alternating pattern
    # The direction of change (up or down) must flip at every step
    for i in range(len(number) - 2):
        diff1 = int(number[i+1]) - int(number[i])
        diff2 = int(number[i+2]) - int(number[i+1])

        # If they don't have opposite signs, it's not undulating
        # (one must be positive, one must be negative)
        if (diff1 > 0 and diff2 > 0) or (diff1 < 0 and diff2 < 0):
            return False

    return True