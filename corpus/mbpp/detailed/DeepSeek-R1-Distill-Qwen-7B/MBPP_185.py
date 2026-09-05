def parabola_focus(a, b, c):
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be zero for a parabola.")
    h = -b / (2 * a)
    k = c - (b ** 2) / (4 * a)
    p = 1 / (4 * a)
    focus_x = h
    focus_y = k + p
    return (focus_x, focus_y)

# Test cases
assert parabola_focus(5, 3, 2) == (-0.3, 1.6)
assert parabola_focus(9, 8, 4) == (-0.4444444444444444, 2.25)
assert parabola_focus(2, 4, 6) == (-1.0, 4.125)