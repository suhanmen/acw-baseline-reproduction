def sum_div(n):
    if n <= 1:
        return 0
    total = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            total += i
            if i*i != n:
                total += n // i
    return total - n