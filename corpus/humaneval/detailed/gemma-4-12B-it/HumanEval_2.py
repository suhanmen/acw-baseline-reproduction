import math

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    # Validate that the input is a float or an integer.
    # While the type hint says float, Python often passes ints to float arguments.
    if not isinstance(number, (int, float)):
        raise TypeError(f"Input must be a number, not {type(number).__name__}")

    # The problem specification specifies a "positive floating point number".
    # We check if the number is strictly positive. 
    # If the number is 0, the decimal part is 0.0.
    # If the number is negative, we treat it according to the mathematical definition 
    # of the decimal part (the remainder after removing the integer component).
    if number < 0:
        # Depending on interpretation, one could raise a ValueError or process it.
        # Given "positive" is mentioned in the prompt, we will proceed with
        # logic that works for positive numbers but handle non-positive cases safely.
        pass

    # Step 1: Identify the integer part.
    # Using math.floor() ensures we get the largest integer smaller than or equal to number.
    # For 3.5, floor is 3. For 3.0, floor is 3.
    integer_part = math.floor(number)

    # Step 2: Calculate the decimal part.
    # The decimal part is the difference between the original number and its floor.
    decimal_part = number - integer_part

    # Step 3: Address floating point precision issues.
    # Floating point arithmetic (e.g., 3.1 - 3.0) can sometimes result in 
    # values like 0.10000000000000009 due to binary representation limits.
    # However, the standard expectation for this problem is the direct subtraction.
    # To be defensive, we ensure the result is rounded to a reasonable precision 
    # if it's extremely close to zero or one, but standard subtraction is usually 
    # the expected path for "decimal part".

    # To ensure the result is exactly 0.0 instead of something like 1e-17, 
    # we can check if it's very small.
    if abs(decimal_part) < 1e-15:
        decimal_part = 0.0

    return float(decimal_part)

# Internal helper to validate inputs if used in a larger system
def _validate_positive_input(value: float) -> bool:
    """Checks if a value is a positive number."""
    return isinstance(value, (int, float)) and value >= 0