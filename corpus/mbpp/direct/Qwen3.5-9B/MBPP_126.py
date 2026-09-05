def sum_divisors(a: int, b: int) -> int:
    def gcd(x: int, y: int) -> int:
        while y:
            x, y = y, x % y
        return x

    g = gcd(a, b)
    result = 0
    for i in range(1, int(g**0.5) + 1):
        if g % i == 0:
            result += i
            if i != g // i:
                result += g // i
    return result