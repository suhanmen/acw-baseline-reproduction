import math

def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. """

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    if a <= 0:
        return False

    prime_factors = []
    divisor = 2

    while divisor * divisor <= a:
        while a % divisor == 0:
            prime_factors.append(divisor)
            a = a // divisor
        divisor += 1

    if a > 1:
        prime_factors.append(a)

    return len(prime_factors) == 3