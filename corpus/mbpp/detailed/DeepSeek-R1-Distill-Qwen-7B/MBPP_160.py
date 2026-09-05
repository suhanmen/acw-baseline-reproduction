def solution(a, b, n):
    if a == 0 and b == 0:
        return ('x = ', 0, ', y = ', 0) if n == 0 else 'No solution'

    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    def extended_gcd(x, y):
        if x == 0:
            return (y, 0, 1)
        else:
            g, y1, x1 = extended_gcd(y % x, x)
            return (g, x1 - (y // x) * y1, y1)

    g, x0, y0 = extended_gcd(a, b)

    if n % g != 0:
        return 'No solution'

    x_particular = x0 * (n // g)
    y_particular = y0 * (n // g)

    return ('x = ', x_particular, ', y = ', y_particular)