def is_undulating(number: str) -> bool:
    # Validate the input to ensure it's a string of digits
    if not number.isdigit():
        return False

    # Handle edge cases
    if len(number) == 1:
        return True
    if len(number) == 2:
        return True

    # Extract the first two digits to determine the pattern
    a = number[0]
    b = number[1]
    if a == b:
        # All digits must be the same
        return all(c == a for c in number)

    # Determine the pattern based on the first two digits
    pattern = [a, b]
    expected = b

    # Check the rest of the digits
    for c in number[2:]:
        if c != expected:
            # The pattern was broken
            return False
        expected = a  # Alternate to the other pattern digit

    # If all digits follow the pattern, it's undulating
    return True