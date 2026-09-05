def lateralsurface_cuboid(a, b, c):
    return 2 * (a * c + b * c)

assert lateralsurface_cuboid(8, 5, 6) == 156
assert lateralsurface_cuboid(7, 9, 10) == 320
assert lateralsurface_cuboid(10, 20, 30) == 1800