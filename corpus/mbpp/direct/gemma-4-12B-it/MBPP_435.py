def last_Digit(number: int) -> int:
    """
    Returns the last digit of a given integer.

    Args:
        number (int): The integer to find the last digit of.

    Returns:
        int: The last digit of the input number.
    """
    return abs(number) % 10

if __name__ == "__main__":
    assert last_Digit(123) == 3
    assert last_Digit(25) == 5
    assert last_Digit(30) == 0