from typing import List

def _validate_input(n: int) -> None:
    """
    Validates that the input is a positive integer.

    Args:
        n: The input value to validate.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is not a positive integer (n <= 0).
    """
    if not isinstance(n, int):
        raise TypeError(f"Input must be an integer. Received: {type(n).__name__}")

    if n <= 0:
        raise ValueError(f"Input must be a positive integer (n > 0). Received: {n}")

def make_a_pile(n: int) -> List[int]:
    """
    Given a positive integer n, you have to make a pile of n levels of stones.
    The first level has n stones.
    The number of stones in the next level is:
        - the next odd number if n is odd.
        - the next even number if n is even.
    Return the number of stones in each level in a list, where element at index
    i represents the number of stones in the level (i+1).

    Examples:
    >>> make_a_pile(3)
    [3, 5, 7]
    """
    # Defensive programming: Validate the input before proceeding
    _validate_input(n)

    # Handle the case where n is 0 (though validation handles this, 
    # for completeness of logic, n=0 would result in an empty list).
    if n == 0:
        return []

    # Initialize the result list.
    # The first level starts with n stones.
    levels: List[int] = []

    # The first level is always n.
    current_stones = n
    levels.append(current_stones)

    # We need to generate a total of n levels.
    # Since we already added the first level, we iterate n-1 more times.
    for _ in range(1, n):
        # Determine the logic for the next stone count based on the current level's stones.
        # If the current level's stone count is odd, the next is the next odd number (+2).
        # If the current level's stone count is even, the next is the next even number (+2).
        # In both cases (odd/even), the "next" number of the same parity is current + 2.

        # Example walkthrough:
        # n=3 (odd): 3 -> next odd is 5 -> next odd is 7. List: [3, 5, 7]
        # n=4 (even): 4 -> next even is 6 -> next even is 8 -> next even is 10. List: [4, 6, 8, 10]

        next_stones = current_stones + 2

        # Update the current stones and append to the result.
        current_stones = next_stones
        levels.append(current_stones)

    return levels