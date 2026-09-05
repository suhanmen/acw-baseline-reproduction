import heapq
from collections import deque

def minPath(grid, k):
    """
    Finds the minimum lexicographical path of length k in a grid.
    """
    n = len(grid)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Priority queue: each element is (path, current_value, current_row, current_col)
    heap = []
    visited = set()

    # Initial step: add all starting positions to the heap and mark them as visited
    for i in range(n):
        for j in range(n):
            heapq.heappush(heap, (grid[i][j], i, j))
            visited.add((i, j))

    # To store the best path found so far
    best_path = None

    # BFS processing each level
    while heap:
        current_val, i, j = heapq.heappop(heap)
        path = [current_val]
        visited.add((i, j))

        # If path length is k, check if it's the best so far
        if len(path) == k:
            if best_path is None or path < best_path:
                best_path = path.copy()
            continue

        # Explore all directions
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n:
                next_val = grid[ni][nj]
                next_path = path + [next_val]
                if (ni, nj) not in visited:
                    heapq.heappush(heap, (next_val, ni, nj))
                    visited.add((ni, nj))

    return best_path