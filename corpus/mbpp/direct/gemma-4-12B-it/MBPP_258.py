def count_odd(numbers):
    return len(list(filter(lambda x: x % 2 != 0, numbers)))