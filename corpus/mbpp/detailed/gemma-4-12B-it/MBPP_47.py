from typing import List

def get_factorial_last_digit(n: int) -> int:
    """
    Computes the last digit of n! (n factorial).
    For n >= 5, n! always ends in 0 because it contains factors 2 and 5.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 6
    elif n == 4:
        return 4  # 4! = 24, last digit is 4
    else:
        # For any n >= 5, n! = 1 * 2 * 3 * 4 * 5 * ...
        # This contains at least one 2 and one 5, so it ends in 0.
        return 0

def compute_Last_Digit(a: int, b: int) -> int:
    """
    Finds the last digit of (b! / a!) given that a! divides b!.

    The logic:
    If a! divides b!, then b! / a! = (b * (b-1) * ... * (a+1)).
    The last digit of this quotient is the last digit of the product of 
    all integers from (a+1) to b.

    Special Case:
    If a == b, the quotient is 1. The last digit of 1 is 1.
    However, based on the provided assertions:
    compute_Last_Digit(2, 4) -> 4!/2! = 24/2 = 12 -> Last digit 2
    compute_Last_Digit(6, 8) -> 8!/6! = 8*7 = 56 -> Last digit 6
    compute_Last_Digit(1, 2) -> 2!/1! = 2/1 = 2 -> Last digit 2
    """
    # Input Validation
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Inputs must be integers.")

    if a < 0 or b < 0:
        raise ValueError("Inputs must be non-negative integers.")

    # If a is greater than b, a! cannot divide b! (unless a! == b! but 
    # a > b is impossible for factorials of non-negative integers).
    # However, the problem implies a! divides b!, so we assume a <= b.
    if a > b:
        # In a production environment, we might raise an error.
        # Based on the math of "a! divides b!", if a > b, this is only 
        # possible if we consider the result of the division as 0 or 
        # handle it as an undefined operation for the specific constraint.
        # Given the context, we assume a <= b.
        raise ValueError("a must be less than or equal to b for a! to divide b!.")

    # Case: a == b
    # b! / a! = 1. The last digit of 1 is 1.
    if a == b:
        return 1

    # The quotient Q = b! / a! = b * (b-1) * ... * (a+1)
    # We need the last digit of this product.
    # To find the last digit of a product, we can multiply the numbers 
    # and take the modulo 10 at each step to prevent integer overflow
    # and keep the logic focused on the last digit.

    last_digit = 1

    # We iterate from a + 1 up to b inclusive.
    # If a=2, b=4, we multiply 3 * 4.
    # If a=6, b=8, we multiply 7 * 8.
    # If a=1, b=2, we multiply 2.
    for i in range(a + 1, b + 1):
        last_digit = (last_digit * i) % 10

    return last_digit