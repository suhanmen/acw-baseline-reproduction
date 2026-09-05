def amicable_numbers_sum(n):
    """
    Calculates the sum of all amicable numbers from 1 up to n.
    An amicable number is a number whose proper divisors sum up to another 
    number, which in turn has proper divisors that sum up to the original number.
    """
    def get_sum_of_proper_divisors(num):
        if num < 2:
            return 0
        total = 1
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                total += i
                complement = num // i
                if complement != i:
                    total += complement
        return total

    amicable_sum = 0
    # Optimization: pre-calculate divisor sums to avoid redundant calculations
    # However, for the given constraints (9999), direct calculation is sufficient.
    # We need to check if d is amicable: 
    # Let s(d) = sum of proper divisors of d.
    # d is amicable if s(d) = m AND s(m) = d AND d != m.

    # To optimize, we can pre-calculate sum of divisors for all numbers up to n.
    # Since m can be larger than n, we need a strategy.
    # Let's use a dictionary to cache sums of divisors.
    divisor_sums = {}

    for i in range(1, n + 1):
        # Calculate sum of proper divisors for i
        if i not in divisor_sums:
            divisor_sums[i] = get_sum_of_proper_divisors(i)

        s_i = divisor_sums[i]

        if s_i > 1 and s_i != i:
            # Now we need s(s_i)
            if s_i not in divisor_sums:
                divisor_sums[s_i] = get_sum_of_proper_divisors(s_i)

            s_si = divisor_sums[s_i]

            if s_si == i:
                amicable_sum += i

    return amicable_sum