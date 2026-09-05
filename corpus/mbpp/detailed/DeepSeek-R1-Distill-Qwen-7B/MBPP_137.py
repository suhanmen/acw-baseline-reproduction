def zero_count(arr):
    # Validate input
    if not isinstance(arr, list):
        raise ValueError("Input must be a list of integers.")
    for num in arr:
        if not isinstance(num, int):
            raise ValueError("All elements in the list must be integers.")

    # Handle empty list case
    if len(arr) == 0:
        return 0.0

    # Count zeroes
    zero_count = 0
    for num in arr:
        if num == 0:
            zero_count += 1

    # Calculate ratio
    ratio = zero_count / len(arr)

    return ratio