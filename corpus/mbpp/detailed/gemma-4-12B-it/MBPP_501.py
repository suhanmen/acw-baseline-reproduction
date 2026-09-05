from typing import List

def get_divisors(n: int) -> List[int]:
    """
    Calculates all positive integer divisors of a given number.

    Args:
        n (int): The integer to find divisors for.

    Returns:
        List[int]: A list of all positive divisors.
    """
    # Handle non-positive numbers by returning an empty list
    # as the problem implies standard positive divisors.
    if n <= 0:
        return []

    divisors = []
    # Iterate from 1 to the square root of n to find divisors efficiently.
    # If i is a divisor, then n/i is also a divisor.
    limit = int(n**0.5)
    for i in range(1, limit + 1):
        if n % i == 0:
            divisors.append(i)
            # If the quotient is different from the divisor, add it too.
            # This prevents duplicates for perfect squares (e.g., 4*4=16).
            quotient = n // i
            if quotient != i:
                divisors.append(quotient)

    return divisors

def num_comm_div(num1: int, num2: int) -> int:
    """
    Finds the greatest common divisor (GCD) between two numbers.
    Note: While the problem description says "common divisor", 
    the assertions (2,4)->2, (2,8)->2, (12,24)->6 indicate 
    that it specifically requires the Greatest Common Divisor (GCD).

    Args:
        num1 (int): The first integer.
        num2 (int): The second integer.

    Returns:
        int: The greatest common divisor.

    Raises:
        ValueError: If inputs are not integers.
        ArithmeticError: If inputs are zero (GCD with zero is technically 
                          the other number, but usually excluded in simple math prompts).
    """
    # Input Validation: Ensure types are correct
    if not isinstance(num1, int) or not isinstance(num2, int):
        raise ValueError("Both inputs must be integers.")

    # Handle edge cases: Zero values
    # GCD(0, x) is technically x, but standard divisor problems usually 
    # expect positive integers. We enforce strict positive checks.
    if num1 == 0 or num2 == 0:
        raise ArithmeticError("Inputs must be non-zero integers.")

    # Work with absolute values to handle negative integers correctly
    # GCD is defined as the largest positive integer.
    val1 = abs(num1)
    val2 = abs(num2)

    # Find divisors for both numbers
    divisors_1 = get_divisors(val1)
    divisors_2 = get_divisors(val2)

    # Find the intersection of the two divisor sets
    # Converting to sets ensures we only look at common values.
    set_1 = set(divisors_1)
    set_2 = set(divisors_2)

    common_divisors = set_1.intersection(set_2)

    # Handle cases where no common divisors exist (though 1 is always common)
    if not common_divisors:
        return 0

    # The problem assertions require the Greatest Common Divisor.
    # We find the maximum value in the set of common divisors.
    greatest_common_divisor = max(common_divisors)

    return greatest_common_divisor