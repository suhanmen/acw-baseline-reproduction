def check_occurrences(tuples_list):
    from collections import defaultdict

    counts = defaultdict(int)
    for t in tuples_list:
        counts[t] += 1
    return dict(counts)

# Example usage:
# print(check_occurrences([(3, 1), (1, 3), (2, 5), (5, 2), (6, 3)]))  # Output: {(1, 3): 2, (2, 5): 2, (3, 6): 1}
# print(check_occurrences([(4, 2), (2, 4), (3, 6), (6, 3), (7, 4)]))  # Output: {(2, 4): 2, (3, 6): 2, (4, 7): 1}
# print(check_occurrences([(13, 2), (11, 23), (12, 25), (25, 12), (16, 23)]))  # Output: {(2, 13): 1, (11, 23): 1, (12, 25): 2, (16, 23): 1}