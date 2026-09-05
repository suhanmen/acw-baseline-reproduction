from typing import List, Tuple, Any

def _validate_colors(colors: List[Any]) -> bool:
    """
    Validates that the provided list of colors is a non-empty list.
    Returns True if valid, False otherwise.
    """
    if not isinstance(colors, list):
        return False

    if len(colors) == 0:
        return False

    # All items must be hashable (tuples, strings, numbers, etc.) to be used in a set
    for item in colors:
        if not isinstance(item, (str, int, float, bool, type(None))):
            # While technically hashable, we restrict to common types for clarity
            # and to prevent issues if unhashable types (like lists) were passed.
            pass 
        # Note: We do not strictly enforce hashability here as strings and tuples 
        # are the primary expected types based on the problem, but we ensure 
        # the list itself is not empty.

    return True

def _validate_count(count: int) -> bool:
    """
    Validates that the specified number of colors to choose is a non-negative integer.
    Returns True if valid, False otherwise.
    """
    if not isinstance(count, int):
        return False

    if isinstance(count, bool):
        # Python bool is a subclass of int, but we usually don't want booleans as counts
        return False

    if count < 0:
        return False

    return True

def _generate_combinations_with_repetition(
    colors: List[Any], 
    k: int
) -> List[Tuple[Any, ...]]:
    """
    Generates all combinations of length k from the given colors list with repetition allowed.
    The combinations are generated in lexicographical order based on the input order of colors.
    Uses an explicit iterative approach (generalized counting) instead of recursion 
    to avoid stack overflow on large k and to make the steps very explicit.

    Logic:
    1. If k is 0, return a list containing one empty tuple.
    2. Initialize the first combination with the first k elements (all 0-indexed).
    3. Iterate indefinitely, generating the next combination until we wrap around (index goes out of bounds).
    4. At each step, find the rightmost element that can be incremented.
    5. Increment that element and reset all elements to its right to 0.
    6. If no element can be incremented (we wrapped around the last element), stop.
    """

    n_colors = len(colors)

    # Edge case: k is 0
    if k == 0:
        return [()]

    # Initialize indices
    indices = [0] * k

    result = []

    # Helper to create a tuple from current indices
    def get_current_combination() -> Tuple[Any, ...]:
        return tuple(colors[i] for i in indices)

    # Generate the first combination
    result.append(get_current_combination())

    while True:
        # Find the rightmost index that can be incremented
        # We look from the last index backwards
        i = k - 1
        while i >= 0 and indices[i] == n_colors - 1:
            i -= 1

        # If i is -1, we have exhausted all combinations
        if i == -1:
            break

        # Increment the found index
        indices[i] += 1

        # Reset all indices to the right of i to 0
        for j in range(i + 1, k):
            indices[j] = 0

        # Add the new combination to results
        result.append(get_current_combination())

    return result

def combinations_colors(colors: List[Any], k: int) -> List[Tuple[Any, ...]]:
    """
    Chooses a specified number of colours from a given list of three different colours
    and generates all the combinations with repetitions.

    The output list contains tuples, where each tuple represents one combination.
    The combinations are generated in lexicographical order according to the order
    of colors in the input list.

    Parameters:
    colors (List[Any]): A list of color names or identifiers.
    k (int): The number of colors to choose for each combination.

    Returns:
    List[Tuple[Any, ...]]: A list of tuples, each representing a unique combination.

    Raises:
    ValueError: If input validation fails.
    """

    # Step 1: Validate inputs explicitly
    valid_colors = _validate_colors(colors)
    if not valid_colors:
        raise ValueError("The 'colors' argument must be a non-empty list.")

    valid_count = _validate_count(k)
    if not valid_count:
        raise ValueError("The 'k' argument must be a non-negative integer.")

    # Step 2: Handle edge case where k is 0 explicitly before calling generator
    if k == 0:
        return [()]

    # Step 3: Generate the combinations using the helper function
    combinations = _generate_combinations_with_repetition(colors, k)

    return combinations