def sum_of_digits(numbers):
    """
    Compute the sum of digits of each number in the given list.

    Args:
        numbers (list): A list of integers.

    Returns:
        int: The sum of all digits in the list.

    Raises:
        TypeError: If input is not a list or contains non-integer elements.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list.")
    for num in numbers:
        if not isinstance(num, int):
            raise TypeError("All elements in the list must be integers.")

    if not numbers:
        return 0

    total = 0
    for num in numbers:
        abs_num = abs(num)
        num_str = str(abs_num)
        for digit_char in num_str:
            total += int(digit_char)

    return total