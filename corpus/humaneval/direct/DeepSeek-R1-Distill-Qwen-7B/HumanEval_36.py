def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for i in range(1, n):
        if i % 11 == 0 or i % 13 == 0:
            num_str = str(i)
            count += num_str.count('7')
    return count

# Example test cases
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3