def is_coprime(a, b):
    # Handle edge case where either number is 0
    if a == 0 or b == 0:
        return False

    # Use the Euclidean algorithm to find GCD
    def gcd(x, y):
        while y != 0:
            x, y = y, x % y
        return x

    # Calculate GCD of a and b
    greatest_common_divisor = gcd(a, b)

    # Check if GCD is 1
    return greatest_common_divisor == 1