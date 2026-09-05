def count_odd(lst):
    return sum(1 for num in lst if num % 2 != 0)