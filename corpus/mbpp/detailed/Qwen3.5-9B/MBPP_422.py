def find_Average_Of_Cube(n: int) -> float:
    """
    Calculate the average of the cubes of the first n natural numbers.

    The formula for the sum of the first n natural numbers is: n * (n + 1) / 2
    The formula for the sum of the cubes of the first n natural numbers is: [n * (n + 1) / 2] ** 2

    The average is calculated as: (Sum of cubes) / n

    Args:
        n (int): The number of first natural numbers to consider.

    Returns:
        float: The average of the cubes of the first n natural numbers.

    Raises:
        ValueError: If n is not a positive integer.
        TypeError: If n is not of integer type.
    """

    # Step 1: Input validation - Type check
    if not isinstance(n, int):
        # Explicitly raise an error if the input is not an integer
        raise TypeError(f"Input must be an integer, but received {type(n).__name__}.")

    # Step 2: Input validation - Value check
    # Natural numbers are positive integers (1, 2, 3, ...).
    if n <= 0:
        raise ValueError(f"Input must be a positive integer (n >= 1), but received {n}.")

    # Step 3: Calculate the sum of the first n natural numbers
    # Formula: S_n = n * (n + 1) / 2
    sum_of_natural_numbers = n * (n + 1) // 2

    # Step 4: Calculate the sum of the cubes of the first n natural numbers
    # Formula: Sum of cubes = (Sum of n natural numbers) ** 2
    sum_of_cubes = sum_of_natural_numbers ** 2

    # Step 5: Calculate the average
    # Average = Sum of cubes / n
    average_value = sum_of_cubes / n

    return average_value