def closest_integer(value):
    '''
    Create a function that takes a value (string) representing a number
    and returns the closest integer to it. If the number is equidistant
    from two integers, round it away from zero.

    Examples
    >>> closest_integer("10")
    10
    >>> closest_integer("15.3")
    15

    Note:
    Rounding away from zero means that if the given number is equidistant
    from two integers, the one you should return is the one that is the
    farthest from zero. For example closest_integer("14.5") should
    return 15 and closest_integer("-14.5") should return -15.
    '''
    num = float(value)
    import math

    # Get the lower and upper integers
    lower = math.floor(num)
    upper = math.ceil(num)

    # If it's already an integer
    if lower == upper:
        return int(lower)

    # Calculate distances
    dist_lower = abs(num - lower)
    dist_upper = abs(num - upper)

    if dist_lower < dist_upper:
        return int(lower)
    elif dist_upper < dist_lower:
        return int(upper)
    else:
        # Equidistant: round away from zero
        if num >= 0:
            return int(upper)
        else:
            return int(lower)