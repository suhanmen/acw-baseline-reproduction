import math

def count_Digit(number: int) -> int:
    """
    Count the number of digits in a given integer.

    This function handles both positive and negative integers.
    Negative numbers are treated based on their absolute value for digit counting,
    as the sign itself does not constitute a digit.

    Parameters:
    number (int): The integer whose digits are to be counted.

    Returns:
    int: The count of digits in the number.

    Raises:
    TypeError: If the input is not an integer.
    """

    # Step 1: Validate the input type
    if not isinstance(number, int):
        raise TypeError(f"Input must be an integer, got {type(number).__name__}")

    # Step 2: Handle the specific edge case where the number is zero.
    # Zero is a single-digit number.
    if number == 0:
        return 1

    # Step 3: Take the absolute value to handle negative numbers uniformly.
    # We store this in a named variable for clarity and potential reuse.
    absolute_value = abs(number)

    # Step 4: Calculate the logarithm base 10 of the absolute value.
    # math.log10 returns the exponent to which 10 must be raised to equal the number.
    # For example, log10(100) = 2.
    log_value = math.log10(absolute_value)

    # Step 5: Determine the integer part of the logarithm.
    # Since log10 of a power of 10 (like 100) is an integer (2.0), we can cast to int directly
    # for powers of 10, but for other numbers (like 123, log is ~2.089), int() floors it.
    # However, a more robust way for non-powers of 10 without relying on float precision quirks
    # for the boundary check involves checking if the log is mathematically an integer.
    # Given the constraints of standard floating point, a small epsilon check is often used,
    # or simpler logic: floor(log10(n)) + 1 for n > 0 covers all cases.
    # Let's verify:
    # n=1 -> log10=0 -> floor=0 -> +1 = 1 (Correct)
    # n=9 -> log10=0.95 -> floor=0 -> +1 = 1 (Correct)
    # n=10 -> log10=1 -> floor=1 -> +1 = 2 (Correct)
    # n=99 -> log10=1.99 -> floor=1 -> +1 = 2 (Correct)
    # n=100 -> log10=2 -> floor=2 -> +1 = 3 (Correct)

    digit_count = int(math.floor(log_value)) + 1

    return digit_count