def first_Digit(number: int) -> int:
    """
    Finds the first digit of a given number.

    Args:
        number (int): The integer to evaluate.

    Returns:
        int: The first digit of the number.
    """
    # Convert to string and strip the negative sign if present
    s = str(abs(number))
    # Return the first character converted back to an integer
    return int(s[0])

if __name__ == "__main__":
    assert first_Digit(123) == 1
    assert first_Digit(456) == 4
    assert first_Digit(12) == 1