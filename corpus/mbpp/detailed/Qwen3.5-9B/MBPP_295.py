import math

def _find_divisors_up_to_sqrt(n: int) -> list[int]:
    """
    Returns a sorted list of all positive divisors of n by iterating
    only up to the integer square root of n.

    Steps:
    1. Initialize an empty list to hold divisors.
    2. Iterate from i = 1 to floor(sqrt(n)).
    3. For each i that divides n evenly:
       a. Append i to the list.
       b. If i is not the square root of n, append n // i as the paired divisor.
    4. Sort the list to ensure deterministic order.
    """
    if n <= 0:
        return []

    divisors: list[int] = []
    sqrt_n = int(math.isqrt(n))

    for i in range(1, sqrt_n + 1):
        if n % i == 0:
            small_divisor = i
            large_divisor = n // i

            divisors.append(small_divisor)

            if small_divisor != large_divisor:
                divisors.append(large_divisor)

    divisors.sort()
    return divisors


def sum_div(n: int) -> int:
    """
    Calculates and returns the sum of all positive divisors of n.

    Validation:
    - The input n must be an integer.
    - The input n must be non-zero (since divisors are defined for positive integers).
      Note: While mathematically divisors exist for negative numbers, the problem
      context (assertions for 7, 8, 12) implies positive integers. We handle n=0
      explicitly as it has no positive divisors in this context.

    Logic:
    1. Validate input type.
    2. Handle zero case explicitly.
    3. Compute divisors using an efficient O(sqrt(n)) approach.
    4. Sum the divisors.

    Returns:
        The sum of all positive divisors of n.
    """
    # Validate type
    if not isinstance(n, int):
        raise TypeError(f"Expected integer input, got {type(n).__name__}")

    # Validate value: divisors are typically defined for positive integers in this context.
    # The problem assertions imply positive inputs.
    if n == 0:
        # Zero has infinitely many divisors or undefined depending on context.
        # Based on standard programming problem constraints for "sum of divisors",
        # 0 is usually treated as having no valid divisors or being invalid.
        # Given the constraints of the problem (assertions on positive integers),
        # we return 0 for 0 as there are no positive integers d where n % d == 0 is uniquely defined,
        # or simply treat it as having no positive divisors.
        return 0

    # Compute divisors
    divisor_list = _find_divisors_up_to_sqrt(n)

    # Calculate sum
    total_sum = sum(divisor_list)

    return total_sum