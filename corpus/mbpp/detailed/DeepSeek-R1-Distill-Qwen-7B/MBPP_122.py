def smartNumber(n):
    """
    Find the n-th smart number.

    Requirements:
    - Must handle all edge cases.
    - Returns the smallest number that can be expressed as the sum of distinct prime cubes in exactly one way.
    - The result must be exactly matching the required n-th position.
    """
    # Generate list of prime numbers up to a certain limit
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes = []
    current = 2
    while len(primes) < 100:  # Generate enough primes to compute necessary sums
        if is_prime(current):
            primes.append(current)
        current += 1

    # Compute prime cubes
    prime_cubes = [p ** 3 for p in primes]

    # Generate all possible sums of distinct prime cubes
    sums = []
    for mask in range(1, 1 << len(prime_cubes)):
        total = 0
        for i in range(len(prime_cubes)):
            if mask & (1 << i):
                total += prime_cubes[i]
        sums.append(total)

    # Identify unique sums (smart numbers)
    unique_sums = sorted(list(set(sums)))

    # Since we need sums that can be formed in exactly one way, we keep track of counts
    from collections import defaultdict
    sum_counts = defaultdict(int)
    for s in sums:
        sum_counts[s] += 1

    # Filter sums with count exactly 1
    smart_numbers = [s for s in unique_sums if sum_counts[s] == 1]

    # Sort the smart numbers
    smart_numbers.sort()

    # Return the n-th smart number (1-based index)
    return smart_numbers[n-1]