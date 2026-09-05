def count_Intgral_Points(x_min, y_min, x_max, y_max):
    count = 0
    for x in range(x_min, x_max + 1):
        for y in range(y_min, y_max + 1):
            count += 1
    return count