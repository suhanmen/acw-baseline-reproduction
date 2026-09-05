import math

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

    # Input validation: Ensure n is an integer
    if not isinstance(n, int):
        raise ValueError("Input n must be an integer.")

    # Input validation: Check the range constraints (1 <= n <= 10^3)
    if n < 1:
        # While the problem states n is a positive integer, 
        # we handle non-positive inputs defensively.
        return (0, 0)

    if n > 1000:
        # The problem constraints specify n <= 1000. 
        # We allow the function to work but could optionally raise an error or clip.
        pass

    def is_palindrome(number: int) -> bool:
        """
        Helper function to determine if a number reads the same backwards.
        """
        # Convert integer to string to check palindromic property
        str_representation = str(number)
        # Compare string with its reverse
        reversed_string = str_representation[::-1]

        return str_representation == reversed_string

    even_palindrome_count = 0
    odd_palindrome_count = 0

    # Iterate through the range [1, n] inclusive
    # range(1, n + 1) ensures that n is included in the check
    for current_num in range(1, n + 1):
        # Check if the current number is a palindrome
        if is_palindrome(current_num):
            # Determine if the palindrome is even or odd
            if current_num % 2 == 0:
                # Increment even count
                even_palindrome_count += 1
            else:
                # Increment odd count
                odd_palindrome_count += 1

    # Return the result as a tuple (even_count, odd_count)
    return (even_palindrome_count, odd_palindrome_count)