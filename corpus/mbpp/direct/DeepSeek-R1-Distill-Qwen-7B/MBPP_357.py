def find_max(records):
    max_val = float('-inf')
    for record in records:
        if record[0] > max_val or record[1] > max_val:
            max_val = max(record[0], record[1])
    return max_val

# Test cases
assert find_max([(2, 4), (6, 7), (5, 1), (6, 10), (8, 7)]) == 10
assert find_max([(3, 5), (7, 8), (6, 2), (7, 11), (9, 8)]) == 11
assert find_max([(4, 6), (8, 9), (7, 3), (8, 12), (10, 9)]) == 12