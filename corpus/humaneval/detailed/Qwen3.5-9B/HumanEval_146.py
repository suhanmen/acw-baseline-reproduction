def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """

    def get_first_digit(value: int) -> int:
        """
        Extracts the first digit of an integer, ignoring the sign.
        The function handles positive integers, negative integers,
        and zeros by returning 0 for zero since 0 is not considered
        a valid 'first digit' for the context of odd/even checks
        in this problem (and 0 is even anyway).

        Args:
            value (int): The integer whose first digit is to be extracted.

        Returns:
            int: The first digit of the absolute value of the input.
        """
        absolute_value = abs(value)

        if absolute_value == 0:
            return 0

        current_value = absolute_value
        while current_value >= 10:
            current_value = current_value // 10

        return current_value

    def get_last_digit(value: int) -> int:
        """
        Extracts the last digit of an integer, ignoring the sign.
        This function uses the modulo operator on the absolute value.

        Args:
            value (int): The integer whose last digit is to be extracted.

        Returns:
            int: The last digit of the absolute value of the input.
        """
        return abs(value) % 10

    def is_digit_odd(digit: int) -> bool:
        """
        Checks if a given single digit is an odd number.
        Valid odd digits are 1, 3, 5, 7, 9.

        Args:
            digit (int): The digit to check.

        Returns:
            bool: True if the digit is odd, False otherwise.
        """
        if not isinstance(digit, int):
            raise TypeError("Digit must be an integer.")
        if not 0 <= digit <= 9:
            raise ValueError("Digit must be between 0 and 9.")

        return digit % 2 == 1

    def does_number_satisfy_conditions(number: int) -> bool:
        """
        Determines if a number meets all the criteria specified in the docstring:
        1. The number must be strictly greater than 10.
        2. The number must have at least two digits (implied by > 10, but checked via first/last extraction logic).
        3. The first digit must be odd.
        4. The last digit must be odd.

        Args:
            number (int): The number to evaluate.

        Returns:
            bool: True if all conditions are met, False otherwise.
        """
        # Condition 1: Must be greater than 10
        if number <= 10:
            return False

        # Extract digits
        first_digit = get_first_digit(number)
        last_digit = get_last_digit(number)

        # Additional validation: Ensure we actually got non-zero digits for the logic to hold meaningfully
        # though technically a number like 109 has first=1 and last=9.
        # A number like 5 has first=5 and last=5, but fails the > 10 check.
        # A number like 0 fails > 10 check.

        # Condition 3: First digit must be odd
        if not is_digit_odd(first_digit):
            return False

        # Condition 4: Last digit must be odd
        if not is_digit_odd(last_digit):
            return False

        return True

    # Input Validation
    if not isinstance(nums, list):
        raise TypeError("Input 'nums' must be a list.")

    for index, element in enumerate(nums):
        if not isinstance(element, (int, float)):
            raise TypeError(f"Element at index {index} is not a number.")

        # Check if float is actually an integer representation
        if isinstance(element, float):
            if not element.is_integer():
                raise TypeError(f"Element at index {index} is a non-integer float.")

    count = 0

    for element in nums:
        # Convert to integer to handle whole-number floats (e.g., 15.0)
        numeric_value = int(element)

        if does_number_satisfy_conditions(numeric_value):
            count = count + 1

    return count