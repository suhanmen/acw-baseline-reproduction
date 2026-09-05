def sumofFactors(n):
    if n == 0:
        return 0
    total = 1  # since 1 is a factor for all numbers except 0
    i = 2
    while i * i <= n:
        if n % i == 0:
            current_factor = i
            current_sum = 1  # since i^0 is 1
            while n % current_factor == 0:
                current_sum += current_factor
                n = n // current_factor
            total *= current_sum
        i += 1
    if n > 1:
        total *= (1 + n)
    return total

# Test cases
assert sumofFactors(18) == 26
assert sumofFactors(30) == 48
assert sumofFactors(6) == 8