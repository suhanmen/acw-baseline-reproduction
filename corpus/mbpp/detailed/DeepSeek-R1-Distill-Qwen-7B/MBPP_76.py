def count_Squares(m, n):
    # Validate inputs
    if m < 1 or n < 1:
        return -1

    max_square = min(m, n)
    total_squares = 0

    for k in range(1, max_square + 1):
        count = (m - k + 1) * (n - k + 1)
        total_squares += count

    return total_squares

# Test cases
print(count_Squares(4, 3))  # Expected output: 20
print(count_Squares(2, 2))  # Expected output: 5
print(count_Squares(1, 1))  # Expected output: 1