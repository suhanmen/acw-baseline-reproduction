def even_odd_palindrome(n):
    """
    Given a positive integer n, return a tuple that has the number of even and odd
    integer palindromes that fall within the range(1, n), inclusive.

    Example 1:

        Input: 3
        Output: (1, 2)
        Explanation:
        Integer palindrome are 1, 2, 3. one of them is even, and two of them are odd.

    Example 2:

        Input: 12
        Output: (4, 6)
        Explanation:
        Integer palindrome are 1, 2, 3, 4, 5, 6, 7, 8, 9, 11. four of them are even, and 6 of them are odd.

    Note:
        1. 1 <= n <= 10^3
        2. returned tuple has the number of even and odd integer palindromes respectively.
    """

    def is_palindrome(number):
        """
        Determine if a given integer is a palindrome.
        A palindrome reads the same forwards and backwards.

        Args:
            number (int): The integer to check.

        Returns:
            bool: True if the number is a palindrome, False otherwise.
        """
        # Convert the number to a string representation
        number_str = str(number)

        # Get the reversed string representation
        reversed_str = number_str[::-1]

        # Compare the original string with the reversed string
        return number_str == reversed_str

    def validate_input(value):
        """
        Validate the input argument to ensure it meets the problem requirements.

        Args:
            value: The input value to validate.

        Returns:
            int: The validated integer value if valid.

        Raises:
            TypeError: If the input is not an integer.
            ValueError: If the input is not a positive integer within the allowed range.
        """
        # Check if the input is an integer
        if not isinstance(value, int):
            raise TypeError(f"Input must be an integer, got {type(value).__name__}")

        # Check if the input is positive (greater than or equal to 1)
        if value < 1:
            raise ValueError(f"Input must be a positive integer (>= 1), got {value}")

        # Check if the input is within the specified upper bound (10^3)
        if value > 1000:
            raise ValueError(f"Input must be <= 1000, got {value}")

        return value

    # Validate the input parameter
    try:
        validated_n = validate_input(n)
    except (TypeError, ValueError) as input_error:
        # Re-raise the error to stop execution with a clear message
        raise input_error

    # Initialize counters for even and odd palindromes
    even_palindrome_count = 0
    odd_palindrome_count = 0

    # Iterate through the range from 1 to n (inclusive)
    # We start at 1 because palindromes are positive integers in this context
    for current_number in range(1, validated_n + 1):
        # Check if the current number is a palindrome
        if is_palindrome(current_number):
            # Determine if the palindrome is even or odd
            if current_number % 2 == 0:
                # Increment the even counter
                even_palindrome_count += 1
            else:
                # Increment the odd counter
                odd_palindrome_count += 1

    # Return the results as a tuple (even_count, odd_count)
    return (even_palindrome_count, odd_palindrome_count)