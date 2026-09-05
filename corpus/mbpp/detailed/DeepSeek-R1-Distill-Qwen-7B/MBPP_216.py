def check_subset_list(a, b):
    # Validate inputs
    if a is None or b is None:
        return False
    if not isinstance(a, list) or not isinstance(b, list):
        return False
    # Handle edge cases
    if not a:
        return True
    if not b:
        return False

    # Convert to sets for efficient lookup
    a_sets = [set(sublist) for sublist in a]
    b_sets = [set(sublist) for sublist in b]

    # Check if all sublists in a are present in b
    for a_set in a_sets:
        if a_set not in b_sets:
            return False
    return True