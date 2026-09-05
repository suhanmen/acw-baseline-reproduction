def square_Sum(n):
    # Validate the input
    if not isinstance(n, int) or n < 1:
        return 0

    # Generate the first n odd numbers
    odd_numbers = [2*i + 1 for i in range(n)]

    # Compute the sum of their squares
    sum_of_squares = sum(num ** 2 for num in odd_numbers)

    return sum_of_squares

# Test cases
assert square_Sum(2) == 10
assert square_Sum(3) == 35
assert square_Sum(4) == 84