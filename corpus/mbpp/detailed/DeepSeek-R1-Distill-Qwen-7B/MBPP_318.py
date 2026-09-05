def max_volume(n):
    if n < 3:
        return 0
    a = n // 3
    b = a
    c = n - a * 2
    if c <= 0:
        return 0
    volume = a * b * c
    # Check adjacent possibilities in case the initial split doesn't give max
    # Case 1: a-1, a, c+2
    if a > 0:
        volume1 = (a - 1) * (a) * (c + 2)
        if volume1 > volume:
            volume = volume1
    # Case 2: a+1, a, c-2
    if c > 0:
        volume2 = (a + 1) * (a) * (c - 2)
        if volume2 > volume:
            volume = volume2
    # Case 3: a, a+1, c-1
    if c > 1:
        volume3 = a * (a + 1) * (c - 1)
        if volume3 > volume:
            volume = volume3
    # Case 4: a, a-1, c+1
    if a > 1:
        volume4 = a * (a - 1) * (c + 1)
        if volume4 > volume:
            volume = volume4
    return volume

# Test the function with the provided assertions
assert max_volume(8) == 18
assert max_volume(4) == 2
assert max_volume(1) == 0