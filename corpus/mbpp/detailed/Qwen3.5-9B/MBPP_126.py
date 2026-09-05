def sum_common_divisors(a, b):
    """
    Calculate the sum of all common divisors of two given integers.

    Parameters:
    a (int): First integer
    b (int): Second integer

    Returns:
    int: The sum of all common divisors of a and b.

    Raises:
    TypeError: If either input is not an integer.
    ValueError: If either input is less than or equal to zero.
    """
    # Validate input types explicitly
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both inputs must be integers.")

    # Validate input values (divisors are typically defined for positive integers >= 1)
    # Based on the problem's implicit context and standard divisor problems, 
    # we assume positive integers > 0. The examples use positive numbers.
    if a <= 0 or b <= 0:
        raise ValueError("Both inputs must be strictly positive integers.")

    # Calculate the Greatest Common Divisor (GCD) first.
    # Common divisors of a and b are exactly the divisors of gcd(a, b).
    # We use Euclid's algorithm for efficiency and robustness.
    gcd_value = _compute_gcd(a, b)

    # Calculate the sum of divisors of the gcd_value.
    # The function will iterate up to the square root of the gcd_value 
    # to find all pairs of divisors efficiently.
    divisor_sum = _sum_divisors_of_number(gcd_value)

    return divisor_sum

def _compute_gcd(a, b):
    """
    Compute the Greatest Common Divisor (GCD) of two positive integers
    using Euclid's algorithm.

    Parameters:
    a (int): First positive integer
    b (int): Second positive integer

    Returns:
    int: The GCD of a and b.
    """
    while b != 0:
        # Store the remainder of the division
        temp_value = b
        # Update b to be the remainder of a / b
        b = a % b
        # Update a to be the previous value of b
        a = temp_value
    return a

def _sum_divisors_of_number(n):
    """
    Calculate the sum of all positive divisors of a given positive integer n.

    This function iterates from 1 up to the square root of n.
    For every number i that divides n evenly:
    - i is a divisor.
    - n // i is the corresponding paired divisor.
    - We add both to the sum, ensuring not to double count if i == n // i.

    Parameters:
    n (int): A positive integer.

    Returns:
    int: The sum of all divisors of n.
    """
    total_sum = 0

    # Loop from 1 up to the square root of n (inclusive)
    # We use integer arithmetic. i * i <= n ensures we stop at the sqrt.
    i = 1
    while i * i <= n:
        remainder_value = n % i

        # Check if i is a divisor of n
        if remainder_value == 0:
            # i is definitely a divisor
            total_sum += i

            # Check if the paired divisor (n // i) is different from i
            paired_divisor = n // i
            if paired_divisor != i:
                total_sum += paired_divisor

        # Move to the next integer
        i += 1

    return total_sum