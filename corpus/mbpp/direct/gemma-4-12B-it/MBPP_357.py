def find_max(records):
    """
    Finds the maximum element across all tuples in a list of tuples.
    """
    if not records:
        return None

    max_val = float('-inf')
    for record in records:
        for element in record:
            if element > max_val:
                max_val = element
    return max_val

if __name__ == "__main__":
    assert find_max([(2, 4), (6, 7), (5, 1), (6, 10), (8, 7)]) == 10
    assert find_max([(3, 5), (7, 8), (6, 2), (7, 11), (9, 8)]) == 11
    assert find_max([(4, 6), (8, 9), (7, 3), (8, 12), (10, 9)]) == 12