def add_pairwise(numbers):
    # Input Validation
    if not isinstance(numbers, tuple):
        raise TypeError("Input must be a tuple of numbers.")

    # Check if the tuple has at least two elements
    if len(numbers) < 2:
        return ()

    # Convert all elements to integers
    try:
        numeric_tuple = tuple(int(x) for x in numbers)
    except ValueError:
        raise ValueError("All elements of the tuple must be integers.")

    # Edge Case Handling for all equal elements
    if all(x == numeric_tuple[0] for x in numeric_tuple):
        return tuple(numeric_tuple[0] for _ in numeric_tuple)

    # Pairwise Addition
    result = []
    for i in range(len(numeric_tuple) - 1):
        result.append(numeric_tuple[i] + numeric_tuple[i + 1])

    return tuple(result)