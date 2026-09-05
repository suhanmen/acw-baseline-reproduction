def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9)."""

    def has_odd_digits(number):
        """Helper function to check if both first and last digits of a number are odd."""
        # Get the absolute value to handle negative numbers
        num = abs(number)
        # Check if the number is a single digit (<=9) which can't satisfy first digit >10 condition
        if num < 10:
            return False
        # Extract the last digit
        last_digit = num % 10
        # If last digit is even, return False
        if last_digit % 2 == 0:
            return False
        # Extract the first digit
        first_digit = num
        while first_digit >= 10:
            first_digit = first_digit // 10
        # Check if the first digit is odd
        return first_digit % 2 == 1

    def count qualifying numbers
        """Helper function to count numbers meeting the criteria"""
        count = 0
        for number in nums:
            if number > 10 and has_odd_digits(number):
                count += 1
        return count

    # Check if the input is valid (list of integers)
    if not isinstance(nums, list) or not all(isinstance(num, int) for num in nums):
        raise ValueError("Input must be a list of integers")

    return count qualifying numbers()