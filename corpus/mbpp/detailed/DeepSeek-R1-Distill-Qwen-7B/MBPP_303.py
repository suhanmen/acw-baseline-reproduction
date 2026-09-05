def solve(list_a, list_b):
    """
    Check if the number of inversions in two lists are the same.

    Args:
        list_a (list): First list to check.
        list_b (list): Second list to check.

    Returns:
        bool: True if inversion counts are equal, False otherwise.
    """
    # Validate inputs
    if not isinstance(list_a, list) or not isinstance(list_b, list):
        return False
    if len(list_a) != len(list_b):
        return False

    # Helper function to count inversions in a single list
    def count_inversions(lst):
        inversion_count = 0
        n = len(lst)
        for i in range(n):
            for j in range(i + 1, n):
                if lst[i] > lst[j]:
                    inversion_count += 1
        return inversion_count

    # Count inversions for both lists
    inversions_a = count_inversions(list_a)
    inversions_b = count_inversions(list_b)

    # Compare the inversion counts
    return inversions_a == inversions_b