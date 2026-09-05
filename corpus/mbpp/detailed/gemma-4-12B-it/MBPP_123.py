from typing import Dict

def get_proper_divisors_sum(n: int) -> int:
    """
    Calculates the sum of all proper divisors of a given integer n.
    A proper divisor is a positive divisor of n, excluding n itself.

    Example:
        get_proper_divisors_sum(220) -> 2 + 4 + 5 + 10 + 11 + 20 + 22 + 44 + 55 + 110 = 284
    """
    # Handle numbers less than 2 as they have no proper divisors > 0
    if n <= 1:
        return 0

    divisor_sum = 1  # 1 is a proper divisor for all n > 1

    # We only need to iterate up to the square root of n.
    # If d is a divisor, then n/d is also a divisor.
    limit = int(n**0.5)

    for i in range(2, limit + 1):
        if n % i == 0:
            # i is a divisor
            divisor_sum += i

            # Find the paired divisor
            paired_divisor = n // i

            # If the divisors are distinct (not the square root), add the pair
            if paired_divisor != i:
                divisor_sum += paired_divisor

    return divisor_sum

def is_amicable(a: int, b: int) -> bool:
    """
    Checks if two numbers a and b are amicable.
    Amicable numbers are two different numbers where the sum of proper 
    divisors of each is equal to the other.
    """
    # Amicable numbers must be distinct by definition
    if a == b:
        return False

    sum_a = get_proper_divisors_sum(a)
    sum_b = get_proper_divisors_sum(b)

    return sum_a == b and sum_b == a

def amicable_numbers_sum(limit: int) -> int:
    """
    Sums all amicable numbers from 1 up to a specified limit (inclusive).

    An amicable number is a number that is part of an amicable pair.
    For example, 220 and 284 are amicable numbers.

    Args:
        limit (int): The upper bound (inclusive) to check for amicable numbers.

    Returns:
        int: The sum of all amicable numbers found within the range [1, limit].
    """
    # Input validation
    if not isinstance(limit, int):
        raise TypeError("The limit must be an integer.")

    if limit < 1:
        return 0

    # To optimize, we pre-calculate the sum of proper divisors for every 
    # number up to the limit. This avoids re-calculating the divisor sum 
    # multiple times for the same number.
    divisor_sums = {}

    # Use a dictionary to cache divisor sums to ensure O(N * sqrt(N)) complexity.
    # We iterate through every number from 1 to limit.
    for i in range(1, limit + 1):
        divisor_sums[i] = get_proper_divisors_sum(i)

    total_sum = 0

    # Iterate through the range and check if the number is part of an amicable pair.
    for current_num in range(1, limit + 1):
        # Get the sum of divisors for the current number
        s_current = divisor_sums[current_num]

        # An amicable number is defined such that:
        # 1. The sum of proper divisors of 'current_num' equals some number 'target'
        # 2. The sum of proper divisors of 'target' equals 'current_num'
        # 3. 'current_num' is not equal to 'target'

        target = s_current

        # Check if the 'target' is a valid candidate:
        # - It must be different from current_num
        # - It must be within the range (though technically, a number could be 
        #   amicable with a number > limit, the problem usually implies both 
        #   numbers in the pair must be <= limit to be "found" in the sum).
        # Based on standard amicable number problems, we check if the target 
        # is <= limit and if it is amicable with current_num.

        if target != current_num and target <= limit:
            # Check if the sum of divisors of 'target' brings us back to 'current_num'
            if divisor_sums[target] == current_num:
                total_sum += current_num

    return total_sum