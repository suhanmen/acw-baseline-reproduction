def max_Prime_Factors(n):
    if n <= 1:
        return None  # No prime factors for 0, 1, or negative numbers
    largest_prime = 1
    # Check divisibility by 2
    while n % 2 == 0:
        largest_prime = 2
        n = n // 2
    # Check for odd factors
    i = 3
    while i * i <= n:
        while n % i == 0:
            largest_prime = i
            n = n // i
        i += 2
    # If remaining n is a prime number
    if n > 2:
        largest_prime = n
    return largest_prime

# Example usage and assertions
print(max_Prime_Factors(15))  # Output: 5
print(max_Prime_Factors(6))   # Output: 3
print(max_Prime_Factors(2))   # Output: 2