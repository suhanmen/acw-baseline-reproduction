import math

def divisor(n: int) -> int:
    if n <= 0:
        raise ValueError("n must be a positive integer")
    if n == 1:
        return 1
    count = 0
    limit = int(math.isqrt(n))
    for i in range(1, limit + 1):
        if n % i == 0:
            if i * i == n:
                count += 1
            else:
                count += 2
    return count