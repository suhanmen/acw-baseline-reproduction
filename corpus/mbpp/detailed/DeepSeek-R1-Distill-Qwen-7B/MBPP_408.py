def k_smallest_pairs(array_a, array_b, k):
    # Handle empty arrays
    if not array_a or not array_b:
        return []

    # Calculate the number of possible pairs
    total_pairs = len(array_a) * len(array_b)

    # If k is larger than the total number of pairs, return all pairs
    if k >= total_pairs:
        return cartesian_product(array_a, array_b)

    # Generate all possible pairs
    all_pairs = cartesian_product(array_a, array_b)

    # Sort the pairs based on their sum and then by the first element
    sorted_pairs = sort_pairs(all_pairs)

    # Return the first k pairs
    return sorted_pairs[:k]

def cartesian_product(array_a, array_b):
    return [(a, b) for a in array_a for b in array_b]

def sort_pairs(pairs):
    # Sort by the sum of the pair, then by the first element
    return sorted(pairs, key=lambda x: (x[0] + x[1], x[0]))

# Test the function
print(k_smallest_pairs([1,3,7], [2,4,6], 2))   # [[1, 2], [1, 4]]
print(k_smallest_pairs([1,3,7], [2,4,6], 1))   # [[1, 2]]
print(k_smallest_pairs([1,3,7], [2,4,6], 7))   # [[1, 2], [1, 4], [3, 2], [1, 6], [3, 4], [3, 6], [7, 2]]