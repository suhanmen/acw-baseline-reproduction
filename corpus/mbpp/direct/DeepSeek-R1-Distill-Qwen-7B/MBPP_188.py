def prod_Square(n):
    from math import isqrt
    if n < 0:
        return False
    if n == 0:
        return False
    for i in range(2, isqrt(n) + 1):
        exponent = 0
        while n % i == 0:
            exponent += 1
            n = n // i
        if exponent % 2 != 0:
            return False
    if n > 1:
        if 1 % 2 != 0:
            return False
    return True

# Test cases
assert prod_Square(25) == False  # 25 = 5^2, but it cannot be expressed as product of two squares
assert prod_Square(30) == False  # 30 = 2 * 3 * 5, all primes have odd exponents
assert prod_Square(16) == True   # 16 = 4^2, can be expressed as 4*4