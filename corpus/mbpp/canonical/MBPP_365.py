def count_Digit(n):
    count = 0
    while n != 0:
        n //= 10
        count += 1
    return count