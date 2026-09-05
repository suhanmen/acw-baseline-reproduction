def areEquivalent(num1, num2):
    """
    Checks whether the sum of proper divisors of two numbers is the same.
    A proper divisor of a number is a positive integer divisor of that number,
    excluding the number itself.
    """
    def sum_proper_divisors(n):
        if n <= 1:
            return 0
        total = 1
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                total += i
                complement = n // i
                if complement != i:
                    total += complement
        return total

    return sum_proper_divisors(num1) == sum_proper_divisors(num2)