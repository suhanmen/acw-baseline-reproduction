def odd_Days(y):
    month_days = [31, 28 + ((y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)), 31, 30,
                  31, 30, 31, 31, 30, 31, 30, 31]
    total = 0
    for i in range(12):
        if i == 0:
            prev = 31
        else:
            prev = month_days[i - 1]
        if prev % 2 != 0:
            total += prev
        month_days[i] += prev // 2
    return total

assert odd_Days(100) == 5
assert odd_Days(50) == 6
assert odd_Days(75) == 2