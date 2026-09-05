def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    count = 0
    temp = a
    # We iterate through potential factors
    # Since a < 100, prime factors are small
    for i in range(2, 100):
        while temp % i == 0 and is_prime(i):
            temp //= i
            count += 1
            if count > 3:
                return False

    return count == 3