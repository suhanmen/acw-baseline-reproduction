def count_first_elements(elements):
    count = 0
    for element in elements:
        if isinstance(element, tuple):
            break
        count += 1
    return count

# Test the function with provided examples
assert count_first_elements((1, 5, 7, (4, 6), 10)) == 3
assert count_first_elements((2, 9, (5, 7), 11)) == 2
assert count_first_elements((11, 15, 5, 8, (2, 3), 8)) == 4