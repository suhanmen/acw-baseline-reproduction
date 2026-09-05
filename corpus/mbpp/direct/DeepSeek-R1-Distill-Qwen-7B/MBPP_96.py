def divisor(n):
    if n < 1:
        return 0
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if i * i == n:
                count += 1
            else:
                count += 2
    return count