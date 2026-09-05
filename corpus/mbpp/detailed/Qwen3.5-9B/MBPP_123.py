def calculate_divisor_sum(n):
    """
    Calculate the sum of all proper divisors of a positive integer n.
    Proper divisors are all divisors of n excluding n itself.

    Args:
        n (int): A positive integer greater than 0.

    Returns:
        int: The sum of all proper divisors of n.

    Raises:
        ValueError: If n is not a positive integer.
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError(f"Input must be a positive integer, got {n}")

    if n == 1:
        return 0

    divisor_sum = 1  # 1 is always a proper divisor for n > 1

    # We only need to check up to the square root of n
    limit = int(n ** 0.5)

    for i in range(2, limit + 1):
        if n % i == 0:
            divisor_sum += i
            other_divisor = n // i
            if other_divisor != i:  # Avoid adding the square root twice for perfect squares
                divisor_sum += other_divisor

    return divisor_sum

def is_amicable_pair(a, b):
    """
    Check if two numbers form an amicable pair.
    Two numbers are amicable if the sum of proper divisors of each equals the other.
    Note: This function does not check if they are within a specific range,
    just if they are mathematically an amicable pair.

    Args:
        a (int): First positive integer.
        b (int): Second positive integer.

    Returns:
        bool: True if a and b are amicable, False otherwise.

    Raises:
        ValueError: If inputs are not positive integers.
    """
    if not isinstance(a, int) or not isinstance(b, int) or a <= 0 or b <= 0:
        raise ValueError("Inputs must be positive integers")

    # They must be distinct for an amicable pair
    if a == b:
        return False

    sum_a = calculate_divisor_sum(a)
    sum_b = calculate_divisor_sum(b)

    return sum_a == b and sum_b == a

def find_amicable_numbers_up_to(n):
    """
    Find all amicable numbers up to the specified limit n.
    A number x is amicable if there exists a distinct number y such that
    sum of divisors of x is y and sum of divisors of y is x, and x <= n.

    Args:
        n (int): Upper bound (inclusive) for the range of numbers to check.

    Returns:
        list: A sorted list of unique amicable numbers in the range [1, n].

    Raises:
        ValueError: If n is not a positive integer.
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError(f"Input must be a positive integer, got {n}")

    amicable_numbers_set = set()

    for candidate in range(1, n + 1):
        sum_divisors = calculate_divisor_sum(candidate)

        # Check if the partner exists within our bounds and forms an amicable pair
        # We need the partner to be less than or equal to n to count it as an amicable number "from 1 to n"
        # However, the definition of "amicable numbers from 1 to n" usually means 
        # numbers x where 1 <= x <= n that are part of an amicable pair.
        # The partner y doesn't necessarily have to be <= n for x to be considered,
        # BUT for x to be counted in the sum, it must be that x is amicable.
        # Standard interpretation: Find all x in [1, n] that are amicable numbers.
        # x is amicable if there exists y (y != x) such that d(x)=y and d(y)=x.

        if sum_divisors > n:
            # If the partner is greater than n, we still need to check if it forms an amicable pair
            # But wait, if y > n, then y is not in our search range [1, n].
            # Does that matter? The problem asks to sum "amicable numbers from 1 to n".
            # This implies we are summing the values x where 1 <= x <= n AND x is amicable.
            # Whether the partner y is <= n or > n, if x is amicable, x counts.
            pass

        if sum_divisors != candidate and sum_divisors > 0:
            potential_partner = sum_divisors

            # Verify the pair relationship
            sum_partner = calculate_divisor_sum(potential_partner)

            if sum_partner == candidate and potential_partner != candidate:
                # They are amicable. Add the candidate if it is within the limit.
                # The problem asks for numbers FROM 1 TO N, so we check if candidate <= n.
                # We also need to ensure the partner is valid (positive integer).
                if 1 <= candidate <= n:
                    amicable_numbers_set.add(candidate)

    return sorted(list(amicable_numbers_set))

def amicable_numbers_sum(n):
    """
    Calculate the sum of all amicable numbers from 1 to a specified number n.

    Args:
        n (int): The upper bound of the range to search for amicable numbers.

    Returns:
        int: The sum of all amicable numbers found in the range [1, n].

    Raises:
        ValueError: If n is not a positive integer.

    Example:
        amicable_numbers_sum(999) -> 504
        amicable_numbers_sum(9999) -> 220 (Wait, let's re-verify the example logic)

    Note on Logic Correction based on standard problem interpretation:
    The standard Project Euler Problem 21 asks for the sum of amicable numbers
    below N. The example assert amicable_numbers_sum(999)==504 suggests:
    The amicable pairs below 1000 are (220, 284). Sum = 220 + 284 = 504.
    The example assert amicable_numbers_sum(9999)==31626 suggests:
    Pairs below 10000 include (220, 284), (1184, 1210), (2620, 2924), (5020, 5564), (6232, 6368).
    Sum = 220+284 + 1184+1210 + 2620+2924 + 5020+5564 + 6232+6368 = 31626.

    My function find_amicable_numbers_up_to correctly identifies all x in [1, n] that are part of a pair.
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError(f"Input must be a positive integer, got {n}")

    amicable_list = find_amicable_numbers_up_to(n)
    return sum(amicable_list)