from typing import List, Tuple, Set

def extract_symmetric(data: List[Tuple[int, int]]) -> Set[Tuple[int, int]]:
    """
    Identifies pairs in a list of tuples that have a symmetric counterpart.
    A pair (a, b) is symmetric if (b, a) also exists in the list.
    The function returns a set of pairs where the pair (a, b) is included 
    only if (b, a) exists, but the pair (b, a) is NOT the same as (a, b) 
    (i.e., it excludes self-symmetric pairs like (1, 1) unless specified 
    otherwise, though the test cases imply we want the first occurrence 
    of the pair that has a twin).

    Based on the provided assertions:
    Input: [(6, 7), (2, 3), (7, 6), (9, 8), (10, 2), (8, 9)]
    Symmetric pairs are (6, 7) and (7, 6), and (9, 8) and (8, 9).
    The expected output is {(8, 9), (6, 7)}. 
    This implies we return one representative of each symmetric pair.
    Specifically, if (a, b) and (b, a) both exist, we pick the one that 
    appears first in the list, but only if a != b.
    """

    # Validation: Ensure the input is a list
    if not isinstance(data, list):
        raise TypeError("Input must be a list of tuples.")

    # Validation: Ensure all elements are tuples of length 2
    for item in data:
        if not isinstance(item, tuple) or len(item) != 2:
            raise ValueError("Each element in the list must be a tuple of two integers.")
        if not all(isinstance(x, int) for x in item):
            raise ValueError("Tuple elements must be integers.")

    # To handle the "return one representative" logic:
    # We need to know which pairs have a symmetric counterpart.
    # A pair (a, b) has a symmetric counterpart if (b, a) is in the list.

    # Convert input list to a set for O(1) lookups
    # We use a set of tuples to check for existence efficiently.
    pair_pool = set(data)

    # Result set to store unique representative pairs
    symmetric_results: Set[Tuple[int, int]] = set()

    # To ensure we only add the representative and not both (a, b) and (b, a),
    # and to respect the order of discovery, we can track what we have seen.
    seen_pairs: Set[Tuple[int, int]] = set()

    for current_pair in data:
        first_val = current_pair[0]
        second_val = current_pair[1]

        # A pair is symmetric if its reverse exists in the pool
        # AND the pair is not self-symmetric (e.g., (1, 1))
        # Looking at assertions: (6, 7) and (7, 6) are symmetric.
        # The output contains (6, 7) and (8, 9).

        # Check if the reverse exists
        reversed_pair = (second_val, first_val)

        is_symmetric = (
            reversed_pair in pair_pool and 
            first_val != second_val
        )

        if is_symmetric:
            # We only want to add one representative of the symmetric pair.
            # If we encounter (6, 7) and (7, 6), we should only add one.
            # The assertions suggest that if (a, b) and (b, a) exist, 
            # we pick the one that appeared first in the list.

            # Check if we have already processed this "symmetry group"
            # A symmetry group is {(a, b), (b, a)}
            if current_pair not in seen_pairs and reversed_pair not in seen_pairs:
                symmetric_results.add(current_pair)
                # Mark both as seen so we don't add the other one later
                seen_pairs.add(current_pair)
                seen_pairs.add(reversed_pair)

    return symmetric_results