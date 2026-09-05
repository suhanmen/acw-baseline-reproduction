def validate(n: int) -> bool:
    """
    Checks whether the frequency of each digit in a given integer 
    is less than or equal to the digit itself.
    """
    s = str(abs(n))
    counts = {}

    # Count the frequency of each digit
    for char in s:
        digit = int(char)
        counts[digit] = counts.get(digit, 0) + 1

    # Check if frequency <= digit value
    for digit, count in counts.items():
        if count > digit:
            return False

    return True