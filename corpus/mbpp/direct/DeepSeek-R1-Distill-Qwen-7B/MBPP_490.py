def extract_symmetric(lst):
    seen = set()
    result = set()
    for pair in lst:
        a, b = pair
        if (b, a) in seen:
            result.add(pair)
        else:
            seen.add((a, b))
    return result

# Example usage and test cases
# assert extract_symmetric([(6, 7), (2, 3), (7, 6), (9, 8), (10, 2), (8, 9)] ) == {(8, 9), (6, 7)}
# assert extract_symmetric([(7, 8), (3, 4), (8, 7), (10, 9), (11, 3), (9, 10)] ) == {(9, 10), (7, 8)}
# assert extract_symmetric([(8, 9), (4, 5), (9, 8), (11, 10), (12, 4), (10, 11)] ) == {(8, 9), (10, 11)}