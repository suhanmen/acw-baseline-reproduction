def count_bidirectional(tuples_list):
    seen = set()
    count = 0
    for a, b in tuples_list:
        if (b, a) in seen:
            count += 1
        else:
            seen.add((a, b))
    return count

# Test cases
print(count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 1), (6, 5), (2, 1)]))  # Output: 3
print(count_bidirectional([(5, 6), (1, 3), (6, 5), (9, 1), (6, 5), (2, 1)]))  # Output: 2
print(count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 2), (6, 5), (2, 1)]))  # Output: 4