def count_Primes_nums(n: int) -> int:
    """
    Counts the number of prime numbers less than a given non-negative number n.
    Uses the Sieve of Eratosthenes algorithm.
    """
    if n <= 2:
        return 0

    # Create a boolean array "prime[0..n-1]" and initialize
    # all entries it as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true.
    primes = [True] * n
    primes[0] = primes[1] = False

    for p in range(2, int(n**0.5) + 1):
        if primes[p]:
            # Update all multiples of p starting from p*p
            for i in range(p * p, n, p):
                primes[i] = False

    return sum(primes)

if __name__ == "__main__":
    assert count_Primes_nums(5) == 2
    assert count_Primes_nums(10) == 4
    assert count_Primes_nums(100) == 25