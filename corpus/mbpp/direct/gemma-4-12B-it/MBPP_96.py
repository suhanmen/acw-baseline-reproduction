def divisor(n: int) -> int:
    """
    Finds the number of divisors of a given integer n.
    """
    if n <= 0:
        return 0
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if i*i == n:
                count += 1
            else:
                count += 2
    return count

if __name__ == "__main__":
    assert divisor(15) == 4 
    assert divisor(12) == 6
    assert divisor(9) == 3