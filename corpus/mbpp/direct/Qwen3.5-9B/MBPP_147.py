def max_path_sum(triangle, n_rows, k):
    # Dynamic programming from bottom to top
    # dp[i][j] represents the maximum sum path starting from position (i, j) to the base
    dp = [[0] * len(row) for row in triangle]

    # Initialize the last row
    last_row = len(triangle) - 1
    if last_row < n_rows:
        last_row = n_rows - 1

    for j in range(len(triangle[last_row])):
        dp[last_row][j] = triangle[last_row][j]

    # Fill DP table from second to last row up to row k (if k < last_row)
    # We only need to compute up to row k if we consider the problem wants path from row k
    # But standard approach: compute full triangle then pick max at row k
    # Actually, re-reading: the problem likely wants the maximum sum path that starts at a specific row k
    # However, the examples show:
    # Example 1: triangle has 3 rows. k=2. Path sum 14.
    # Let's trace:
    # Row 0: [1, 0, 0]
    # Row 1: [4, 8, 0]
    # Row 2: [1, 5, 3]
    # If starting at row 2 (index 2), max is 5 or 3? No, 5 is max in row 2. But path must go down?
    # Wait, standard triangle path problem: you start at top and go down.
    # But here k is given as a parameter. Looking at examples:
    # Example 1: k=2. Max path sum 14.
    # If we start at top (row 0) and go down:
    # 1 -> 8 -> 5 = 14. This matches.
    # Example 2: k=2. 13 -> 7 -> 2? = 22. 13->7->4=24. 13->4->4=21. Max is 24. Matches.
    # Example 3: k=2. 2->18->25=45. 2->18->21=41. 2->11->21=34. 2->11->25=38. 
    # Wait, example 3 output is 53.
    # How to get 53? 
    # 2 (row0) -> 11 (row1) -> 25 (row2) = 38.
    # 2 (row0) -> 18 (row1) -> 21 (row2) = 41.
    # Maybe the triangle is:
    # 2, 0, 0
    # 11, 18, 0
    # 21, 25, 33
    # Path: 2 -> 11 -> 21 = 34.
    # Path: 2 -> 18 -> 25 = 45.
    # Path: 2 -> 11 -> 25 = 38.
    # Path: 2 -> 18 -> 21 = 41.
    # Path: 2 -> 0 -> ...? 
    # Wait, maybe k is not the starting row but something else? Or maybe the triangle values are different?
    # Let me re-read the problem statement carefully.
    # "find the maximum total path sum in the given triangle"
    # Usually, this is a dynamic programming problem where you start at the top and move to adjacent numbers on the row below.
    # But the parameter k is there. 
    # Let's check the first example again:
    # [[1, 0, 0], [4, 8, 0], [1, 5, 3]], 2, 2
    # If k=2 means start at row index 2? Then max is 5. Not 14.
    # If k=2 means stop at row index 2? Then it's the full path. 1+8+5=14.
    # Example 2: 13+7+4=24.
    # Example 3: 2+18+25=45. But expected is 53.
    # How to get 53 in example 3?
    # Maybe the triangle is:
    # 2
    # 11, 18
    # 21, 25, 33
    # Path: 2 -> 18 -> 33 = 53? 
    # 2 + 18 + 33 = 53. Yes!
    # So the path is: top -> right child of 18 -> right child of 33? No, 33 is in row 2.
    # Row 0: 2
    # Row 1: 11, 18
    # Row 2: 21, 25, 33
    # From 2, you can go to 11 or 18.
    # From 18, you can go to 25 or 33.
    # Path: 2 -> 18 -> 33 = 53.
    # So the triangle is triangular: row i has i+1 elements?
    # Example 1:
    # Row 0: 1
    # Row 1: 4, 8
    # Row 2: 1, 5, 3
    # Path: 1 -> 8 -> 5 = 14. Correct.
    # Example 2:
    # Row 0: 13
    # Row 1: 7, 4
    # Row 2: 2, 4, 6
    # Path: 13 -> 7 -> 4 = 24? Or 13 -> 7 -> 6 = 26? Or 13 -> 4 -> 4 = 21? Or 13 -> 4 -> 6 = 23?
    # Wait, 13+7+4=24. 13+7+6=26. But expected is 24.
    # Why 24? Maybe the triangle is:
    # 13, 0, 0
    # 7, 4, 0
    # 2, 4, 6
    # And the path is: 13 -> 7 -> 4? But 7 is at index 0, 4 at index 1? 
    # From index 0 of row 1 (value 7), you can go to index 0 or 1 of row 2 (values 2, 4).
    # From index 1 of row 1 (value 4), you can go to index 1 or 2 of row 2 (values 4, 6).
    # So paths:
    # 13 -> 7 -> 2 = 22
    # 13 -> 7 -> 4 = 24
    # 13 -> 4 -> 4 = 21
    # 13 -> 4 -> 6 = 23
    # Max is 24. Correct.
    # So the problem is: find the maximum path sum starting from the top (row 0) to the bottom (row n_rows-1).
    # The parameter k might be redundant or indicate the number of rows? But n_rows is also given.
    # Wait, the function signature is max_path_sum(triangle, n_rows, k).
    # In the examples, n_rows=3 for all? 
    # Example 1: triangle has 3 rows. n_rows=3, k=2.
    # Example 2: triangle has 3 rows. n_rows=3, k=2.
    # Example 3: triangle has 3 rows. n_rows=3, k=2.
    # So k=2 in all cases. What does k mean?
    # Maybe k is the number of rows to consider? But n_rows is also provided.
    # Or maybe the triangle is not necessarily triangular in the input, but we only consider the first n_rows rows?
    # And k is something else?
    # But in all examples, the path goes from row 0 to row n_rows-1.
    # And k=2 in all examples. Maybe k is the maximum index allowed in the last row? 
    # Or maybe k is unused? 
    # Let's assume the standard problem: maximum path sum from top to bottom.
    # The parameter k might be a red herring or used for something else, but based on examples, we just compute the full path.
    # However, the problem says "satisfy these assertions", so we must follow the pattern.
    # Given that in all examples k=2 and n_rows=3, and the path goes to the last row, I'll compute the full path sum.
    # But what if k is the row index where we start? No, because then example 1 would be 5.
    # What if k is the number of rows to skip? No.
    # Let's ignore k and n_rows and just use the triangle as is, assuming it's a standard triangle problem.
    # But wait, the problem says "given triangle" and provides n_rows. Maybe the triangle has more rows but we only care about n_rows?
    # And k is the maximum column index? 
    # But in the examples, the path naturally goes to the bottom.
    # I'll implement the standard dynamic programming for maximum path sum from top to bottom, ignoring k for now since it doesn't affect the examples.
    # Actually, looking again: the problem might be from a context where k is the number of rows, but n_rows is also provided.
    # Let's just use the triangle's actual rows up to n_rows.
    # And k might be unused. I'll proceed with standard DP.

    # However, to be safe, let's assume the triangle is given as a list of lists, and we take the first n_rows rows.
    # And k is not used.

    # But wait, the problem might be from a specific platform where k has meaning.
    # Given the constraints, I'll write the standard solution.

    # DP approach:
    # Create a DP table of same dimensions as triangle (up to n_rows)
    # Initialize the last row with the values from the triangle
    # For each row from n_rows-2 down to 0, update each cell with value + max of two children
    # The answer is the maximum value in the top row (which is just one value).

    # But wait, the standard problem: the answer is the value at the top after computing bottom-up.
    # Let's code it.

    # However, the triangle might not be perfectly triangular in the input? 
    # But the examples are triangular.
    # We'll assume the triangle is a list of lists where triangle[i] has i+1 elements.
    # And we take the first n_rows rows.

    # Steps:
    # 1. Take the first n_rows rows of triangle.
    # 2. If n_rows is 0, return 0.
    # 3. Create a DP table of size n_rows x n_rows (since row i has i+1 elements, we can just use the triangle structure).
    # 4. Initialize DP with the last row (row n_rows-1).
    # 5. Iterate from row = n_rows-2 down to 0:
    #      For each element in row i, dp[i][j] = triangle[i][j] + max(dp[i+1][j], dp[i+1][j+1])
    # 6. The result is dp[0][0].

    # But wait, what if k is used to limit the columns? 
    # In the examples, k=2, and the last row has 3 elements (indices 0,1,2). 
    # Maybe k is the maximum column index allowed? But in the examples, the path uses columns within range.
    # Since the examples work with the full triangle, I'll ignore k.

    # Let's code accordingly.

    n_rows = min(n_rows, len(triangle)) if triangle else 0

    if n_rows == 0:
        return 0

    # Take the first n_rows rows
    triangle = triangle[:n_rows]

    # Initialize DP with the last row
    dp = [row[:] for row in triangle[-1]]

    # Build from bottom to top
    for i in range(n_rows - 2, -1, -1):
        new_row = []
        for j in range(len(triangle[i])):
            new_val = triangle[i][j] + max(dp[j], dp[j+1])
            new_row.append(new_val)
        dp = new_row

    return dp[0]

# But wait, the examples have k=2. What if k is the number of rows to consider?
# In the examples, n_rows=3, k=2. But we used 3 rows.
# Maybe k is the maximum index in the last row? 
# But in example 1, last row has 3 elements, k=2. 
# Maybe we only consider elements up to index k in the last row? 
# But the path naturally goes to the last