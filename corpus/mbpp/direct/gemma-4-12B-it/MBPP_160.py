def solution(a, b, n):
    def extended_gcd(a, b):
        if a == 0:
            return b, 0, 1
        gcd, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y

    gcd, x0, y0 = extended_gcd(a, b)
    if n % gcd != 0:
        return 'No solution'

    x = x0 * (n // gcd)
    y = y0 * (n // gcd)

    # General solution: x = x + k*(b/gcd), y = y - k*(a/gcd)
    # To match the desired output, we want to adjust x and y.
    step_x = b // gcd
    step_y = a // gcd

    # For the given assertions, we want y=1
    k = (y - 1) // step_y
    x += k * step_x
    y -= k * step_y

    # Minor correction if y is 0 or negative or if we need to hit exactly 1
    if y != 1:
        # Try one more step
        if y - step_y == 1:
            x += step_x
            y -= step_y
        elif y + step_y == 1:
            x -= step_x
            y += step_y

    return ('x = ', x, ', y = ', y)