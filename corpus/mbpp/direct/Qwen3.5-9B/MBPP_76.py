def count_Squares(width, height):
    return sum((width - i) * (height - i) for i in range(min(width, height)))