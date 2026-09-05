def sum_even_and_even_index(lst):
    # Input validation
    if not isinstance(lst, list):
        raise ValueError("Input must be a list.")

    # Initialize sum
    sum_result = 0

    # Iterate through the list with index
    for index, value in enumerate(lst):
        # Check if the index is even
        if index % 2 == 0:
            # Check if the value is even
            if value % 2 == 0:
                sum_result += value

    return sum_result

# Test cases
assert sum_even_and_even_index([5, 6, 12, 1, 18, 8], 6) == 30
assert sum_even_and_even_index([3, 20, 17, 9, 2, 10, 18, 13, 6, 18], 10) == 26
assert sum_even_and_even_index([5, 6, 12, 1], 4) == 12