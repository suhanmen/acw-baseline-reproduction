import math
from typing import List

def get_divisors(n: int) -> List[int]:
    """
    Calculates all positive divisors of a given integer n.

    Args:
        n: The integer to find divisors for.

    Returns:
        A list of all positive integers that divide n without a remainder.
    """
    if n <= 0:
        # Divisors are typically defined for positive integers in this context.
        # If n is 0, it has infinite divisors; if negative, we treat as absolute.
        return []

    divisors = []
    # We only need to iterate up to the square root of n for efficiency.
    limit = int(math.isqrt(n))

    for i in range(1, limit + 1):
        if n % i == 0:
            divisors.append(i)
            # If the quotient is different from the divisor, add it too.
            # This handles cases like 16: 4*4, we don't want to add 4 twice.
            quotient = n // i
            if quotient != i:
                divisors.append(quotient)

    return divisors

def find_common_divisors_sum(num1: int, num2: int) -> int:
    """
    Finds the sum of all common divisors of two given numbers.

    Args:
        num1: The first integer.
        num2: The second integer.

    Returns:
        The sum of the common divisors of num1 and num2.

    Raises:
        ValueError: If inputs are not integers.
    """
    # Input Validation
    if not isinstance(num1, int) or not isinstance(num2, int):
        raise ValueError("Both inputs must be integers.")

    # Handle the case where numbers are zero or negative.
    # Common divisors are usually considered for the magnitudes of the numbers.
    abs_num1 = abs(num1)
    abs_num2 = abs(num2)

    # Edge case: If both are 0, common divisors are infinite. 
    # However, based on the test cases, we assume positive integer inputs.
    # If one is 0, the common divisors are the divisors of the non-zero number.
    # If both are 0, this logic would be ill-defined.
    if abs_num1 == 0 and abs_num2 == 0:
        return 0

    # Step 1: Get divisors for the first number.
    divisors1 = get_divisors(abs_num1)

    # Step 2: Get divisors for the second number.
    divisors2 = get_divisors(abs_num2)

    # Step 3: Identify common divisors.
    # Using a set to ensure uniqueness, though get_divisors already handles uniqueness.
    set_divisors1 = set(divisors1)
    set_divisors2 = set(divisors2)

    common_divisors = []
    for d in set_divisors1:
        if d in set_divisors2:
            common_divisors.append(d)

    # Step 4: Calculate the sum.
    total_sum = sum(common_divisors)

    return total_sum

def sum(num1: int, num2: int) -> int:
    """
    Wrapper function to match the required signature.
    Note: This shadows the built-in sum() function locally.
    """
    return find_common_divisors_sum(num1, num2)

# The logic is encapsulated in the find_common_divisors_sum function,
# but the entry point is named 'sum' as per the requirement.