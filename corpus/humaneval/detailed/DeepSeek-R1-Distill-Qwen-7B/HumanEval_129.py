import heapq
from collections import deque

def minPath(grid, k):
    """
    Given a grid with N rows and N columns (N >= 2) and a positive integer k, 
    each cell of the grid contains a value. Every integer in the range [1, N * N]
    inclusive appears exactly once on the cells of the grid.

    You have to find the minimum path of length k in the grid. You can start
    from any cell, and in each step you can move to any of the neighbor cells,
    in other words, you can go to cells which share an edge with you current
    cell.
    The minimum path is determined based on lexicographical order.

    Args:
        grid: A 2D list representing the grid.
        k: The required length of the path.

    Returns:
        An ordered list of the values on the cells that form the minimum path.

    Raises:
        ValueError: If grid is empty or has less than 2 rows, or k is larger than the grid size squared.
    """
    # Handle edge cases based on problem constraints
    n = len(grid)
    if n == 0 or k > n * n:
        raise ValueError("Invalid input")
    if k == 1:
        min_val = min(val for row in grid for val in row)
        positions = [(i, j) for i, row in enumerate(grid) for j, val in enumerate(row) if val == min_val]
        # Return the lexicographically smallest path of length 1
        return [min_val]

    # Directions for moving up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Priority queue: (current_path, current_row, current_col)
    # We use a min-heap to always expand the smallest current path first
    heap = []

    # Initialize the priority queue with all possible starting positions
    for i in range(n):
        for j in range(n):
            path = [grid[i][j]]
            heapq.heappush(heap, (path, i, j))

    # Visited structure to avoid revisiting the same cell in a path
    # Visited is a dictionary where key is (row, col) and value is the length of the path
    # This helps in avoiding infinite loops and redundant processing
    visited = {}

    while heap:
        current_path, i, j = heapq.heappop(heap)
        current_len = len(current_path)

        # If we have found a path of length k, return it immediately as it's the smallest
        if current_len == k:
            return current_path

        # If we've already processed a path to this cell that's longer or equal, skip
        if (i, j) in visited and len(current_path) >= visited[(i, j)]:
            continue

        # Update the visited for this cell
        visited[(i, j)] = len(current_path)

        # Explore all four directions
        for dx, dy in directions:
            ni, nj = i + dx, j + dy
            if 0 <= ni < n and 0 <= nj < n:
                # Create the new path by adding the next cell's value
                new_path = current_path.copy()
                new_path.append(grid[ni][nj])

                # If this is the first cell we're visiting, add it to the heap
                if (ni, nj) not in visited or len(new_path) < visited[(ni, nj)]:
                    heapq.heappush(heap, (new_path, ni, nj))

    # If no path found, return an empty list (shouldn't happen due to problem constraints)
    return []