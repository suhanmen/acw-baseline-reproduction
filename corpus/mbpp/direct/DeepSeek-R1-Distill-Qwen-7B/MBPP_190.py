def count_Intgral_Points(x1, y1, x2, y2):
    if x1 >= x2 or y1 >= y2:
        return 0
    return (x2 - x1 - 1) * (y2 - y1 - 1)