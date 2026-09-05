import math

def is_prime(n: int) -> bool:
    """
    Helper function to determine if an integer is a prime number.
    A prime number is a natural number greater than 1 that has no 
    positive divisors other than 1 and itself.
    """
    # Prime numbers must be greater than 1.
    # This handles 0, 1, and negative numbers.
    if n <= 1:
        return False

    # 2 and 3 are prime numbers.
    if n <= 3:
        return True

    # Eliminate even numbers and multiples of 3 early to optimize.
    if n % 2 == 0 or n % 3 == 0:
        return False

    # Use the 6k +/- 1 rule to check for factors.
    # We only need to check up to the square root of n.
    limit = int(math.isqrt(n))
    for i in range(5, limit + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False

    return True

def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Defensive programming: Verify that the input is actually a string.
    # If the input is not a string, we raise a TypeError to ensure
    # the function is used correctly in a production environment.
    if not isinstance(string, str):
        raise TypeError(f"Expected input of type 'str', but received '{type(string).__name__}'.")

    # Calculate the length of the input string.
    # This handles empty strings (length 0), single characters (length 1),
    # and any other string length.
    string_length = len(string)

    # Delegate the primality test to the helper function.
    # The logic is separated to improve readability and testability.
    result = is_prime(string_length)

    return result