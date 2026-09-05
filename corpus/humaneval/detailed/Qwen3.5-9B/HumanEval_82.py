def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """

    # Helper function to validate the input type
    def is_valid_string_input(value):
        """Checks if the input is an instance of str.

        If not, raises a TypeError with a descriptive message.
        """
        if not isinstance(value, str):
            raise TypeError(
                f"Input must be of type 'str', but got '{type(value).__name__}' instead."
            )
        return True

    # Helper function to check if a number is prime
    def is_prime_number(number):
        """Determines if a non-negative integer is a prime number.

        A prime number is a natural number greater than 1 that has no positive
        divisors other than 1 and itself.

        Args:
            number (int): The number to check for primality.

        Returns:
            bool: True if the number is prime, False otherwise.
        """
        # Edge case: Numbers less than 2 are not prime
        if number < 2:
            return False

        # Edge case: 2 is the only even prime number
        if number == 2:
            return True

        # Edge case: All other even numbers are not prime
        if number % 2 == 0:
            return False

        # Optimization: Check for odd divisors up to the square root of the number
        # We start from 3 and increment by 2 to skip even numbers.
        divisor = 3
        max_divisor = int(number ** 0.5) + 1

        while divisor < max_divisor:
            if number % divisor == 0:
                return False
            divisor += 2

        return True

    # Main logic execution starts here

    # Step 1: Validate the input argument explicitly
    try:
        is_valid_string_input(string)
    except TypeError as e:
        raise e

    # Step 2: Calculate the length of the string
    string_length = len(string)

    # Step 3: Check if the calculated length is a prime number using the helper
    result = is_prime_number(string_length)

    return result