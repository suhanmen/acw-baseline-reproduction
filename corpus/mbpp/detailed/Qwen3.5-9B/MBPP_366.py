def adjacent_num_product(numbers):
    """
    Finds the largest product of a pair of adjacent elements in a list of integers.

    Args:
        numbers (list[int]): A list of integers.

    Returns:
        int: The largest product of any two adjacent elements.

    Raises:
        ValueError: If the input list contains fewer than two elements.
        TypeError: If the input is not a list or contains non-integer elements.
    """

    # Step 1: Validate the input type is a list
    if not isinstance(numbers, list):
        raise TypeError(f"Input must be a list of integers, got {type(numbers).__name__} instead.")

    # Step 2: Validate the length of the list is sufficient (at least 2 elements)
    if len(numbers) < 2:
        raise ValueError(
            f"Input list must contain at least two elements to form a pair. "
            f"Received a list of length: {len(numbers)}."
        )

    # Step 3: Validate that all elements are integers (or numeric types that behave like integers)
    for index, value in enumerate(numbers):
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError(
                f"All elements must be integers. Element at index {index} is of type {type(value).__name__}."
            )

    # Step 4: Initialize variables to track the maximum product found so far.
    # We start with the product of the first pair (index 0 and 1).
    current_max_product = numbers[0] * numbers[1]

    # Step 5: Iterate through the list starting from the second pair (index 1 and 2).
    # We use range(len(numbers) - 1) to stop before the last index,
    # so that 'i' and 'i+1' are always valid indices.
    for index in range(len(numbers) - 1):
        # Calculate the product of the current adjacent pair
        current_product = numbers[index] * numbers[index + 1]

        # Compare the current product with the stored maximum
        if current_product > current_max_product:
            current_max_product = current_product

    # Step 6: Return the calculated maximum product
    return current_max_product