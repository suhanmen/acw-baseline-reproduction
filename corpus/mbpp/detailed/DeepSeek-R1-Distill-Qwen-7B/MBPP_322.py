def position_min(numbers):
    if not numbers:
        raise ValueError("The input list cannot be empty.")

    min_val = min(numbers)
    indices = []

    for index, value in enumerate(numbers):
        if value == min_val:
            indices.append(index)

    return indices