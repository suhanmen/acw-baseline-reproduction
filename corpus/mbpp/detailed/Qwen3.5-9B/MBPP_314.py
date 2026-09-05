from typing import List, Tuple, Optional

def _validate_2d_grid(input_grid: List[List[int]]) -> None:
    """
    Validates that the input is a valid 2D grid of integers.

    Raises:
        TypeError: If input_grid is not a list of lists or contains non-integer values.
        ValueError: If the grid dimensions are inconsistent or empty.
    """
    if not isinstance(input_grid, list):
        raise TypeError("Input grid must be a list of lists.")

    if len(input_grid) != 2:
        raise ValueError("Input grid must have exactly 2 rows.")

    row_0 = input_grid[0]
    row_1 = input_grid[1]

    if not isinstance(row_0, list) or not isinstance(row_1, list):
        raise TypeError("Each row of the grid must be a list.")

    if len(row_0) != len(row_1):
        raise ValueError("Both rows in the grid must have the same number of columns.")

    if len(row_0) == 0:
        raise ValueError("The grid cannot have zero columns (empty input not allowed).")

    if len(row_0) != 2:
        # The problem specifies a 2xn grid, but structurally we might need more columns.
        # However, the assertion examples imply n is the number of columns.
        # The function signature takes n as an argument, so we trust the caller's n.
        # We just validate the structure matches the concept of a grid.
        pass

    for value in row_0:
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("All elements in the grid must be integers.")

    for value in row_1:
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("All elements in the grid must be integers.")


def _validate_n(n: int, num_columns: int) -> None:
    """
    Validates the dimension n against the actual number of columns in the grid.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n does not match the number of columns or is negative.
    """
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("The dimension n must be an integer.")

    if n != num_columns:
        raise ValueError(f"The provided dimension n ({n}) does not match the number of columns ({num_columns}).")

    if n <= 0:
        raise ValueError("The dimension n must be a positive integer.")


def _get_column_at_index(grid: List[List[int]], index: int) -> Tuple[int, int]:
    """
    Helper to retrieve the pair of values from both rows at a specific column index.

    Returns:
        A tuple (top_value, bottom_value).
    """
    top = grid[0][index]
    bottom = grid[1][index]
    return top, bottom


def _calculate_max_sum_for_column(index: int, grid: List[List[int]], 
                                   current_col_sum: int) -> Tuple[int, int]:
    """
    Internal helper to manage state as we iterate through columns.
    This function is a placeholder for the logic that will be expanded in the main loop.
    It currently just returns the current sum and zero for the next step to initialize logic.
    """
    return current_col_sum, 0


def _solve_max_sum_rectangular_dp(num_columns: int, grid: List[List[int]]) -> int:
    """
    Solves the problem using dynamic programming.

    The problem asks for the maximum sum such that no two chosen numbers are adjacent.
    In a 2xN grid, "adjacent" typically implies:
    1. Left-Right adjacency within the same row.
    2. Top-Bottom adjacency within the same column.
    3. Diagonal adjacency is usually NOT considered "adjacent" in standard "no two chosen numbers are adjacent" grid problems unless specified.
       However, looking at the problem constraints and standard variations (like House Robber II or variations):
       - If we pick (r, c), we cannot pick (r, c+1), (r, c-1), (r-1, c), (r+1, c).
       - The phrase "no two chosen numbers are adjacent" usually means the four cardinal neighbors (Up, Down, Left, Right).
       - Let's verify with the first example:
         Grid: [[1, 4, 5], [2, 0, 0]]
         n=3.
         Columns: (1,2), (4,0), (5,0).
         If we cannot pick adjacent columns (left-right) and adjacent rows (top-bottom):
         Option A: Pick Col 0 (1, 2). Sum = 3. Remaining valid: Col 2 (5, 0). Pick 5. Total = 8? 
         Wait, the example says 7.
         Let's re-read carefully: "no two chosen numbers are adjacent".
         Adjacency in a grid usually includes diagonals in some contexts, but strictly in graph theory on a grid, it's 4-connectivity.
         Let's try to derive 7 from [[1, 4, 5], [2, 0, 0]].
         Possible sets of non-adjacent cells:
         1. (0,0)=1, (0,2)=5 -> Sum 6.
         2. (0,0)=1, (1,2)=0 -> Sum 1.
         3. (1,0)=2, (0,2)=5 -> Sum 7. -> This works. (1,0) and (0,2) are not adjacent (separated by col 1).
         4. (1,0)=2, (1,2)=0 -> Sum 2.
         5. (0,1)=4, (0,0) no, (0,2) no, (1,1)=0. Can we pick (0,1)? Neighbors: (0,0), (0,2), (1,1). 
            If we pick (0,1)=4, we can't pick (0,0), (0,2), (1,1). 
            We could pick (1,0)? No, (1,0) is adjacent to (0,0) and (1,1). Is (1,0) adjacent to (0,1)? No (diagonal).
            Is diagonal considered adjacent? 
            If diagonal is NOT adjacent: Pick (1,0)=2, (0,1)=4. Sum = 6.
            If diagonal IS adjacent: Pick (1,0)=2, (0,1)=4 is invalid.

         Let's look at the second example to deduce the adjacency rule.
         Grid: [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
         Target: 24.
         Columns: 
         0: (1, 6)
         1: (2, 7)
         2: (3, 8)
         3: (4, 9)
         4: (5, 10)

         If we assume standard "no two adjacent" means 4-connectivity (Left, Right, Up, Down):
         We can pick (1,0)=1 and (2,2)=3? No, (1,0) and (2,2) are far.
         Let's try a pattern.
         If we pick column 0 (top) and column 2 (top): 1 + 3 = 4.
         If we pick column 0 (bottom) and column 2 (bottom): 6 + 8 = 14.

         Let's try to get 24.
         Max possible sum if no adjacency constraints: 1+2+3+4+5 + 6+7+8+9+10 = 55.
         We need to skip adjacent ones.

         Hypothesis 1: We can pick at most one cell per column? 
         If we pick one per column, we can't have adjacent columns picked. This is the standard House Robber problem.
         Values per column: 
         C0: max(1, 6) = 6
         C1: max(2, 7) = 7
         C2: max(3, 8) = 8
         C3: max(4, 9) = 9
         C4: max(5, 10) = 10
         Sequence: 6, 7, 8, 9, 10.
         Max sum non-adjacent in 1D array [6, 7, 8, 9, 10]:
         Pick 6 (skip 7, 8) -> pick 9 (skip 10)? 6+9=15.
         Pick 7 (skip 8, 9) -> pick 10? 7+10=17.
         This doesn't reach 24.

         Hypothesis 2: We can pick multiple cells in a column? 
         But if we pick both (top and bottom) of a column, they are adjacent vertically. So at most one per column.
         So we must pick at most one cell per column.
         AND we cannot pick adjacent columns? 
         If we pick Col 0 and Col 2, are they adjacent? No.
         So it reduces to: For each column i, choose exactly one value (top or bottom) OR none.
         Constraint: If we choose a value at column i, we cannot choose a value at column i-1 or i+1.
         This is equivalent to: Find a subset of columns such that no two indices are consecutive, and for each selected column i, we pick max(grid[0][i], grid[1][i]).

         Let's test Hypothesis 2 on Example 1:
         Cols: 
         0: max(1, 2) = 2
         1: max(4, 0) = 4
         2: max(5, 0) = 5
         Array: [2, 4, 5].
         Max non-adjacent sum: 
         Option 1: 2 (idx 0) + 5 (idx 2) = 7.
         Option 2: 4 (idx 1) = 4.
         Max is 7. Matches Example 1!

         Let's test Hypothesis 2 on Example 2:
         Cols:
         0: max(1, 6) = 6
         1: max(2, 7) = 7
         2: max(3, 8) = 8
         3: max(4, 9) = 9
         4: max(5, 10) = 10
         Array: [6, 7, 8, 9, 10].
         Max non-adjacent sum:
         Indices 0, 2, 4 -> 6 + 8 + 10 = 24.
         Matches Example 2 (24)!

         Let's test Hypothesis 2 on Example 3:
         Grid: [[7, 9, 11, 15, 19], [21, 25, 28, 31, 32]]
         Cols:
         0: max(7, 21) = 21
         1: max(9, 25) = 25
         2: max(11, 28) = 28
         3: max(15, 31) = 31
         4: max(19, 32) = 32
         Array: [21, 25, 28, 31, 32].
         Max non-adjacent sum:
         Try indices 0, 2, 4: 21 + 28 + 32 = 81.
         Try indices 1, 3: 25 + 31 = 56.
         Try indices 0, 3: 21 + 31 = 52.
         Try indices 0, 2: 21 + 28 = 49.
         Max is 81. Matches Example 3!

         Conclusion: The problem is reduced to a 1D House Robber problem where the value of column i is max(grid[0][i], grid[1][i]).
         The "adjacent" constraint applies between columns. Within a column, we pick the max, assuming we can't pick both (which would be adjacent vertically).
         What if picking the smaller one in a column allows a better global solution?
         Example: 
         Col 0: [100, 1] -> Max is 100.
         Col 1: [100, 100] -> Max is 100.
         Col 2: [100, 1] -> Max is 100.
         If we pick Col 0 (100), Col 2 (100) -> 200.
         Is there any case where picking the smaller value in a column is beneficial?
         No, because the choice at column i only restricts i-1 and i+