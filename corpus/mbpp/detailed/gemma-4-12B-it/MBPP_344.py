import math

def is_perfect_square(n: int) -> bool:
    """
    Determines if a non-negative integer is a perfect square.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if n is a perfect square, False otherwise.
    """
    if n < 0:
        return False
    if n == 0:
        return True

    # Calculate the integer square root
    root = int(math.isqrt(n))
    # Check if the square of the root matches the original number
    return (root * root) == n

def has_odd_factors_count_property(n: int) -> bool:
    """
    Determines if a positive integer has an odd number of factors.

    Mathematical Property:
    A positive integer has an odd number of factors if and only if
    it is a perfect square.

    Example:
    4 factors of 4 are 1, 2, 4 (3 factors - odd).
    6 factors of 6 are 1, 2, 3, 6 (4 factors - even).

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number has an odd number of factors, False otherwise.
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")

    if n <= 0:
        # Factors are typically defined for positive integers.
        # Zero has infinite factors, and negative numbers don't have
        # standard factorizations in this context.
        return False

    return is_perfect_square(n)

def count_Odd_Squares(lower_bound: int, upper_bound: int) -> int:
    """
    Counts the number of elements in the range [lower_bound, upper_bound] 
    (inclusive) that have an odd number of factors.

    An integer has an odd number of factors if and only if it is a perfect square.

    Args:
        lower_bound (int): The start of the range (inclusive).
        upper_bound (int): The end of the range (inclusive).

    Returns:
        int: The count of perfect squares in the given range.

    Raises:
        ValueError: If the range is invalid (lower_bound > upper_bound).
    """
    # Input Validation
    if not isinstance(lower_bound, int) or not isinstance(upper_bound, int):
        raise TypeError("Both bounds must be integers.")

    if lower_bound > upper_bound:
        # Handle cases where the range is logically inverted
        raise ValueError("lower_bound must be less than or equal to upper_bound.")

    count = 0

    # We iterate through the range. 
    # To handle large ranges efficiently, we could calculate the number of
    # squares mathematically, but the prompt requests explicit steps.
    # However, a simple loop is clear and follows the "no dense logic" rule.

    for current_number in range(lower_bound, upper_bound + 1):
        # A number has an odd number of factors if and only if it is a perfect square.
        # We check this property for every number in the range.
        is_odd_factor_count = has_odd_factors_count_property(current_number)

        if is_odd_factor_count:
            count += 1

    return count

# The logic can also be implemented more efficiently for very large ranges 
# using the property that we are counting squares:
# count = floor(sqrt(upper)) - floor(sqrt(lower - 1))
# But the prompt asks for explicit steps and defensive programming.