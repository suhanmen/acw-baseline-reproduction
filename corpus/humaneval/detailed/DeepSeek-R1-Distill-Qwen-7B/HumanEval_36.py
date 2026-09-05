def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    if n <= 0:
        return 0

    def count_seven(number):
        """Count the number of '7's in the digits of the given number."""
        return str(number).count('7')

    count = 0
    for i in range(1, n):
        if i % 11 == 0 or i % 13 == 0:
            count += count_seven(i)

    return count

# Example outputs:
print(fizz_buzz(50))   # 0
print(fizz_buzz(78))   # 2
print(fizz_buzz(79))   # 3
print(fizz_buzz(143))  # 4