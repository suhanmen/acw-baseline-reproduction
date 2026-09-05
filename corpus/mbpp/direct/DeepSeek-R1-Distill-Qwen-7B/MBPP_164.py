def areEquivalent(a, b):
    def sum_of_divisors(n):
        if n <= 0:
            return 0
        sqrt_n = int(n**0.5)
        total = 0
        for i in range(1, sqrt_n + 1):
            if n % i == 0:
                if i == n // i:
                    total += i
                else:
                    total += i + n // i
        return total

    return sum_of_divisors(a) == sum_of_divisors(b)