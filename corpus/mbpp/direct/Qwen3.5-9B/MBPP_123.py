def amicable_numbers_sum(limit: int) -> int:
    # Precompute sum of proper divisors for all numbers up to limit
    # sum_div[i] will store the sum of proper divisors of i
    sum_div = [0] * (limit + 1)

    # For each number i from 1 to limit, add i to sum_div[j] for all multiples j of i
    for i in range(1, limit + 1):
        for j in range(2 * i, limit + 1, i):
            sum_div[j] += i

    amicable_set = set()

    for i in range(1, limit + 1):
        j = sum_div[i]
        if j > i and j <= limit and sum_div[j] == i:
            amicable_set.add(i)

    return sum(amicable_set)