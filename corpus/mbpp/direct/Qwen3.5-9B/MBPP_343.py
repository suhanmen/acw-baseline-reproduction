def dig_let(s: str) -> tuple:
    """
    Calculate the number of digits and letters in a string.

    Args:
        s (str): The input string.

    Returns:
        tuple: A tuple containing (count_of_digits, count_of_letters).
    """
    digit_count = 0
    letter_count = 0

    for char in s:
        if char.isdigit():
            digit_count += 1
        elif char.isalpha():
            letter_count += 1

    return (digit_count, letter_count)