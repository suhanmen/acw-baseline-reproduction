def check(n):
    reversed_n = int(str(n)[::-1])
    return n == 2 * reversed_n - 1

assert check(70) == False
assert check(23) == False
assert check(73) == True