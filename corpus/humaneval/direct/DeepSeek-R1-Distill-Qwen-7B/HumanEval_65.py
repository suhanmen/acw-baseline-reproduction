def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    x_str = str(x)
    num_digits = len(x_str)

    if shift >= num_digits or shift <= 0:
        if shift >= num_digits:
            return ''.join(reversed(x_str))
        else:
            return x_str

    # Calculate effective shift
    effective_shift = shift % num_digits

    # Perform circular shift
    shifted_part = x_str[-effective_shift:]
    result = shifted_part + x_str[:-effective_shift]

    return result