def largest_neg(lst):
    largest = None
    for num in lst:
        if num < 0 and (largest is None or num > largest):
            largest = num
    return largest