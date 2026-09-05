import math

def count_Digit(number: int) -> int:
    """
    Counts the number of digits in a given integer.

    The function handles:
    - Positive integers
    - Negative integers (count ignores the sign)
    - Zero (which has 1 digit)
    - Large integers

    Args:
        number (int): The integer to be checked.

    Returns:
        int: The total count of digits in the absolute value of the number.

    Raises:
        TypeError: If the input is not an integer.
    """
    # 1. Input Validation: Ensure the input is actually an integer.
    if not isinstance(number, int):
        raise TypeError(f"Expected an integer, but received {type(number).__name__}")

    # 2. Handle the zero case explicitly.
    # Zero is a single-digit number.
    if number == 0:
        return 1

    # 3. Handle negative numbers.
    # The digit count of -123 is the same as 123 (3 digits).
    # We work with the absolute value to avoid issues with sign representation.
    absolute_value = abs(number)

    # 4. Calculate the number of digits.
    # We can do this by converting to string or by using mathematical log10.
    # String conversion is very safe and avoids precision issues with extremely large floats.

    # Convert to string to count characters.
    # Since we already took the absolute value, we don't have to worry about the '-' sign.
    string_representation = str(absolute_value)
    digit_count = len(string_representation)

    return digit_count

# The assertions provided in the prompt:
if __name__ == "__main__":
    # Test cases provided by the user
    assert count_Digit(12345) == 5
    assert count_Digit(11223305) == 8
    assert count_Digit(4123459) == 7

    # Additional robust test cases:
    assert count_Digit(0) == 1           # Edge case: zero
    assert count_Digit(-500) == 3        # Edge case: negative number
    assert count_Digit(7) == 1           # Edge case: single digit
    assert count_Digit(1000000000) == 10 # Boundary: large power of 10