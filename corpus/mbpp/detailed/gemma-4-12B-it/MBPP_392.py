from typing import Dict

def get_max_sum(n: int) -> int:
    """
    Finds the maximum sum possible by using the recurrence:
    f(n) = max((f(n/2) + f(n/3) + f(n/4) + f(n/5)), n)
    where n/k is integer division.

    Args:
        n (int): The input number for the recursive calculation.

    Returns:
        int: The maximum sum calculated.

    Raises:
        ValueError: If n is negative or not an integer.
    """
    # Input Validation
    if not isinstance(n, int):
        raise ValueError("Input must be an integer.")

    if n < 0:
        raise ValueError("Input must be a non-negative integer.")

    # Memoization dictionary to store results of subproblems
    # Key: n (int), Value: result of f(n) (int)
    memo: Dict[int, int] = {}

    def solve_recursive(current_n: int) -> int:
        """
        Helper function to perform the recursive calculation with memoization.
        """
        # Base case: The problem implies f(n) = n for small values 
        # where the sum of previous terms is less than n.
        # However, the recursive definition f(n) = max(sum, n)
        # naturally handles the base case for n=0 and n=1.
        if current_n == 0:
            return 0
        if current_n == 1:
            return 1

        # Check if value is already computed
        if current_n in memo:
            return memo[current_n]

        # Calculate the values for the four branches: n/2, n/3, n/4, n/5
        # Using integer division as implied by standard competitive programming
        # and the logic of the recursive formula provided.
        val_div_2 = solve_recursive(current_n // 2)
        val_div_3 = solve_recursive(current_n // 3)
        val_div_4 = solve_recursive(current_n // 4)
        val_div_5 = solve_recursive(current_n // 5)

        # Sum the results of the branches
        combined_sum = val_div_2 + val_div_3 + val_div_4 + val_div_5

        # The recurrence relation is f(n) = max(f(n/2) + f(n/3) + f(n/4) + f(n/5), n)
        # We determine the final value for the current n.
        result = max(combined_sum, current_n)

        # Store result in memoization table
        memo[current_n] = result
        return result

    # Initial call to the recursive helper
    return solve_recursive(n)

# Assertions to verify the correctness of the implementation
if __name__ == "__main__":
    assert get_max_sum(60) == 106
    assert get_max_sum(10) == 12
    assert get_max_sum(2) == 2