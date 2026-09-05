def change_base(x: int, base: int) -> str:
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.

    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    # Input validation
    if not isinstance(x, int) or not isinstance(base, int):
        return 'invalid input'
    if x < 0:
        return 'invalid input'
    if not (2 <= base <= 9):
        return 'invalid input'

    # Special case: x is zero
    if x == 0:
        return '0'

    # Base conversion algorithm
    digits = []
    while x > 0:
        remainder = x % base
        digits.append(remainder)
        x = x // base

    # Reverse to get the correct order and convert to string
    digits = digits[::-1]
    result = ''.join(str(d) for d in digits)

    return result