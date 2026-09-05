import math

def multiply(a: int, b: int) -> int:
    """Complete the function that takes two integers and returns 
    the product of their unit digits.
    Assume the input is always valid.
    Examples:
    multiply(148, 412) should return 16.
    multiply(19, 28) should return 72.
    multiply(2020, 1851) should return 0.
    multiply(14,-15) should return 20.
    """
    # Internal helper to extract the unit digit of an integer.
    # The unit digit is the digit in the ones place.
    # For negative numbers, the unit digit is treated as the positive
    # representation of that digit (e.g., the unit digit of -15 is 5).
    def get_unit_digit(number: int) -> int:
        # Use the absolute value to ensure we are looking at the magnitude
        # of the digit, as the problem implies (e.g., -15 -> 5).
        absolute_value = abs(number)

        # The modulo operator (%) with 10 returns the remainder of 
        # division by 10, which effectively isolates the ones place.
        unit_digit = absolute_value % 10

        return unit_digit

    # Input Validation:
    # Although the prompt says assume input is valid, production-grade 
    # code should verify types to ensure robustness.
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both inputs must be of type int.")

    # Step 1: Extract the unit digit of the first integer.
    unit_digit_a = get_unit_digit(a)

    # Step 2: Extract the unit digit of the second integer.
    unit_digit_b = get_unit_digit(b)

    # Step 3: Calculate the product of these two digits.
    product = unit_digit_a * unit_digit_b

    # Step 4: Return the final result.
    return product