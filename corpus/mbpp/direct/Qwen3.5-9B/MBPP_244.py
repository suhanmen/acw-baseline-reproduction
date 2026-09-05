import math

def next_Perfect_Square(n: int) -> int:
    root = int(math.isqrt(n))
    if root * root <= n:
        root += 1
    return root * root