def extract_min_max(t, k):
    if k == 0:
        return ()
    # Get the sorted tuple
    sorted_t = sorted(t)
    # Extract the minimum k elements and the maximum k elements
    min_elements = sorted_t[:k]
    max_elements = sorted_t[-k:]
    # Combine the min and max elements, removing duplicates by using a set
    combined = list(set(min_elements + max_elements))
    # If k is 1, return only the single element without duplicates
    if k == 1:
        return tuple(sorted(combined))
    else:
        # Sort the combined list
        combined.sort()
        # Return the combined elements as a tuple
        return tuple(combined)

# Test the function with the given examples
assert extract_min_max((5, 20, 3, 7, 6, 8), 2) == (3, 5, 8, 20)
assert extract_min_max((4, 5, 6, 1, 2, 7), 3) == (1, 2, 4, 5, 6, 7)
assert extract_min_max((2, 3, 4, 8, 9, 11, 7), 4) == (2, 3, 4, 7, 8, 9, 11)