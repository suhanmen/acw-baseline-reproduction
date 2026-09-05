def adjacent_num_product(numbers):
    if len(numbers) < 2:
        return None  # Assuming the list must have at least two elements
    max_product = numbers[0] * numbers[1]
    for i in range(1, len(numbers) - 1):
        current_product = numbers[i] * numbers[i + 1]
        if current_product > max_product:
            max_product = current_product
    return max_product