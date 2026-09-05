def sum(n, m):
    # Find the greatest common divisor (gcd) of n and m
    import math
    gcd = math.gcd(n, m)

    # If gcd is 1, return 1 as there are no common divisors other than 1
    if gcd == 1:
        return 1

    # Find all divisors of gcd
    divisors = set()
    for i in range(1, int(gcd**0.5) + 1):
        if gcd % i == 0:
            divisors.add(i)
            divisors.add(gcd // i)

    # Sum all the divisors
    return sum(divisors)