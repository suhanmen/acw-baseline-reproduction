def count_With_Odd_SetBits(n):
    count = 0
    for i in range(n + 1):
        if bin(i).count('1') % 2 != 0:
            count += 1
    return count