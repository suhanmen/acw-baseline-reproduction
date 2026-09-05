def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True

def skjkasdkd(lst):
    primes = [x for x in lst if x > 1 and is_prime(x)]
    if not primes:
        return 0
    largest_prime = max(primes)
    return sum(int(digit) for digit in str(largest_prime))