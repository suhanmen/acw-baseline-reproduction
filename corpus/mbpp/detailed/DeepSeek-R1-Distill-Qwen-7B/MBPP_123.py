def amicable_numbers_sum(n):
    def sum_proper_divisors(num):
        if num <= 1:
            return 0
        divisors_sum = 1  # 1 is a proper divisor
        sqrt_num = int(num ** 0.5)
        for i in range(2, sqrt_num + 1):
            if num % i == 0:
                divisors_sum += i
                other_divisor = num // i
                if other_divisor != i and other_divisor != num:
                    divisors_sum += other_divisor
        return divisors_sum

    amicable = set()
    for number in range(1, n + 1):
        sum1 = sum_proper_divisors(number)
        if sum1 != number and sum_proper_divisors(sum1) == number:
            amicable.add(number)

    return sum(amicable)

# Test cases
assert amicable_numbers_sum(999) == 504
assert amicable_numbers_sum(9999) == 31626
assert amicable_numbers_sum(99) == 0