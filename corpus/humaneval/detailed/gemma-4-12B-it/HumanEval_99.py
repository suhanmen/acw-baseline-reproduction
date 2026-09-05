import math

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
    # Step 1: Validate input type
    if not isinstance(value, str):
        raise TypeError(f"Expected input type 'str', but received '{type(value).__name__}'.")

    # Step 2: Handle empty input
    if not value.strip():
        raise ValueError("Input string is empty or contains only whitespace.")

    # Step 3: Convert string to float
    try:
        numeric_value = float(value)
    except ValueError as e:
        raise ValueError(f"The provided string '{value}' cannot be parsed as a valid number.") from e

    # Step 4: Determine the candidates for rounding
    # The closest integer must be either the floor or the ceiling of the value.
    floor_val = math.floor(numeric_value)
    ceil_val = math.ceil(numeric_value)

    # Step 5: Logic for finding the closest integer
    # If the value is already an integer, return it.
    if floor_val == ceil_val:
        return int(floor_val)

    # Calculate distances from the given numeric value
    distance_to_floor = abs(numeric_value - floor_val)
    distance_to_ceil = abs(numeric_value - ceil_val)

    # Step 6: Determine the result based on distance and rounding rules
    # Rule 1: If one distance is strictly smaller, pick that one.
    if distance_to_floor < distance_to_ceil:
        result = floor_val
    elif distance_to_ceil < distance_to_floor:
        result = ceil_val
    else:
        # Rule 2: If distances are equal (equidistant), round away from zero.
        # For positive numbers, away from zero is the larger (ceil) value.
        # For negative numbers, away from zero is the smaller (floor) value.
        if numeric_value > 0:
            result = ceil_val
        else:
            result = floor_val

    return int(result)