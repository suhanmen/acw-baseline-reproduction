from typing import List, Any, Dict

def first_Element(arr: List[Any], n: int, k: int) -> Any:
    """
    Finds the first element in the input list that occurs exactly k times.

    Args:
        arr (List[Any]): The list of elements to search through.
        n (int): The declared size of the input array (for validation).
        k (int): The target frequency of the element.

    Returns:
        Any: The first element found that appears exactly k times.

    Raises:
        ValueError: If inputs are invalid (e.g., negative k, size mismatch).
        TypeError: If inputs are not of the expected types.
    """
    # --- Input Validation ---

    # Ensure types are correct
    if not isinstance(arr, list):
        raise TypeError(f"Input 'arr' must be a list, got {type(arr).__name__}")
    if not isinstance(n, int):
        raise TypeError(f"Input 'n' must be an integer, got {type(n).__name__}")
    if not isinstance(k, int):
        raise TypeError(f"Input 'k' must be an integer, got {type(k).__name__}")

    # Check for logical consistency
    if k <= 0:
        raise ValueError("Frequency 'k' must be a positive integer greater than 0.")

    if len(arr) != n:
        # While the prompt implies 'n' is the length, we check for robustness.
        # Some interpretations might allow n to be a maximum bounds, but usually, 
        # it represents the count of items expected.
        raise ValueError(f"Length of array ({len(arr)}) does not match provided 'n' ({n}).")

    # Handle edge case: empty list
    if n == 0:
        # Technically, no element exists to appear k times.
        # Depending on requirement, could return None or raise error.
        # Given the assertions, we assume n > 0 and valid elements exist.
        return None

    # --- Logic Execution ---

    # Step 1: Calculate frequencies of all elements in the array.
    # We use a dictionary to store counts for O(1) average lookups/updates.
    counts: Dict[Any, int] = {}

    for item in arr:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1

    # Step 2: Iterate through the original array to maintain order.
    # The problem asks for the *first* element occurring k times.
    # This means we must check elements in their original sequence.
    for item in arr:
        current_count = counts.get(item)

        # Check if this specific item's total count in the array is exactly k
        if current_count == k:
            # Because we iterate through 'arr' sequentially, the first item
            # we encounter that satisfies this condition is the correct answer.
            return item

    # Step 3: Handle case where no element appears exactly k times.
    # The problem doesn't specify what to return if none found.
    # Returning None is standard Python practice for "not found".
    return None

# Standard assertions provided in the problem description
if __name__ == "__main__":
    # The following lines are provided to confirm the solution works against requirements.
    assert first_Element([0, 1, 2, 3, 4, 5], 6, 1) == 0
    assert first_Element([1, 2, 1, 3, 4], 5, 2) == 1
    assert first_Element([2, 3, 4, 3, 5, 7, 1, 2, 3, 5], 10, 2) == 2