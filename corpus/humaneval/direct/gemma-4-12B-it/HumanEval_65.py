def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    s = str(x)
    n = len(s)

    if shift > n:
        return s[::-1]

    # For circular shift right by 'shift'
    # The last 'shift' digits move to the front
    # Example: 123, shift 1 -> 312
    # Example: 12, shift 1 -> 21
    shift %= n
    if shift == 0:
        return s

    res = s[-shift:] + s[:-shift]
    return res