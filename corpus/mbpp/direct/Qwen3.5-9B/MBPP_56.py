def check(n: int) -> bool:
    rev = int(str(n)[::-1])
    return n == 2 * rev - 1