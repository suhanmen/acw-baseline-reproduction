def multiply_num(numbers):
    if not isinstance(numbers, tuple):
        return None

    if not numbers:  # Empty tuple
        return None

    if len(numbers) == 1:  # Single element
        return float(numbers[0])

    product = 1
    for num in numbers:
        product *= num

    return product / len(numbers)