import re

def _parse_string_to_float(value: str) -> float:
    """
    Attempts to parse a string representation of a number into a float.

    Args:
        value (str): The string to parse.

    Returns:
        float: The parsed float value.

    Raises:
        ValueError: If the string cannot be parsed as a number.
    """
    if not isinstance(value, str):
        raise TypeError("Input must be a string.")

    if not value:
        raise ValueError("Input string cannot be empty.")

    # Define a regex pattern for valid floating-point numbers
    # Allows optional sign, digits, optional decimal point with digits.
    # Handles cases like "123", ".45", "-12.3", "+.5", etc.
    pattern = r'^[+-]?(\d+(\.\d*)?|\.\d+)$'

    if not re.match(pattern, value):
        raise ValueError(f"Invalid number format: '{value}'")

    try:
        number = float(value)
        if not isinstance(number, (int, float)):
            raise ValueError()
        return number
    except ValueError:
        raise ValueError(f"Unable to convert string to float: '{value}'")

def _determine_rounded_integer(float_value: float) -> int:
    """
    Determines the closest integer to a given float value.
    Uses standard rounding rules with a specific tie-breaking condition:
    if equidistant between two integers, round away from zero.

    Args:
        float_value (float): The number to round.

    Returns:
        int: The rounded integer.
    """
    # Truncate towards zero to get the integer part
    truncated = int(float_value)

    # Calculate the difference between the number and the truncated integer
    # This gives us the fractional part relative to zero
    fractional_part = float_value - truncated

    # Check if the number is equidistant from two integers
    # This happens when the absolute value of the fractional part is exactly 0.5
    # However, due to float precision, we check if the remainder is very close to 0.5
    # Specifically, we look at the distance to the next integer.

    # Distance to the next higher integer (if positive) or next lower (if negative)
    # Actually, let's look at the distance from truncated to the true value.
    # If abs(fractional_part) == 0.5, we need to decide direction.

    # Due to floating point inaccuracy (e.g., 0.5 might be 0.49999999 or 0.50000001),
    # we need a small epsilon to detect the "exactly 0.5" case robustly, 
    # but the problem implies mathematical exactness. 
    # A common robust way is to check if 2 * abs(fractional_part) is close to 1.0.

    two_times_fractional = 2.0 * abs(fractional_part)

    # Epsilon for floating point comparison
    epsilon = 1e-9

    is_equidistant = (abs(two_times_fractional - 1.0) < epsilon)

    if is_equidistant:
        # We are exactly in the middle (e.g., 14.5 or -14.5)
        # Rule: Round away from zero.
        if float_value > 0:
            # Positive number: round up (truncate + 1)
            return truncated + 1
        else:
            # Negative number: round down (truncate - 1)
            # Example: -14.5. Truncated is -14. Away from zero is -15.
            # Since trunc(-14.5) is -14, we subtract 1 to get -15.
            return truncated - 1
    else:
        # Not equidistant. Standard rounding: round to the nearest.
        # If fractional part >= 0.5, move away from truncated.
        # If fractional part < 0.5, stay at truncated.

        # Re-evaluate fractional part for standard rounding logic
        # We need the magnitude of the fractional part relative to 0.5
        abs_fractional = abs(fractional_part)

        if abs_fractional >= 0.5:
            # Round away from the truncated value
            if float_value > 0:
                return truncated + 1
            else:
                return truncated - 1
        else:
            # Round towards the truncated value
            return truncated

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

    # Step 1: Validate and parse the input string into a float.
    # We explicitly handle type checking and string validation here.
    try:
        number = _parse_string_to_float(value)
    except (TypeError, ValueError) as error:
        # Re-raise or handle appropriately. For this problem, 
        # re-raising the informative error is the defensive approach.
        raise error from None

    # Step 2: Apply the custom rounding logic to the parsed float.
    # We separate the logic to ensure the specific "away from zero" 
    # tie-breaking rule is implemented clearly and correctly.
    result = _determine_rounded_integer(number)

    # Step 3: Return the calculated integer result.
    return result