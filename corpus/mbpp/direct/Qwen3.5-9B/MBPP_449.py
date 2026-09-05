import math

def check_Triangle(x1, y1, x2, y2, x3, y3):
    def distance(xa, ya, xb, yb):
        return math.sqrt((xa - xb) ** 2 + (ya - yb) ** 2)

    a = distance(x1, y1, x2, y2)
    b = distance(x2, y2, x3, y3)
    c = distance(x3, y3, x1, y1)

    sides = [a, b, c]
    if any(s == 0 for s in sides):
        return 'No'

    sides.sort()
    if sides[0] + sides[1] <= sides[2]:
        return 'No'

    return 'Yes'