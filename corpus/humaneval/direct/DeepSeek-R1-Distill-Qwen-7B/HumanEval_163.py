def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # Determine the start and end of the range
    start = min(a, b)
    end = max(a, b)

    even_digits = []

    for number in range(start, end + 1):
        # Check each digit in the current number
        for digit_char in str(number):
            digit = int(digit_char)
            if digit % 2 == 0:
                even_digits.append(digit)

    return even_digits