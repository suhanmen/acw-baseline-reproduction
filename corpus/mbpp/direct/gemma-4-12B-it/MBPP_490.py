def extract_symmetric(pairs_list):
    """
    Extracts all pairs which have a symmetric counterpart in the given tuple list.
    The result contains only one of the pair from each symmetric set, 
    specifically the one that appeared first in the input list.
    """
    seen = set()
    result = set()
    # We use a set to track pairs that have already been 'matched' 
    # so we don't include both (a, b) and (b, a) in the output.
    matched = set()

    for first, second in pairs_list:
        pair = (first, second)
        reverse_pair = (second, first)

        if reverse_pair in seen and pair not in matched:
            result.add(pair)
            matched.add(pair)

        seen.add(pair)

    # The problem's assertions imply that we return the first occurrence 
    # of the pair that has a symmetric counterpart.
    # Let's refine the logic to match the exact expected output.

    # Re-evaluating based on test cases: 
    # [(6, 7), (2, 3), (7, 6), (9, 8), (10, 2), (8, 9)] -> {(8, 9), (6, 7)}
    # (6, 7) and (7, 6) exist. (9, 8) and (8, 9) exist.
    # Only the pair appearing earlier in the list is kept.

    final_result = set()
    found_pairs = set()

    # Pass 1: Identify all pairs that have a symmetric counterpart
    all_pairs = [tuple(p) for p in pairs_list]
    pair_set = set(all_pairs)

    # Pass 2: Collect the first occurrence of a pair that has a reverse in the set
    # but ensure we don't pick both (a, b) and (b, a) if both are in the list.
    processed = set()
    for p in all_pairs:
        rev = (p[1], p[0])
        if rev in pair_set and p not in processed:
            # If both (a, b) and (b, a) exist, we need to decide which one.
            # The test cases suggest the one that appears earlier.
            # However, if both (6,7) and (7,6) are there, and (6,7) is first, 
            # we add (6,7) and mark both as 'handled' to avoid (7,6) later.
            if p not in final_result:
                final_result.add(p)
                processed.add(p)
                processed.add(rev)
            else:
                processed.add(p)

    # Wait, the logic above is slightly flawed for the specific set logic.
    # Let's look at the expected output again: {(8, 9), (6, 7)}
    # (6, 7) is index 0, (7, 6) is index 2. (6, 7) is kept.
    # (9, 8) is index 3, (8, 9) is index 5. (9, 8) is NOT kept, (8, 9) is.
    # This means the rule is: Keep the pair (a, b) if (b, a) exists, 
    # but only if (a, b) is the one that is "mirrored" by something that came before it?
    # No, let's look at (8, 9) and (9, 8). (9, 8) is at index 3. (8, 9) is at index 5.
    # The output is {(8, 9), (6, 7)}. 
    # (6, 7) is index 0. (7, 6) is index 2. 
    # (9, 8) is index 3. (8, 9) is index 5.
    # It seems it keeps the pair that appears LATER in the list if its reverse appeared EARLIER.

    # Let's try: Keep pair p if its reverse was already seen.
    final_result = set()
    seen_so_far = set()
    for p in pairs_list:
        rev = (p[1], p[0])
        if rev in seen_so_far:
            final_result.add(p)
        seen_so_far.add(p)

    return final_result