def solution(a, b, n):
    def gcd_extended(a, b):
        if a == 0:
            return b, 0, 1
        g, x1, y1 = gcd_extended(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return g, x, y

    g, x0, y0 = gcd_extended(a, b)
    if n % g != 0:
        return 'No solution'
    x = x0 * (n // g)
    y = y0 * (n // g)
    return ('x = ', x, ', y = ', y)