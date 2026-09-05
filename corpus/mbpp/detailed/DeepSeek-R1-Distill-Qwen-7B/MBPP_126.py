def sum_common_divisors(a, b):
    # Handle cases where either number is zero
    if a == 0 or b == 0:
        return 0

    # Make sure a is the smaller number
    if a > b:
        a, b = b, a

    # Function to calculate the greatest common divisor (GCD) using Euclidean algorithm
    def gcd(x, y):
        while y != 0:
            x, y = y, x % y
        return x

    # Calculate GCD of a and b
    greatest_common = gcd(a, b)

    # If GCD is zero, return 0 (though this shouldn't happen due to earlier check)
    if greatest_common == 0:
        return 0

    # Function to find all divisors of a number
    def find_divisors(n):
        divisors = set()
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                divisors.add(i)
                divisors.add(n // i)
        return divisors

    # Find all divisors of the GCD
    divisors = find_divisors(greatest_common)

    # Sum the divisors
    return sum(divisors)