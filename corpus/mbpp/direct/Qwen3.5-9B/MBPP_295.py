def sum_div(n: int) -> int:
    if n <= 0:
        raise ValueError("n must be a positive integer")
    total = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
        i += 1
    if n == 1:
        return 1
    return total