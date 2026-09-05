def get_perrin(n):
    if n == 0:
        return 3
    elif n == 1 or n == 2:
        return 0
    else:
        return get_perrin(n - 2) + get_perrin(n - 3)