def areEquivalent(num1: int, num2: int) -> bool:
    def sum_of_divisors(n: int) -> int:
        if n <= 1:
            return 0
        total = 1  # 1 is always a divisor
        limit = int(n ** 0.5)
        for i in range(2, limit + 1):
            if n % i == 0:
                total += i
                if i != n // i:
                    total += n // i
        return total

    return sum_of_divisors(num1) == sum_of_divisors(num2)