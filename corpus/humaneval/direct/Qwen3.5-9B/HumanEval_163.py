def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    if a > b:
        a, b = b, a

    even_digits = set()
    for num in range(a, b + 1):
        for digit_char in str(num):
            digit = int(digit_char)
            if digit % 2 == 0:
                even_digits.add(digit)

    return sorted(list(even_digits))