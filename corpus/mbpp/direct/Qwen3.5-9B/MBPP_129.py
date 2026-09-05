def magic_square_test(square):
    n = len(square)
    if n == 0:
        return False
    for row in square:
        if len(row) != n:
            return False

    numbers = set()
    for row in square:
        for val in row:
            if not isinstance(val, int) or val < 1 or val > n * n:
                return False
            if val in numbers:
                return False
            numbers.add(val)
    if numbers != set(range(1, n * n + 1)):
        return False

    target = n * (n * n + 1) // 2

    for row in square:
        if sum(row) != target:
            return False

    for col_idx in range(n):
        col_sum = sum(square[row_idx][col_idx] for row_idx in range(n))
        if col_sum != target:
            return False

    diag1_sum = sum(square[i][i] for i in range(n))
    diag2_sum = sum(square[i][n - 1 - i] for i in range(n))
    if diag1_sum != target or diag2_sum != target:
        return False

    return True