def is_Diff(number):
    """
    Determines if the difference between the sum of even and odd digits is a specific value.

    Args:
        number (int): The input integer whose digits will be analyzed.

    Returns:
        int: The difference between the sum of even digits and the sum of odd digits.
    """
    # Handle invalid input by raising an error
    if not isinstance(number, int):
        raise ValueError("Input must be an integer.")

    # Handle negative numbers by taking absolute value
    num = abs(number)

    # Initialize sums for even and odd digits
    sum_even = 0
    sum_odd = 0

    # Helper function to split digits into even and odd
    def split_digits(n):
        while n > 0:
            digit = n % 10
            if digit % 2 == 0:
                sum_even += digit
            else:
                sum_odd += digit
            n = n // 10
        return sum_even, sum_odd

    # Split the number into even and odd digits
    sum_even, sum_odd = split_digits(num)

    # Calculate the difference
    difference = sum_even - sum_odd

    return difference