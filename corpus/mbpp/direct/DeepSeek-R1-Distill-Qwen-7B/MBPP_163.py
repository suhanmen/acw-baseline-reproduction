def area_polygon(n, s):
    import math
    area = (n * s**2) / (4 * math.tan(math.pi / n))
    return round(area, 12)