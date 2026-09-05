from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    """
    Given a grid with N rows and N columns (N >= 2) and a positive integer k, 
    each cell of the grid contains a value. Every integer in the range [1, N * N]
    inclusive appears exactly once on the cells of the grid.

    You have to find the minimum path of length k in the grid. You can start
    from any cell, and in each step you can move to any of the neighbor cells,
    in other words, you can go to cells which share an edge with you current
    cell.
    Please note that a path of length k means visiting exactly k cells (not
    necessarily distinct).
    You CANNOT go off the grid.
    A path A (of length k) is considered less than a path B (of length k) if
    after making the ordered lists of the values on the cells that A and B go
    through (let's call them lst_A and lst_B), lst_A is lexicographically less
    than lst_B, in other words, there exist an integer index i (1 <= i <= k)
    such that lst_A[i] < lst_B[i] and for any j (1 <= j < i) we have
    lst_A[j] = lst_B[j].
    It is guaranteed that the answer is unique.
    Return an ordered list of the values on the cells that the minimum path go through.
    """
    # --- Input Validation ---
    if not grid or not grid[0]:
        raise ValueError("Grid must not be empty.")

    rows = len(grid)
    cols = len(grid[0])

    if rows != cols or rows < 2:
        raise ValueError("Grid must be square and N >= 2.")

    if not isinstance(k, int) or k <= 0:
        raise ValueError("k must be a positive integer.")

    # --- Data Preparation ---
    # Map value to (row, col) for efficient O(1) lookup of starting points
    # Since every number 1 to N*N appears exactly once, this is a perfect map.
    val_to_pos = {}
    for r in range(rows):
        for c in range(cols):
            val_to_pos[grid[r][c]] = (r, c)

    # --- Strategy ---
    # To find the lexicographically smallest path:
    # 1. The first element of the path must be the smallest possible value 
    #    available in the grid that can initiate a valid path of length k.
    #    Since any cell can start a path and we can move back and forth, 
    #    the first element is simply the smallest value in the grid (which is 1).
    # 2. For each subsequent step, we want to choose the smallest possible 
    #    neighbor of the current cell.
    # 3. However, there's a catch: just choosing the smallest neighbor at 
    #    every step might not be optimal if a slightly larger neighbor leads 
    #    to a much smaller neighbor later.
    #    BUT, because we can move back and forth (e.g., 1 -> 2 -> 1), 
    #    the best strategy is greedy. At each step, we want the smallest neighbor.
    #    If the smallest neighbor is 'x', we go there. If we can go to an even 
    #    smaller neighbor from 'x' in the next step, that's what we want.
    #    Since we can move back to the previous cell, the best "local" move is 
    #    always the best "global" move because we can always oscillate 
    #    between the two smallest adjacent cells.

    # Let's re-evaluate: To minimize the sequence lexicographically:
    # Path = [p1, p2, p3, ..., pk]
    # We want smallest p1. That is always 1.
    # Then we want smallest p2 such that p2 is a neighbor of p1.
    # Then we want smallest p3 such that p3 is a neighbor of p2.
    # This greedy approach works because at any step i, choosing the smallest 
    # possible value for p_i is always superior to any other choice, regardless 
    # of what p_{i+1}...p_k are.

    # --- Greedy Construction ---

    # Find the starting position of the value 1
    current_r, current_c = val_to_pos[1]
    path = [1]

    # Directions for 4-connectivity
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for _ in range(k - 1):
        best_neighbor_val = float('inf')
        best_neighbor_pos = (current_r, current_c)

        for dr, dc in directions:
            nr, nc = current_r + dr, current_c + dc

            # Check boundaries
            if 0 <= nr < rows and 0 <= nc < cols:
                neighbor_val = grid[nr][nc]
                if neighbor_val < best_neighbor_val:
                    best_neighbor_val = neighbor_val
                    best_neighbor_pos = (nr, nc)

        # Update current position and path
        current_r, current_c = best_neighbor_pos
        path.append(best_neighbor_val)

    return path