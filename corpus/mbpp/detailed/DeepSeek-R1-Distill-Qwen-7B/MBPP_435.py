def last_Digit(number):
    """
    Finds the last digit of a given number.

    Args:
        number (int): The number whose last digit is to be found.

    Returns:
        int: The last digit of the number.

    Raises:
        TypeError: If the input is not an integer.
    """
    if not isinstance(number, int):
        raise TypeError("Input must be an integer.")

    # Handle negative numbers by converting them to positive
    num = abs(number)

    # Get the last digit using modulus 10
    last_digit = num % 10

    # Handle the case where the number is 0
    if number == 0:
        return 0

    return last_digit

# Test cases
assert last_Digit(123) == 3, "Test case 1 failed"
assert last_Digit(25) == 5, "Test case 2 failed"
assert last_Digit(30) == 0, "Test case 3 failed"

# Test with negative number
assert last_Digit(-45) == 5, "Test case 4 failed"

# Test with zero
assert last_Digit(0) == 0, "Test case 5 failed"

# Test with invalid input
try:
    last_Digit("123")
except TypeError:
    pass