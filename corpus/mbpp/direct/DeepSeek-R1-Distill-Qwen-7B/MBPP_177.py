def answer(lower, upper):
    for a in range(lower, upper + 1):
        for b in range(a + 1, upper + 1):
            if (a * b) // gcd(a, b) >= lower and (a * b) // gcd(a, b) <= upper:
                return (a, b)
    return None

from math import gcd