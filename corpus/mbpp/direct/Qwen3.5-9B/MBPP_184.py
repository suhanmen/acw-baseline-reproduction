def greater_specificnum(lst: list, num: int) -> bool:
    return any(x > num for x in lst)