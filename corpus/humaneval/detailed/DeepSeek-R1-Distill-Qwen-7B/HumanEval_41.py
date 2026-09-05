def car_race_collision(n: int) -> int:
    """
    Determines the number of collisions between two groups of cars moving in opposite directions.

    Args:
        n (int): The number of cars in each group.

    Returns:
        int: The total number of collisions.

    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Number of cars cannot be negative.")

    # Calculate the number of collisions
    collisions = n * n

    return collisions