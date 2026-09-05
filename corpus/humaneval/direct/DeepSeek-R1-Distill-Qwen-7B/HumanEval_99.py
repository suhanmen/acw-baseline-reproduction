def closest_integer(value):
    number = float(value)
    if abs(number) - int(abs(number)) == 0.5:
        if number < 0:
            return -int(number) - 1
        else:
            return int(number) + 1
    else:
        return round(number)