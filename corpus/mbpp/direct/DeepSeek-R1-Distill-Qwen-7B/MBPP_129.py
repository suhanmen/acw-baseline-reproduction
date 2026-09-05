def magic_square(arr):
    # Check if the input is a square matrix
    n = len(arr)
    if any(len(row) != n for row in arr):
        return False

    # Calculate the magic constant
    magic_constant = n * (n * (n ** 2) // 2) // n

    # Check all rows
    for row in arr:
        if sum(row) != magic_constant:
            return False

    # Check all columns
    for col in range(n):
        if sum(arr[row][col] for row in range(n)) != magic_constant:
            return False

    # Check main diagonal
    if sum(arr[i][i] for i in range(n)) != magic_constant:
        return False

    # Check anti-diagonal
    if sum(arr[i][n - 1 - i] for i in range(n)) != magic_constant:
        return False

    return True