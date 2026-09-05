import math

def sum(a: int, b: int) -> int:
    """
    Finds the sum of common divisors of two given numbers.
    """
    common_sum = 0
    # The greatest common divisor limits the search range for common divisors
    gcd_val = math.gcd(a, b)

    # Iterate from 1 to the square root of the GCD
    for i in range(1, int(math.sqrt(gcd_val)) + 1):
        if gcd_val % i == 0:
            common_sum += i
            # If the divisor is not the square root, add the paired divisor
            if i*i != gcd_val:
                common_sum += gcd_val // i

    return common_sum