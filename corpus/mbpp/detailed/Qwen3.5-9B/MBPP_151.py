import math

def _validate_positive_integer(value):
    """
    Validates that the input value is a positive integer (greater than 0).
    Raises a ValueError if the validation fails.
    """
    if not isinstance(value, int):
        raise TypeError(f"Input must be an integer, got {type(value).__name__}")
    if value <= 0:
        raise ValueError(f"Input must be a positive integer (> 0), got {value}")
    return value

def _calculate_greatest_common_divisor(a, b):
    """
    Calculates the Greatest Common Divisor (GCD) of two positive integers.

    We use the built-in math.gcd function for robustness and efficiency,
    but this function encapsulates the logic for clarity and separation of concerns.

    Parameters:
    a (int): First positive integer.
    b (int): Second positive integer.

    Returns:
    int: The greatest common divisor of a and b.
    """
    # Although math.gcd handles these constraints internally based on our validation,
    # we explicitly pass the validated inputs to ensure the contract holds here.
    return math.gcd(a, b)

def is_coprime(first_number, second_number):
    """
    Checks whether the given two numbers are co-prime.

    Two numbers are co-prime (or relatively prime) if their greatest common divisor (GCD) is exactly 1.

    Parameters:
    first_number (int): The first number to check. Must be a positive integer.
    second_number (int): The second number to check. Must be a positive integer.

    Returns:
    bool: True if the numbers are co-prime, False otherwise.

    Raises:
    TypeError: If either input is not an integer.
    ValueError: If either input is not greater than zero.
    """
    # Step 1: Explicitly validate the first input
    validated_first = _validate_positive_integer(first_number)

    # Step 2: Explicitly validate the second input
    validated_second = _validate_positive_integer(second_number)

    # Step 3: Calculate the Greatest Common Divisor using our helper
    common_divisor = _calculate_greatest_common_divisor(validated_first, validated_second)

    # Step 4: Determine if they are co-prime by checking if the GCD is 1
    is_coprime_status = (common_divisor == 1)

    return is_coprime_status