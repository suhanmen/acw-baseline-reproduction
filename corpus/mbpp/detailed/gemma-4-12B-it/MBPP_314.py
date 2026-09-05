1.  **Define a constant for the expected number of rows.**
2.  **Validate input dimensions.**
3.  **Flatten the 2xN grid into a sequence of columns, where each column is the sum of its two cells.**
    - Wait, the problem says "no two chosen numbers are adjacent". In a 2xN grid, adjacency is defined by both horizontal and vertical neighbors.
    - If we choose a cell $(r, c)$, we cannot choose $(r \pm 1, c)$, $(r, c \pm 1)$, or $(r \pm 1, c \pm 1)$? No, standard grid adjacency usually means sharing an edge (4-connectivity).
    - Let's re-examine the examples:
        - `[[1, 4, 5], [2, 0, 0]]`, n=3. Max sum = 7. (Possible sets: {4, 5} no, {1, 0, 0} no. {1, 5} no, {4, 0} no. Actually, 1+2 is adjacent. 4+0 is adjacent. 1+4 is adjacent. 5+0 is adjacent. 4+5 is adjacent.
        - Let's look at the sum: 1+2=3, 4+0=4, 5+0=5.
        - To get 7, we need (2, 5) or (1, 2, 4) ... wait.
        - If "adjacent" means 4-connectivity:
          Grid:
          A B C
          D E F
          Adjacencies: (A,B), (B,C), (D,E), (E,F), (A,D), (B,E), (C,F).
          Example 1: `[[1, 4, 5], [2, 0, 0]]`
          A=1, B=4, C=5, D=2, E=0, F=0.
          Sum 7 can be achieved by {B, F} -> 4+0=4 (No), {A, C, E} -> 1+5+0=6 (No).
          Wait, if we pick B(4) and C(5), they are adjacent.
          If we pick A(1) and C(5), they are not adjacent. Sum 6.
          If we pick D(2) and C(5), they are not adjacent. Sum 7.
          Wait, D and C are (1,0) and (0,2) - they are not adjacent.
          Correct. Sum 7 is D(2) + C(5).
        - Example 2: `[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]`
          Max sum 24.
          Possible: 10 + 9 (adj) X. 10 + 8 (adj) X. 10 + 7 (adj) X.
          10 + 5 (adj) X. 10 + 4 (adj) X.
          Let's try picking elements from the bottom row and top row.
          If we pick 10 (bottom right), we cannot pick 9 (bottom) or 5 (top).
          We can pick 8 (bottom) - No, 8 is adjacent to 9 (no) but 10 is adjacent to 9. 8 is not adjacent to 10.
          Wait, in a 2xN grid, $(r, c)$ is adjacent to $(r, c-1), (r, c+1), (r-1, c), (r+1, c)$.
          So for Example 2:
          Row 0: 1, 2, 3, 4, 5
          Row 1: 6, 7, 8, 9, 10
          Pick 10 (1,4). Neighbors: 9 (1,3) and 5 (0,4).
          Pick 8 (1,2). Neighbors: 7 (1,1), 9 (1,3), 3 (0,2).
          Pick 4 (0,3). Neighbors: 3 (0,2), 5 (0,4), 9 (1,3).
          This is a dynamic programming problem on a grid.

4.  **DP State:**
    Let $dp[i][mask]$ be the max sum using first $i$ columns where $mask$ represents the selection in column $i$.
    Since there are 2 rows, the mask has 4 possibilities for each column:
    00: Neither selected
    01: Row 0 selected
    10: Row 1 selected
    11: Both selected (Not allowed since they are adjacent)

    Actually, because $(r, c)$ and $(r+1, c)$ are adjacent, we can never pick both in the same column.
    Possible states per column:
    State 0: None selected in column $i$.
    State 1: Row 0 selected in column $i$.
    State 2: Row 1 selected in column $i$.

    Transitions:
    - To State 0 at $i$:
      From State 0 at $i-1$, State 1 at $i-1$, State 2 at $i-1$.
      $dp[i][0] = \max(dp[i-1][0], dp[i-1][1], dp[i-1][2])$
    - To State 1 at $i$:
      From State 0 at $i-1$ (No neighbors), State 2 at $i-1$ (Row 1 is not adjacent to Row 0 of next col? No, Row 1 of $i-1$ is adjacent to Row 0 of $i-1$, but is it adjacent to Row 0 of $i$?)
      Adjacency check:
      $(0, i)$ is adjacent to: $(0, i-1), (0, i+1), (1, i)$.
      So if we pick $(0, i)$, we cannot pick $(0, i-1)$ and we cannot pick $(1, i)$.
      Wait, $(0, i)$ is NOT adjacent to $(1, i-1)$.
      Let's re-verify:
      Grid:
      (0,0) (0,1) (0,2)
      (1,0) (1,1) (1,2)
      Neighbors of (0,1): (0,0), (0,2), (1,1).
      Neighbors of (1,1): (1,0), (1,2), (0,1).

      So, if we pick $(0, i)$:
      - We cannot pick $(0, i-1)$.
      - We cannot pick $(1, i)$.
      - We CAN pick $(1, i-1)$.

      DP States for column $i$:
      $dp[i][0]$: Max sum ending at col $i$, nothing picked in col $i$.
      $dp[i][1]$: Max sum ending at col $i$, only row 0 picked in col $i$.
      $dp[i][2]$: Max sum ending at col $i$, only row 1 picked in col $i$.

      Transitions:
      $dp[i][0] = \max(dp[i-1][0], dp[i-1][1], dp[i-1][2])$
      $dp[i][1] = \text{grid}[0][i] + \max(dp[i-1][0], dp[i-1][2])$
      $dp[i][2] = \text{grid}[1][i] + \max(dp[i-1][0], dp[i-1][1])$

    Let's trace Example 1: `[[1, 4, 5], [2, 0, 0]]`
    $i=0$:
    $dp[0][0] = 0$
    $dp[0][1] = 1$
    $dp[0][2] = 2$
    $i=1$:
    $dp[1][0] = \max(0, 1, 2) = 2$
    $dp[1][1] = 4 + \max(0, 2) = 6$
    $dp[1][2] = 0 + \max(0, 1) = 1$
    $i=2$:
    $dp[2][0] = \max(2, 6, 1) = 6$
    $dp[2][1] = 5 + \max(2, 1) = 7$
    $dp[2][2] = 0 + \max(2, 6) = 6$
    Max(6, 7, 6) = 7. Correct.

    Trace Example 2: `[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]`
    $i=0: dp[0][0]=0, dp[0][1]=1, dp[0][2]=6$
    $i=1: dp[1][0]=\max(0,1,6)=6; dp[1][1]=2+\max(0,6)=8; dp[1][2]=7+\max(0,1)=8$
    $i=2: dp[2][0]=\max(6,8,8)=8; dp[2][1]=3+\max(6,8)=11; dp[2][2]=8+\max(6,8)=16$
    $i=3: dp[3][0]=\max(8,11,16)=16; dp[3][1]=4+\max(8,16)=20; dp[3][2]=9+\max(8,11)=20$
    $i=4: dp[4][0]=\max(16,20,20)=20; dp[4][1]=5+\max(16,20)=25; dp[4][2]=10+\max(16,20)=30$
    Wait, Example 2 result is 24. Let me re-read.
    Ah, $dp[4][1] = 5 + \max(dp[3][0], dp[3][2]) = 5 + \max(16, 20) = 25$.
    My trace got 30. Let me re-check the adjacency.
    Example 2: `[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]`
    If I pick 10 (row 1, col 4) and 5 (row 0, col 4), they are adjacent.
    If I pick 10 (row 1, col 4) and 4 (row 0, col 3), they are NOT adjacent.
    Wait, $10 + 4 + 3 + 7 = 24$? No.
    Wait, the sum is 24. How to get 24?
    Maybe 10 + 9 is adjacent. 10 + 8 is adjacent? No.
    Let's re-list neighbors:
    (1,4) is 10. Neighbors: (1,3)=9, (0,4)=5.
    (1,2) is 8. Neighbors: (1,1)=7, (1,3)=9, (0,2)=3.
    (0,0) is 1. Neighbors: (0,1)=2, (1,0)=6.
    If we pick 10, 8, 6: $10+8+6 = 24$.
    Are they adjacent?
    10 at (1,4)
    8 at (1,2)
    6 at (1,0)
    None of these are adjacent!
    (1,4) neighbors: (1,3), (0,4).
    (1,2) neighbors: (1,1), (1,3), (0,2).
    (1,0) neighbors: (1,1), (0,0).
    None of the picked coordinates are in each other's neighbor sets.
    So 24 is correct.

    Why did my DP get 30?
    $dp[4][2]$ is picking 10 at (1,4).
    $dp[4][2] = 10 + \max(dp[3][0], dp[3][1])$
    $dp[3][0] = 16$ (from $dp[2][2]=16$)
    $dp[3][1] = 20$ (from $dp[2][2]=16$)
    $dp[4][2] = 10 + 20 = 30$.
    Wait, $dp[3][1]$ is picking 4 at (0,3).
    If we pick 4 at (0,3) and 10 at (1,4), are they adjacent?
    (0,3) neighbors: (0,2), (0,4), (1,3