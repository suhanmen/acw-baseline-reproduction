def count_first_elements(t):
    for i, elem in enumerate(t):
        if isinstance(elem, (tuple, list)) and len(elem) > 0:
            continue
        else:
            return i
    return 0

# Example usage:
# assert count_first_elements((1, 5, 7, (4, 6), 10)) == 3
# assert count_first_elements((2, 9, (5, 7), 11)) == 2
# assert count_first_elements((11, 15, 5, 8, (2, 3), 8)) == 4