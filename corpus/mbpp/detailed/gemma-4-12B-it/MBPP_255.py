from typing import List, Tuple, Any

def combinations_colors(colors: List[str], n: int) -> List[Tuple[str, ...]]:
    """
    Generates all combinations with repetitions of a specified number of colors
    from a given list of available colors.

    Args:
        colors: A list of strings representing the available colors.
        n: The number of colors to choose for each combination.

    Returns:
        A list of tuples, where each tuple is a unique combination with repetition.
    """
    # --- Input Validation ---

    # Ensure the colors input is actually a list
    if not isinstance(colors, list):
        raise TypeError(f"Expected 'colors' to be a list, got {type(colors).__name__}")

    # Ensure the number of colors to choose (n) is an integer
    if not isinstance(n, int):
        raise TypeError(f"Expected 'n' to be an integer, got {type(n).__name__}")

    # Check for negative n
    if n < 0:
        raise ValueError("The number of colors to choose (n) cannot be negative.")

    # Handle the edge case where n is 0
    # A combination of 0 elements is an empty tuple
    if n == 0:
        return [()]

    # Handle the edge case where the input color list is empty but n > 0
    if len(colors) == 0:
        return []

    # --- Core Logic ---

    # To ensure the output matches the expected order (lexicographical based on 
    # original list indices), we work with the list indices rather than the values.
    # This prevents issues if the input list contains duplicate color names.

    result: List[Tuple[str, ...]] = []

    def generate_recursive(start_index: int, current_combination: List[str]) -> None:
        """
        A helper function to perform Depth-First Search to find combinations.

        Args:
            start_index: The index in the 'colors' list to start picking from.
            current_combination: The accumulation of colors picked so far.
        """
        # Base Case: If the combination has reached the desired length n,
        # add a tuple copy of it to our result list.
        if len(current_combination) == n:
            result.append(tuple(current_combination))
            return

        # Recursive Step: Iterate through the colors starting from 'start_index'.
        # Because repetitions are allowed, we do not increment start_index 
        # in the recursive call, allowing the same element to be picked again.
        for i in range(start_index, len(colors)):
            current_color = colors[i]

            # Choose the current color
            current_combination.append(current_color)

            # Recurse to pick the next color in the combination
            generate_recursive(i, current_combination)

            # Backtrack: Remove the last added color before the next iteration
            current_combination.pop()

    # Initiate the recursive generation
    generate_recursive(0, [])

    return result