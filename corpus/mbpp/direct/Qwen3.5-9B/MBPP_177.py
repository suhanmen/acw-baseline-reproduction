import math
from functools import reduce

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def answer(low, high):
    for i in range(low, high + 1):
        for j in range(i + 1, high + 1):
            l = lcm(i, j)
            if low <= l <= high:
                return (i, j)
    return None