from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    try:
        if not isinstance(n, int):
            raise ValueError("Input must be an integer.")
        if n < 0:
            raise ValueError("Negative numbers cannot be factorized into primes.")
        if n == 1:
            return []

        factors = []
        divisor = 2
        temp = n

        while temp > 1:
            if temp % divisor == 0:
                factors.append(divisor)
                temp //= divisor
            else:
                divisor += 1
            # Early exit if divisor exceeds the square root of temp
            if divisor * divisor > temp:
                if temp > 1:
                    factors.append(temp)
                break

        return factors

    except ValueError as e:
        raise
    except Exception as e:
        raise ValueError(f"Invalid input: {e}")