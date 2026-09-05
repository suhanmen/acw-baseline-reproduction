def count_Num(n):
    count = 0
    for i in range(1, n+1):
        if (i >> (n-1)) & 1:
            count += 1
    return count