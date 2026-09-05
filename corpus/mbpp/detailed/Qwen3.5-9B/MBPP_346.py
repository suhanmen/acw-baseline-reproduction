def is_valid_input(n: int, k: int) -> bool:
    """
    Validate the inputs n and k.

    The problem context suggests n and k should be positive integers (n >= 1, k >= 1)
    based on the provided assertions (zigzag(4, 3), etc.).
    We will enforce n > 0 and k > 0.

    Args:
        n: An integer representing the row number.
        k: An integer representing the position in the row.

    Returns:
        True if inputs are valid, False otherwise.
    """
    if not isinstance(n, int):
        return False
    if not isinstance(k, int):
        return False
    if n <= 0:
        return False
    if k <= 0:
        return False

    return True

def is_in_bounds(n: int, k: int) -> bool:
    """
    Check if position k is within the valid bounds for row n in a zigzag triangle.

    In a standard zigzag (or Pascal-like triangle) numbering:
    Row 1 has 1 element.
    Row 2 has 2 elements.
    ...
    Row n has n elements.

    Therefore, for a given row n, valid k values are 1 <= k <= n.

    Args:
        n: The row number.
        k: The position in the row.

    Returns:
        True if k is within the bounds [1, n], False otherwise.
    """
    # We already validated n > 0 and k > 0 in the calling function,
    # but we check the upper bound here.
    if k > n:
        return False
    return True

def get_diagonal_level(row: int, pos: int) -> int:
    """
    Determine which anti-diagonal (or 'level' of summation) the element belongs to.

    In a triangular arrangement where:
    Row 1: [1] (diagonal index 1)
    Row 2: [2, 3] (diagonal indices 2, 2) -> Wait, let's trace the values.

    Let's reconstruct the pattern from the assertions:
    zigzag(1, 1) -> The sequence starts with 1.
    zigzag(2, 1) -> The next number is 2.
    zigzag(2, 2) -> The next number is 3.
    zigzag(3, 1) -> The next is 4? No, assertion says zigzag(3, 1) == 1.

    Wait, the assertion `assert zigzag(3, 1) == 1` contradicts a simple sequential count starting from 1 across rows.
    Let's re-read the standard definition of "Zigzag Number" or "Entry Number" in this context.
    Often, "Zigzag" in this specific competitive programming or math puzzle context refers to the position 
    in a sequence that bounces between diagonals, OR it refers to the Cantor pairing function, OR it refers to 
    the indices in a specific enumeration.

    However, looking at the specific values:
    zigzag(4, 3) == 5
    zigzag(4, 2) == 4
    zigzag(3, 1) == 1

    Let's try to build the triangle (n, k) -> value:
    (3, 1) -> 1
    (4, 2) -> 4
    (4, 3) -> 5

    What about (1, 1)? Usually 1.
    (2, 1)? Usually 2?
    (2, 2)? Usually 3?
    (3, 1)? 1? This implies the triangle is 1-indexed but the values reset or follow a snake pattern.

    Let's look at the sequence of values if we traverse the triangle in a "Zigzag" manner:
    Maybe the triangle is filled sequentially, but the question asks for the number at (n, k) 
    in a specific layout?

    Alternative Interpretation:
    The problem might be describing the "Zigzag" sequence A000000 or similar, but let's look at the geometry.

    If we fill the triangle row by row:
    Row 1: 1
    Row 2: 2, 3
    Row 3: 4, 5, 6
    Row 4: 7, 8, 9, 10
    This doesn't match (3, 1) -> 1.

    If we fill diagonally (like Cantor):
    Diag 1: (1,1) -> 1
    Diag 2: (1,2) X, (2,1) -> 2
    Diag 3: (1,3) X, (2,2) -> 3, (3,1) -> 4
    This doesn't match (3, 1) -> 1.

    Let's reconsider the specific data points:
    A = (3, 1) = 1
    B = (4, 2) = 4
    C = (4, 3) = 5

    Is it possible the triangle is defined such that row n starts at value 1 and goes up?
    Row 1: 1
    Row 2: 1, 2
    Row 3: 1, 2, 3 -> Then (3,1)=1. (3,2)=2, (3,3)=3.
    Row 4: 1, 2, 3, 4 -> Then (4,2)=2, (4,3)=3.
    This does NOT match (4,2)=4.

    Let's try a 1-based index sum approach (Cantor pairing style) but checking the values again.
    Maybe the value is the sum of coordinates?
    (3, 1) -> 3+1 = 4. No, result is 1.

    Maybe the value is related to the difference? |n - k|?
    (3, 1) -> 2. No.

    Let's look at the sequence 1, 4, 5 again.
    (3,1)=1
    (4,2)=4
    (4,3)=5

    Hypothesis: The "Zigzag" refers to the position of a number in a sequence that is written in a zigzag pattern on a grid, 
    and we are reversing the function to find the number at (n, k).

    Sequence S: 1, 2, 3, 4, 5, 6, 7, 8...
    Grid layout (Row n, Col k):
    If we write the numbers in a zigzag path through the integer lattice (n, k)?

    Let's try the standard "Zigzag number" definition from OEIS A000000? No.
    How about the "Entry number" in a specific "Zigzag" triangle where the direction of filling alternates?

    Standard Zigzag Triangle (Snake pattern):
    Row 1: 1 (Direction: Right)
    Row 2: 2, 3 (Direction: Right? Or Left?)
    Usually:
    Row 1: 1
    Row 2: 3, 2 (Right to Left)
    Row 3: 4, 5, 6 (Left to Right)
    Row 4: 9, 8, 7, 10? No.

    Let's try the "Snake" filling again carefully:
    Total elements before row n = (n-1)*n/2.
    Row n has n elements.
    If n is odd, we fill Left to Right?
    If n is even, we fill Right to Left?

    Let's test this hypothesis:
    Total before row 1: 0.
    Row 1 (n=1, odd): Fill 1..1.
       (1,1) = 1.

    Total before row 2: 1.
    Row 2 (n=2, even): Fill 2..3, but Right to Left.
       Positions: k=1, k=2.
       Values: 2, 3.
       Right to Left means (2,2) gets 2, (2,1) gets 3.
       So (2,1)=3, (2,2)=2.

    Total before row 3: 1+2=3.
    Row 3 (n=3, odd): Fill 4..6, Left to Right.
       Positions: k=1, k=2, k=3.
       (3,1)=4, (3,2)=5, (3,3)=6.
       Assertion check: zigzag(3, 1) should be 4. But required is 1. Fail.

    Okay, the standard snake fill doesn't yield (3,1)=1.

    Let's try the reverse: Maybe the numbering is based on diagonals?
    Diagonal d = n + k.
    Let's order by diagonal sum.
    (1,1): sum=2.
    (1,2), (2,1): sum=3.
    (1,3), (2,2), (3,1): sum=4.
    (1,4), (2,3), (3,2), (4,1): sum=5.

    If we zigzag the diagonals:
    Diag 2 (1,1): 1.
    Diag 3: (2,1), (1,2). Zigzag direction?
       If we go (2,1) then (1,2): values 2, 3.
       Then (3,1) is in Diag 4.

    This is getting complicated. Let's look at the numbers 1, 4, 5 again.
    (3,1) -> 1
    (4,2) -> 4
    (4,3) -> 5

    Notice that for n=3, k=1, the result is 1.
    For n=4, k=2, the result is 4.
    For n=4, k=3, the result is 5.

    Is it possible the formula is: Value = (n - k + 1) + (k - 1)? No.

    Let's try: Value = (k - 1) * n + (n - k + 1)?
    n=3, k=1: (0)*3 + (3) = 3. No.

    Let's try to fit a polynomial or specific pattern.
    (3, 1) -> 1
    (4, 2) -> 4
    (4, 3) -> 5

    Maybe the value is the rank of the element if we traverse the triangle in a specific zigzag order?
    Let's define the traversal order:
    Start at (1,1).
    Go to (2,1).
    Go to (2,2).
    Go to (3,2).
    Go to (3,3).
    Go to (4,3).
    Go to (4,2).
    Go to (4,1).

    Let's number these steps:
    1. (1,1) -> 1
    2. (2,1) -> 2
    3. (2,2) -> 3
    4. (3,2) -> 4
    5. (3,3) -> 5
    6. (4,3) -> 6
    7. (4,2) -> 7
    8. (4,1) -> 8

    Check assertions:
    zigzag(3, 1): In this sequence, (3,1) is not visited until... wait.
    My sequence missed (3,1).
    Let's adjust the zigzag path.
    Usually zigzag goes:
    (1,1)
    (2,1), (2,2)
    (3,2), (3,3) ... skipping (3,1)?
    No, we must visit all (n, k) where 1<=k<=n.

    Let's try the "Cantor Zigzag" specifically on the triangle 1<=k<=n.
    Diagonals D = n + k.
    D=2: (1,1) -> 1.
    D=3: (2,1), (1,2) [Invalid since k<=n].
           Valid points for D=3 in our triangle: (2,1). (1,2) is invalid (2>1).
           So only (2,1).
           Order?
           If D=3 goes (2,1) -> 2.
    D=4: (3,1), (2,2).
           If we zigzag alternating direction.
           D=2 (Right to Left? n increases, k decreases?): (1,1).
           D=3 (Left to Right?): (2,1). (Note: (1,2) invalid).
           D=4 (Right to Left?): (2,2), (3,1).
           Values:
           (1,1) -> 1
           (2,1) -> 2
           (2,2)