def No_of_Triangle(n, k):
    """
    Counts the maximum number of equilateral triangles that can be formed 
    within a larger equilateral triangle of side length n, 
    where each smaller triangle has a side length of k.

    Constraints/Logic:
    1. If k > n, it is impossible to fit a triangle of side k, return -1.
    2. If k == n, exactly 1 triangle exists.
    3. If k < n, we use the formula for the number of sub-triangles of 
       side k that can be oriented "upright" and "downward" within 
       a large triangle of side n.

    The number of triangles of side length k contained in a triangle of side n 
    is given by the formula:
    Count = (n - k + 1) * (n - k + 2) * (n - k + 3) // 6  -- this is for specific configurations.

    However, looking at the specific test cases provided:
    (4, 2) -> 7
    (4, 3) -> 3
    (1, 3) -> -1

    Let's analyze:
    If n=4, k=2:
    Upright triangles: The centers of the base of triangles of side 2 can 
    be placed in a triangle of side (n-k+1) = 3. 
    The number of such positions is (3 * (3+1) / 2) = 6.
    But we also have "inverted" triangles.
    Wait, for n=4, k=2, the formula for total triangles of side k is:
    Number of upright triangles = (n-k+1)(n-k+2)/2
    Number of inverted triangles = (n-2k+1)(n-2k+2)/2 if n >= 2k

    For (4, 2):
    Upright: (4-2+1)(4-2+2)/2 = 3*4/2 = 6
    Inverted: (4-2*2+1)(4-2*2+2)/2 = 1*2/2 = 1
    Total = 6 + 1 = 7. (Matches assertion)

    For (4, 3):
    Upright: (4-3+1)(4-3+2)/2 = 2*3/2 = 3
    Inverted: (4-2*3+1)... n < 2k, so 0.
    Total = 3 + 0 = 3. (Matches assertion)

    For (1, 3):
    k > n, returns -1. (Matches assertion)
    """
    if k > n:
        return -1

    # Number of upright triangles of side k
    upright = (n - k + 1) * (n - k + 2) // 2

    # Number of inverted triangles of side k
    inverted = 0
    if n >= 2 * k:
        inverted = (n - 2 * k + 1) * (n - 2 * k + 2) // 2
    elif n >= 1.5 * k: # Handle cases where inverted might exist but n < 2k
        # Actually, for an inverted triangle of side k to fit, 
        # the height required is k + (height of upright part).
        # The standard geometric derivation for inverted triangles of side k
        # requires the base to have enough room, which is n >= 2k.
        # Let's re-verify (4, 2): n=4, k=2. 2k=4. 4>=4 is true. 
        # Inverted = (4-4+1)(4-4+2)/2 = 1*2/2 = 1. Correct.
        pass

    return upright + inverted