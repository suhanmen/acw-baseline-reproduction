from typing import Any, List


def validate_input(input_list: Any) -> None:
    """
    Validates that the input is a list and does not raise an error for any list content.
    Raises a ValueError if the input is not a list.
    """
    if not isinstance(input_list, list):
        raise ValueError("Input must be a list.")


def _build_combinations_recursive(
    items: List[Any],
    current_index: int,
    current_combination: List[Any],
    all_combinations: List[List[Any]],
) -> None:
    """
    Recursively builds all possible combinations.

    The strategy used here is slightly different from the standard 'include/exclude at each step'
    approach to match the specific ordering of the provided assertions.

    The specific ordering observed in the problem statement is:
    1. The empty set is always first.
    2. All combinations of size 1 are listed in the order of their appearance in the input.
    3. All combinations of size 2 are listed. Within size 2, the order is:
       - Element 0 paired with Element 1, 2, ...
       - Element 1 paired with Element 2, ...
       - Element 2 paired with Element 3, ...
       (This corresponds to picking the 'first' element of the combination from the input
       and then picking the 'second' element from the remaining elements to its right.)
    4. This pattern continues for all sizes up to n.

    Algorithm Logic:
    - Start with the empty combination.
    - Iterate through every possible length 'k' from 1 to n.
    - For a fixed length 'k', generate combinations by iterating through the input list.
      Let the outer loop index be 'i' (the index of the first element of the combination).
      Let the inner loop index be 'j' (the index of the second element, if k>=2).
      Generally, for the m-th element in the combination (0-indexed m), we pick from
      elements in the input list at index >= previous_index.

    To implement this robustly and match the output exactly:
    We will use a recursive helper that, given the current depth in the combination
    and the starting index in the input list, attempts to pick an element.

    However, a simpler iterative approach that matches the visual pattern in the assertions
    is to generate combinations of length k, and ensure that for length k, the first element
    is chosen from index i, the second from j > i, etc.

    Let's refine the approach to match the specific output order:
    Input: [A, B, C]
    Expected: [], [A], [B], [C], [A,B], [A,C], [B,C], [A,B,C]

    Order of generation based on length k:
    k=1: A, B, C (Indices: 0, 1, 2)
    k=2: A,B, A,C, B,C (Indices: (0,1), (0,2), (1,2))
    k=3: A,B,C (Indices: (0,1,2))

    This implies that for a fixed size k, we iterate the first element index 'i' from 0 to n-k.
    Then we recursively or iteratively find combinations of size k-1 from the sublist starting at i+1.

    Let's implement a helper that generates combinations of a specific size 'size' 
    starting from a specific 'start_index'.
    """
    n = len(items)

    # Add the empty combination immediately
    if len(all_combinations) == 0:
        all_combinations.append([])

    # We will iterate through every possible size of the combination: 1 to n
    for combination_size in range(1, n + 1):
        # Generate all combinations of this specific size
        _generate_combinations_of_size(
            items, 
            start_index=0, 
            current_size=combination_size, 
            current_combo=[], 
            all_combinations=all_combinations
        )


def _generate_combinations_of_size(
    items: List[Any],
    start_index: int,
    current_size: int,
    current_combo: List[Any],
    all_combinations: List[List[Any]],
) -> None:
    """
    Generates combinations of a specific size using backtracking.

    Parameters:
    - items: The original list of items.
    - start_index: The index in 'items' from which we can start picking the next element.
    - current_size: The target number of elements to pick for this specific iteration.
    - current_combo: The list of items selected so far.
    - all_combinations: The master list to store the results.
    """
    remaining_items_count = len(items) - start_index

    # If the remaining items are not enough to fulfill the current_size, stop.
    if remaining_items_count < current_size:
        return

    # If we have already picked enough items to match the target size, save it.
    if len(current_combo) == current_size:
        # Create a deep copy to ensure immutability in the list of lists
        combo_copy: List[Any] = current_combo.copy()
        all_combinations.append(combo_copy)
        return

    # Base case: if size is 0, we just return (handled by the check above usually)
    if current_size <= 0:
        return

    # Iterate through available items starting from start_index
    for i in range(start_index, len(items)):
        # Pick item at index i
        current_combo.append(items[i])

        # Recursive step: find the rest of the items starting from i + 1
        _generate_combinations_of_size(
            items, 
            start_index=i + 1, 
            current_size=current_size - 1, 
            current_combo=current_combo, 
            all_combinations=all_combinations
        )

        # Backtrack: remove the last added item
        current_combo.pop()