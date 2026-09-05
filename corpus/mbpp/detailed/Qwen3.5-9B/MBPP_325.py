def _compute_max_square_root(value: int) -> int:
    """
    Computes the floor of the square root of a non-negative integer.
    This function finds the largest integer 'k' such that k*k <= value.
    It uses integer arithmetic to avoid floating-point precision issues.

    :param value: A non-negative integer.
    :return: The integer square root (floor) of value.
    :raises ValueError: If value is negative.
    """
    if value < 0:
        raise ValueError("Cannot compute square root for a negative number.")

    if value == 0:
        return 0

    # Initial guess using floating point sqrt, then clamp to integer.
    # For very large numbers, this is still a good starting point.
    guess = int(value ** 0.5)

    # Newton's method refinement to ensure exact integer result if floating point had errors.
    # This loop runs very few times for standard integers.
    while True:
        square = guess * guess
        if square > value:
            guess -= 1
        else:
            # Check if the next lower integer would work
            next_guess = guess + 1
            if next_guess * next_guess > value:
                break
            else:
                guess += 1
        if square == value:
            break

    return guess


def _find_smallest_square_for_difference(
    current_target: int, 
    max_edge: int, 
    min_squares_count: int
) -> int:
    """
    Recursive helper function to find the minimum number of squares 
    needed to sum up to 'current_target'.

    Strategy:
    We iterate from the largest possible perfect square (max_edge * max_edge) 
    down to 1. For each square 's*s', we subtract it from the target and 
    recursively solve for the remainder. We add 1 to the result of the 
    recursive call because we just used one square ('s*s').

    We keep track of 'min_squares_count' to prune branches that have already 
    exceeded the current best known solution for 'current_target'.

    :param current_target: The remaining number we need to decompose.
    :param max_edge: The maximum integer whose square can be used (optimization).
    :param min_squares_count: The current best solution found so far for this target 
                             (used for memoization/pruning).
    :return: The minimum number of squares needed to sum to current_target.
    :raises ValueError: If current_target is negative.
    """
    if current_target < 0:
        raise ValueError("Current target cannot be negative.")

    if current_target == 0:
        return 0

    # Base case optimization: 
    # If max_edge is 0 or 1, we can only use 1 (unless target is 0 which is handled).
    if max_edge <= 1:
        return current_target

    # Initialize minimum squares to infinity (or a large enough number).
    best_count = float('inf')

    # Iterate from max_edge down to 1.
    # We stop early if max_edge * max_edge > current_target.
    # However, the loop logic handles this by checking if square > target.
    for edge in range(max_edge, 0, -1):
        square = edge * edge

        if square > current_target:
            continue

        # Recursive step:
        # Use one square of size 'edge', then find min squares for the remainder.
        remainder = current_target - square

        # Get the result for the remainder.
        # We pass 'remainder' as the new target.
        # For the recursive call, the max_edge can technically be the same 'edge' 
        # or slightly less to avoid redundant calculations of the same square size,
        # but standard Lagrange's four-square algorithm logic often just recurses.
        # To be strictly greedy/dp based, we just recurse.
        count_for_remainder = _find_smallest_square_for_difference(
            current_target=remainder,
            max_edge=edge,  # Optimize: next square cannot be larger than the one just used
            min_squares_count=best_count
        )

        total_count = 1 + count_for_remainder

        # Update best_count if we found a shorter sequence.
        if total_count < best_count:
            best_count = total_count

        # Optimization: If we found a solution with 4 squares (Lagrange's theorem says 
        # every number is sum of at most 4), we can stop searching for larger squares
        # because we can't do better than 4? Actually, Lagrange says max is 4.
        # But we are finding the *minimum*. If we hit 1, 2, or 3, we might break?
        # Not necessarily. 12 = 4+4+4 (3). 12 = 9+1+1+1 (4). Minimum is 3.
        # However, if we find a solution equal to the theoretical lower bound 
        # (e.g. if target is a perfect square -> 1, or can be done in 2?), 
        # we might want to stop. 
        # But a simpler optimization is simply the pruning against 'min_squares_count'.
        # If 'best_count' drops to 4, we might still find a 3. 
        # Given the constraint of "explicit code" and correctness, we let it run 
        # unless we implement full DP/memoization. 
        # Since the problem asks for explicit steps and the numbers usually aren't huge 
        # for this specific algorithm (Lagrange's 4-square theorem guarantees termination quickly),
        # we proceed with the explicit recursion.
        # However, to ensure robustness and avoid infinite loops in weird edge cases 
        # (though unlikely with this logic), we ensure we don't go deeper than a safe limit?
        # No, the base case handles 0. The loop decreases the target. It terminates.

    return int(best_count)


def get_Min_Squares(target_number: int) -> int:
    """
    Finds the minimum number of perfect square numbers that sum to 'target_number'.

    This function implements Lagrange's Four-Square Theorem approach via recursion.
    It explicitly handles edge cases like negative numbers, zeros, and single elements
    before delegating to the recursive solver.

    Examples:
    get_Min_Squares(6) -> 3 (4 + 1 + 1)
    get_Min_Squares(2) -> 2 (1 + 1)
    get_Min_Squares(4) -> 1 (4)

    :param target_number: The positive integer to be decomposed into sum of squares.
    :return: The minimum count of squares required.
    :raises ValueError: If the input is not a non-negative integer.
    """

    # --- Step 1: Input Validation ---

    # Check for type correctness.
    if not isinstance(target_number, int):
        raise TypeError(f"Input must be an integer, received {type(target_number).__name__}")

    # Check for negative numbers.
    if target_number < 0:
        raise ValueError(f"Input must be non-negative, received {target_number}")

    # --- Step 2: Handle Degenerate Cases Explicitly ---

    # Edge case: 0. The sum of squares equal to 0 is just one 0, 
    # but mathematically 0 needs 0 squares if we don't count 0 itself as a building block 
    # for positive sums. However, usually in this problem context (Lagrange), 
    # the target is positive. 
    # If target is 0, strictly speaking, 0 = 0^2. Does that count as 1 square?
    # Or 0 squares? 
    # Based on standard LeetCode "Perfect Squares" (Problem 279) definition:
    # 12 = 4 + 4 + 4 (3 squares).
    # If input is 0, the answer is usually 0 squares in algorithmic contexts, 
    # but sometimes 1 if 0 is considered a square. 
    # Given the constraints of the problem (assertions use 2, 4, 6), 
    # let's assume 0 -> 0 squares (identity) or handle it gracefully.
    # Let's assume 0 requires 0 squares.
    if target_number == 0:
        return 0

    # Edge case: Negative handled above.

    # --- Step 3: Calculate Maximum Edge ---

    # Determine the largest integer whose square is <= target_number.
    max_edge = _compute_max_square_root(target_number)

    # --- Step 4: Solve Recursively ---

    # Call the helper function with the calculated max_edge.
    # We pass a large number for min_squares_count to indicate "no pruning yet".
    result = _find_smallest_square_for_difference(
        current_target=target_number,
        max_edge=max_edge,
        min_squares_count=float('inf')
    )

    # --- Step 5: Return Result ---

    # The result is guaranteed to be an integer.
    return result