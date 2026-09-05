def extract_symmetric(tuples_list):
    seen = set()
    symmetric_pairs = set()
    for t in tuples_list:
        reversed_t = (t[1], t[0])
        if reversed_t in tuples_list and t not in seen and reversed_t not in seen:
            symmetric_pairs.add(tuple(sorted(t)))
            seen.add(t)
            seen.add(reversed_t)
    return symmetric_pairs