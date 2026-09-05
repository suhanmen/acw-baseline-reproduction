def _compute_recursive_sum(n):
    """
    Helper function to compute the value based on the recursive formula:
    f(n) = max( f(n/2) + f(n/3) + f(n/4) + f(n/5), n )

    This function is designed to be called recursively with memoization to avoid recomputation.
    It handles non-integer inputs by converting them to floats for division, but ultimately
    returns an integer result as implied by the problem context and assertions.

    Parameters:
    n (int or float): The number to compute the function value for. Must be non-negative.

    Returns:
    int: The computed maximum sum.
    """
    # Explicit type conversion to ensure we are working with a numeric type that supports division
    numeric_n = float(n)

    # Check for negative numbers explicitly
    if numeric_n < 0:
        raise ValueError(f"Input must be non-negative, got {n}")

    # Base case: if n is 0, the sum is 0
    if numeric_n == 0:
        return 0

    # Base case: if n is less than 12 (threshold where division reduces the sum significantly)
    # We determine this threshold empirically or logically. 
    # For small n, n itself is often greater than the sum of parts.
    # For n=10, f(10) = max(f(5)+f(3)+f(2)+f(2), 10) = max(10+3+2+2, 10) = 17? 
    # Wait, let's re-evaluate the logic based on the assertion get_max_sum(10) == 12.
    # If f(10) = 12, then f(5)+f(3)+f(2)+f(2) must be <= 12, and 12 > 10.
    # Let's trace:
    # f(2) = max(f(1)+f(0)+f(0)+f(0), 2) = max(2+0+0+0, 2) = 2.
    # f(5) = max(f(2)+f(1)+f(1)+f(1), 5) = max(2+2+2+2, 5) = 8.
    # f(10) = max(f(5)+f(3)+f(2)+f(2), 10) -> need f(3).
    # f(3) = max(f(1)+f(1)+f(0)+f(0), 3) = max(4, 3) = 4.
    # So f(10) = max(8 + 4 + 2 + 2, 10) = max(16, 10) = 16? 
    # But the assertion says 12.
    # Ah, the problem statement implies integer division (floor) is usually intended in such problems (like Project Euler 116 style), 
    # BUT the problem explicitly says `n/2`, `n/3` etc. which in Python 3 is float division.
    # However, looking at the standard version of this problem (often found in coding challenges), 
    # the arguments to the recursive calls are typically `int(n/2)`, `int(n/3)`, etc.
    # Let's re-read the prompt equation: `f(n/2) + f(n/3) + f(n/4) + f(n/5)`.
    # If we use float division, f(60) = 106. 
    # Let's try with integer division (floor) logic, as float division usually leads to infinite recursion towards small floats unless floored.
    # Actually, if we don't floor, n/2 becomes 5.0, then 2.5, then 1.25... it never hits 0 cleanly without a specific check or floor.
    # Given the assertions, this is almost certainly the "integer division" variant of the problem 
    # where the inputs to the subproblems are the integer part of the division.
    # Standard interpretation for this specific problem (Project Euler 116 is different, but this specific recurrence is common):
    # f(n) = max( f(n//2) + f(n//3) + f(n//4) + f(n//5), n )
    # Let's verify with integer division (//).

    # Verification with Integer Division (//):
    # f(2) = max(f(1)+f(0)+f(0)+f(0), 2)
    # f(1) = max(f(0)+f(0)+f(0)+f(0), 1) = max(0,1) = 1.
    # f(2) = max(1+0+0+0, 2) = 2. (Matches assertion)

    # f(10) = max(f(5)+f(3)+f(2)+f(2), 10)
    # f(5) = max(f(2)+f(1)+f(1)+f(1), 5) = max(2+1+1+1, 5) = 5. (Wait, 5 is not greater than 5, so 5)
    # f(3) = max(f(1)+f(1)+f(0)+f(0), 3) = max(1+1+0+0, 3) = 3.
    # f(2) = 2.
    # f(10) = max(5 + 3 + 2 + 2, 10) = max(12, 10) = 12. (Matches assertion)

    # f(60) = max(f(30)+f(20)+f(15)+f(12), 60)
    # ... this seems to be the intended logic. The use of `/` in the prompt text is likely a representation of mathematical division 
    # implying integer parts for discrete recursive steps, or the prompt implies integer division semantics common in this specific algorithmic problem.
    # We will implement using integer division (floor) to satisfy the assertions.

    # Memoization dictionary
    memo = {}

    def _helper(current_n):
        if current_n == 0:
            return 0
        if current_n in memo:
            return memo[current_n]

        # Calculate components with integer division
        comp1 = _helper(current_n // 2)
        comp2 = _helper(current_n // 3)
        comp3 = _helper(current_n // 4)
        comp4 = _helper(current_n // 5)

        sum_of_parts = comp1 + comp2 + comp3 + comp4
        direct_value = current_n

        result = sum_of_parts if sum_of_parts > direct_value else direct_value

        memo[current_n] = result
        return result

    return _helper(int(n))

def get_max_sum(n):
    """
    Calculates the maximum sum possible using the recurrence relation:
    f(n) = max( f(n//2) + f(n//3) + f(n//4) + f(n//5), n )

    This function validates the input and ensures robust execution by handling edge cases
    and invalid inputs explicitly.

    Parameters:
    n (int): The integer input to compute the maximum sum for.

    Returns:
    int: The computed maximum sum.

    Raises:
    TypeError: If the input is not an integer.
    ValueError: If the input is negative.
    """
    # Step 1: Input Validation
    # Check for type. The problem implies integer inputs based on the assertions and nature of the recurrence.
    if not isinstance(n, int):
        raise TypeError(f"Input must be an integer, received {type(n).__name__}")

    # Check for negative values. The recurrence is undefined or trivial for negative numbers in this context.
    if n < 0:
        raise ValueError(f"Input must be non-negative, received {n}")

    # Step 2: Handle specific degenerate cases explicitly for clarity, though the helper covers them.
    if n == 0:
        return 0

    # Step 3: Compute and return the result using the helper function with memoization
    return _compute_recursive_sum(n)