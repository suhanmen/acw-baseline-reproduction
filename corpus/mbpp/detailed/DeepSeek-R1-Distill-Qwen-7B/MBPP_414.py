def overlapping(seq1, seq2):
    """
    Check if two sequences have any common elements.

    Args:
        seq1 (iterable): The first sequence to check.
        seq2 (iterable): The second sequence to check.

    Returns:
        bool: True if sequences have at least one common element, False otherwise.
    """
    # Validate inputs by converting them to sets
    set1 = set(seq1)
    set2 = set(seq2)

    # Handle cases where either sequence is empty
    if not set1 or not set2:
        return False

    # Convert sequences to sets to find common elements
    unique_elements1 = set1
    unique_elements2 = set2

    # Check for intersection
    common_elements = unique_elements1 & unique_elements2

    # Return True if there are common elements, False otherwise
    return len(common_elements) > 0

# Test the function with the provided assertions
assert overlapping([1,2,3,4,5],[6,7,8,9]) == False
assert overlapping([1,2,3],[4,5,6]) == False
assert overlapping([1,4,5],[1,4,5]) == True