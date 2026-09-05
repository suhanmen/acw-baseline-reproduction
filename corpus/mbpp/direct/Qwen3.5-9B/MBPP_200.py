def position_max(numbers):
    if not numbers:
        return []
    max_value = max(numbers)
    return [i for i, val in enumerate(numbers) if val == max_value]