def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # Validate inputs
    if not (isinstance(a, int) and isinstance(b, int) and a > 0 and b > 0):
        return []

    # Ensure a is the smaller number
    start, end = (a, b) if a < b else (b, a)

    result = []

    # Iterate through each number from start to end inclusive
    for number in range(start, end + 1):
        # Convert number to string to iterate through each digit
        for digit_char in str(number):
            digit = int(digit_char)
            if digit % 2 == 0:
                result.append(digit)

    return result