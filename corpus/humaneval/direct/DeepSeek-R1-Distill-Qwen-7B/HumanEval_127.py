def intersection(interval1, interval2):
    # Calculate the intersection start and end
    start_int = max(interval1[0], interval2[0])
    end_int = min(interval1[1], interval2[1])

    # If no intersection, return "NO"
    if start_int > end_int:
        return "NO"

    # Calculate the length of the intersection
    length = end_int - start_int

    # Function to check if a number is prime
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    # Check if the length is a prime number
    return "YES" if is_prime(length) else "NO"