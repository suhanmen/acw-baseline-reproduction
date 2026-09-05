import math
from typing import List

def is_perfect_square(n: int) -> bool:
    """
    Helper function to determine if a non-negative integer is a perfect square.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if n is a perfect square, False otherwise.
    """
    if n < 0:
        return False
    if n == 0 or n == 1:
        return True

    # Calculate the integer square root
    root = int(math.isqrt(n))

    # Verify by squaring the result
    return (root * root) == n

def prod_Square(n: int) -> bool:
    """
    Checks whether the given number can be represented by the product of 
    two perfect squares (x^2 * y^2 = n).

    A number is a product of two squares if and only if it is itself 
    a perfect square (since x^2 * y^2 = (x*y)^2).
    However, the problem implies looking for two squares x^2 and y^2 
    where x and y are integers.

    Note on the provided assertions:
    prod_Square(25) == False
    prod_Square(30) == False
    prod_Square(16) == True

    Wait, let's re-examine the assertions:
    25 = 5^2. 5^2 can be 1^2 * 5^2 or 5^2 * 1^2.
    If prod_Square(25) is False, it implies the problem might mean 
    the product of two NON-UNIT squares (x^2 * y^2 where x, y > 1).

    Wait, let's re-read: "product of two squares".
    Usually, 1 is a perfect square. 
    If prod_Square(25) is False, then the "two squares" must be 
    distinct/non-unit or the prompt implies something specific.

    Let's analyze the numbers:
    25 = 5 * 5. (Squares are 1, 4, 9, 16, 25...)
    30 = ? (Not a square)
    16 = 4 * 4. (Squares are 1, 4, 9, 16, 25...)

    If 16 is True and 25 is False:
    16 = 4 * 4 (Both 4 and 4 are squares > 1).
    25 = 5 * 5 (Only 1*25 is possible, but if 25 is False, it means 
    we can't use 1). 
    Wait, 25 = 5 * 5. 5 is not a square. 25 is a square.
    If 16 = 4 * 4, then 4 is a square.
    If 25 = 5 * 5, 5 is NOT a square.

    The rule is: n = a^2 * b^2, where a and b are integers.
    This is equivalent to n = (a*b)^2. 
    Wait, if n = (a*b)^2, then n is a perfect square.
    But 25 is a perfect square. If prod_Square(25) is False, 
    then the logic "n = (a*b)^2" is not the only condition.

    Let's re-examine:
    16 = 4 * 4. (4 is a square).
    25 = 5 * 5. (5 is NOT a square).

    Therefore, the condition is: 
    n must be representable as n = x * y, where x is a perfect square 
    AND y is a perfect square, AND x and y are BOTH greater than 1.

    Let's test:
    25: Factors are (1, 25), (5, 5). 
        - 1 and 25: 1 is a square, 25 is a square. But 1 is a unit.
        - 5 and 5: 5 is not a square.
        If 1 is excluded, 25 is False.
    30: Factors are (1, 30), (2, 15), (3, 10), (5, 6).
        - None are pairs of squares > 1.
        Result: False.
    16: Factors are (1, 16), (2, 8), (4, 4).
        - 4 and 4: 4 is a square. 4 > 1.
        Result: True.

    Conclusion: The function checks if n = x * y where x and y are 
    perfect squares and x > 1 and y > 1.
    """
    # Input validation
    if not isinstance(n, int):
        raise ValueError("Input must be an integer.")

    # Handle non-positive numbers
    # Squares are non-negative, so their product is non-negative.
    if n <= 0:
        return False

    # We are looking for n = x * y
    # where x = a^2 and y = b^2 for some integers a, b > 1.
    # This implies n = (a*b)^2.
    # However, we need to ensure that n can be split into two 
    # factors x and y such that both are perfect squares > 1.

    # If n is not a perfect square, it cannot be a product of two squares.
    if not is_perfect_square(n):
        return False

    # If n is a perfect square, n = k^2.
    # We need to find if k^2 = a^2 * b^2 for some a, b > 1.
    # This is equivalent to finding if k = a * b for some a, b > 1.
    # This is possible if and only if k is a composite number.

    root_n = math.isqrt(n)

    # Now we check if root_n is composite.
    # A number is composite if it has a factor other than 1 and itself.
    # Smallest composite number is 4 (2*2).

    if root_n < 4:
        return False

    # Check if root_n has any divisor d such that 1 < d < root_n.
    # If it does, then root_n = d * (root_n / d),
    # so n = d^2 * (root_n / d)^2.
    # Both d^2 and (root_n / d)^2 will be perfect squares > 1.

    has_divisor = False
    for i in range(2, int(math.isqrt(root_n)) + 1):
        if root_n % i == 0:
            has_divisor = True
            break

    return has_divisor