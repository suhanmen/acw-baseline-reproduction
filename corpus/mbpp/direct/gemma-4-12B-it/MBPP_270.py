def sum_even_and_even_index(numbers, n):
    """
    Calculates the sum of even numbers that are located at even indices
    within the first n elements of a list.

    Indices are 0-based (0, 2, 4, ...).
    """
    total_sum = 0
    # Iterate through the list up to n, checking even indices
    for i in range(0, n, 2):
        # Check if the number at the even index is even
        if numbers[i] % 2 == 0:
            total_sum += numbers[i]
    return total_sum