def tuple_intersection(tuple_list_1, tuple_list_2):
    """
    Find the intersection of tuples in two lists, ignoring the order within each tuple.
    Tuples are considered equal if they contain the same elements regardless of order.
    Returns a set of tuples where each tuple is sorted to ensure consistent representation.
    """
    def normalize(t):
        # Sort elements of the tuple to make (a, b) equivalent to (b, a)
        return tuple(sorted(t))

    # Normalize all tuples in both lists and convert to sets for O(1) lookups
    set_1 = set(map(normalize, tuple_list_1))
    set_2 = set(map(normalize, tuple_list_2))

    # Compute intersection of normalized tuples
    intersection_normalized = set_1 & set_2

    # Convert back to standard tuples (already sorted from normalization)
    return tuple(sorted(intersection_normalized, key=lambda x: (x[0], x[1]))) if intersection_normalized else tuple_intersection.__annotations__.get('return', ()) or set()

# Re-implementing to match exact expected return type (set of tuples) as per assertions
def tuple_intersection(tuple_list_1, tuple_list_2):
    def normalize(t):
        return tuple(sorted(t))

    set_1 = set(map(normalize, tuple_list_1))
    set_2 = set(map(normalize, tuple_list_2))

    # Intersection
    intersection_normalized = set_1 & set_2

    # Convert back to regular tuples (sorted representation)
    result = set()
    for t in intersection_normalized:
        result.add(t)

    return result