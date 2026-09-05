def sum_div(n):
    if n < 1:
        return 0
    sum_divisors = 1  # 1 is a divisor of all numbers except 0
    sqrt_n = int(n ** 0.5)
    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            if i == n // i:
                sum_divisors += i
            else:
                sum_divisors += i + n // i
    return sum_divisors