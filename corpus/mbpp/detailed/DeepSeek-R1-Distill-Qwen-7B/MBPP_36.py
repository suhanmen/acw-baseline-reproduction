def find_Nth_Digit(numerator, denominator, n):
    # Input validation
    if denominator == 0:
        raise ValueError("Denominator cannot be zero.")
    if n <= 0:
        raise ValueError("n must be a positive integer.")
    if numerator >= denominator:
        raise ValueError("numerator must be less than denominator.")

    current = numerator
    position = 0

    while position < n:
        current *= 10
        digit = current // denominator
        current = current % denominator * 10
        position += 1

    return digit