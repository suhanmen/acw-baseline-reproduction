def get_maxgold(grid, n, m):
    if not grid or n <= 0 or m <= 0:
        return 0

    max_gold = [[0] * m for _ in range(n)]

    for j in range(m):
        max_gold[0][j] = grid[0][j]

    for i in range(1, n):
        max_gold[i][0] = max_gold[i-1][0] + grid[i][0]
        for j in range(1, m):
            max_gold[i][j] = grid[i][j] + max(max_gold[i-1][j], max_gold[i-1][j-1], max_gold[i-1][j+1] if j+1 < m else 0)

    return max(max_gold[n-1])


def get_maxgold(grid, n, m):
    if not grid or n <= 0 or m <= 0:
        return 0

    max_gold = [[0] * m for _ in range(n)]

    for j in range(m):
        max_gold[0][j] = grid[0][j]

    for i in range(1, n):
        max_gold[i][0] = max_gold[i-1][0] + grid[i][0]
        for j in range(1, m):
            max_gold[i][j] = grid[i][j] + max(max_gold[i-1][j], max_gold[i-1][j-1], max_gold[i-1][j+1] if j+1 < m else 0)

    return max(max_gold[n-1])