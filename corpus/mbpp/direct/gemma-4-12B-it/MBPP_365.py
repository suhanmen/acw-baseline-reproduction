def count_Digit(number: int) -> int:
    """
    Counts the number of digits in a given integer.
    """
    # Use absolute value to handle negative numbers correctly
    # Convert to string and count characters, excluding the minus sign if present
    return len(str(abs(number)))

if __name__ == "__main__":
    assert count_Digit(12345) == 5
    assert count_Digit(11223305) == 8
    assert count_Digit(4123459) == 7