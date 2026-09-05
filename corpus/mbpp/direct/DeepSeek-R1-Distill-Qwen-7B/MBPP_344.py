def count_Odd_Squares(a, b):
    start = a ** 0.5
    start = math.ceil(start)
    end = math.sqrt(b)
    end = math.floor(end)
    return end - start + 1 if end >= start else 0