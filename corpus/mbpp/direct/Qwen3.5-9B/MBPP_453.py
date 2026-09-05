def sumofFactors(n):
    if n <= 0:
        return 0
    total = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            if i % 2 == 0:
                total += i
            if i * i != n:
                other = n // i
                if other % 2 == 0:
                    total += other
        i += 1
    return total