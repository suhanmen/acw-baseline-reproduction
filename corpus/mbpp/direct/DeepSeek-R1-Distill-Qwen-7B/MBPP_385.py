def get_perrin(n):
    if n == 0:
        return 3
    elif n == 1:
        return 0
    elif n == 2:
        return 3
    else:
        return get_perrin(n - 1) + get_perrin(n - 3)