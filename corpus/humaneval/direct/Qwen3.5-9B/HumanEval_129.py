def minPath(grid, k):
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
    A path A (of length k) is considered less than a path B (length k) if
    after making the ordered lists of the values on the cells that A and B go
    through (let's call them lst_A and lst_B), lst_A is lexicographically less
    than lst_B, in other words, there exist an integer index i (1 <= i <= k)
    such that lst_A[i] < lst_B[i] and for any j (1 <= j < i) we have
    lst_A[j] = lst_B[j].
    It is guaranteed that the answer is unique.
    Return an ordered list of the values on the cells that the minimum path go through.

    Examples:

        Input: grid = [ [1,2,3], [4,5,6], [7,8,9]], k = 3
        Output: [1, 2, 1]

        Input: grid = [ [5,9,3], [4,1,6], [7,8,2]], k = 1
        Output: [1]
    """
    import collections

    n = len(grid)
    # Map value -> (row, col)
    val_to_pos = {val: (r, c) for r in range(n) for c in range(n) for val in [grid[r][c]]}
    # Since values are 1..N*N and unique, we can also precompute sorted order of positions by value.

    # Directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # We need to find the lexicographically smallest path of length k.
    # Since k can be large, we cannot do BFS for all paths.
    # However, note the following:
    # The lexicographically smallest path will always try to pick the smallest available number at each step.
    # But we are constrained by connectivity.
    #
    # Key insight: 
    # The absolute smallest number in the grid is 1. If we can start at 1, then the first element of our path is 1 (which is the smallest possible start).
    # Then, from 1, we want to go to the smallest neighbor. If we get stuck or need to revisit, we might have to choose again.
    # However, note that the problem says "lexicographically least". This is a greedy approach if we can always extend the path.
    # But what if the smallest neighbor is not reachable? Actually, we can always move to a neighbor if we are not at the boundary.
    # However, the path must be of length k. We might have to loop.
    #
    # Important observation from examples:
    # Example 1: grid = [[1,2,3],[4,5,6],[7,8,9]], k=3 -> [1,2,1]
    # Why [1,2,1] and not [1,2,3]? Because [1,2,1] < [1,2,3] lexicographically? 
    # Compare: 
    #   [1,2,1] vs [1,2,3]: at index 2, 1 < 3 -> so [1,2,1] is smaller.
    # But why can't we do [1,2,1]? We can go from 2 (at (0,1)) to 1 (at (0,0)) because they are neighbors.
    #
    # Strategy:
    # We can use BFS layer by layer (like Dijkstra but for lex order) but the state space is too big if k is large.
    # However, note that the grid size is not specified but typically in such problems N is small (e.g., up to 100) and k might be large.
    # But the problem says "It is guaranteed that the answer is unique", which hints that there's a deterministic greedy strategy.
    #
    # Alternate approach:
    # Since we want the lexicographically smallest path, we can think of it as:
    #   Step 0: start at the smallest number in the grid? Not necessarily, because maybe the smallest number is isolated and we can't form a path of length k? 
    #   But the grid is connected (it's a grid graph) and we can revisit nodes. So we can always start at 1 and then move around.
    #   Therefore, the first element of the path must be 1? 
    #   Wait: what if k=1? Then the smallest path is [1]. 
    #   What if k>1? We start at 1, then go to the smallest neighbor. Then from that neighbor, go to the smallest neighbor of that, and so on.
    #   But note: the example [1,2,1] for k=3: 
    #       Start at 1 -> then go to 2 (smallest neighbor of 1 is 2) -> then from 2, the neighbors are 1, 3, 5. The smallest is 1. So we go back to 1.
    #   So it seems greedy: at each step, go to the smallest value among the neighbors.
    #
    # Is this always optimal?
    # Consider: grid = [[1, 100], [2, 3]], k=3. 
    #   Start at 1: neighbors are 100 and 2. Smallest is 2. Path: [1,2]. 
    #   From 2: neighbors are 1 and 3. Smallest is 1. Path: [1,2,1].
    #   But what if we started at 1 and went to 100? [1,100,...] which is worse than [1,2,...].
    #   What if we didn't start at 1? If we start at 2: [2,...] which is worse than [1,...].
    # So starting at 1 is always best for the first element.
    #
    # Then, at each step, we choose the smallest neighbor. 
    # Why? Because if we have a choice between going to value A or value B (A < B) at step i, then any path going to B at step i will be lexicographically larger than one going to A at step i, regardless of what comes after.
    # Therefore, greedy choice at each step is optimal.
    #
    # Algorithm:
    #   1. Find the position of the value 1. Start there.
    #   2. For step in range(k-1) [we already have the first element]:
    #        Look at all valid neighbors (up, down, left, right) that are in bounds.
    #        Choose the neighbor with the smallest grid value.
    #        Append that value to the path.
    #        Update current position to that neighbor.
    #   3. Return the path.
    #
    # But wait: what if there are multiple neighbors with the same smallest value? 
    #   The problem states: "Every integer in the range [1, N * N] inclusive appears exactly once". So values are unique. 
    #   Therefore, there is exactly one neighbor with the minimal value (if any exist).
    #
    # Let's test with example 1: 
    #   grid = [[1,2,3],[4,5,6],[7,8,9]], k=3
    #   Start at 1 (0,0). Path = [1]
    #   Step 1: neighbors of (0,0) are (0,1)=2 and (1,0)=4. Min is 2. Path=[1,2], pos=(0,1)
    #   Step 2: neighbors of (0,1) are (0,0)=1, (0,2)=3, (1,1)=5. Min is 1. Path=[1,2,1] -> matches.
    #
    # Example 2: k=1 -> we return [1] (since we start at 1 and k=1, we don't do any steps).
    #
    # Therefore, the algorithm is:
    #   Find (r, c) such that grid[r][c] == 1.
    #   path = [1]
    #   current_r, current_c = r, c
    #   for _ in range(k-1):
    #       Find all neighbors (nr, nc) in bounds.
    #       Find the one with min grid[nr][nc].
    #       Append that value, update current position.
    #   return path

    # Edge: k=1 -> the loop doesn't run, returns [1] which is correct.

    # Find position of 1
    start_r, start_c = 0, 0
    for r in range(n):
        for c in range(n):
            if grid[r][c] == 1:
                start_r, start_c = r, c
                break
        if grid[start_r][start_c] == 1:
            break

    path = [1]
    r, c = start_r, start_c

    for _ in range(k-1):
        best_r, best_c = -1, -1
        best_val = float('inf')
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n:
                val = grid[nr][nc]
                if val < best_val:
                    best_val = val
                    best_r, best_c = nr, nc
        # Append the best value
        path.append(best_val)
        r, c = best_r, best_c

    return path