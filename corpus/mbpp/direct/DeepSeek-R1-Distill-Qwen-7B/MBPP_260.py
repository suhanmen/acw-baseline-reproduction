import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def newman_prime(n):
    s = [1, 1]
    while len(s) < n:
        next_val = 2 * s[-1] + s[-2]
        s.append(next_val)
        if is_prime(next_val):
            pass
    return s[n-1]