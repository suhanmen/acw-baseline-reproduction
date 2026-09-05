def max_fill(grid, capacity):
    """
    You are given a rectangular grid of wells. Each row represents a single well,
    and each 1 in a row represents a single unit of water.
    Each well has a corresponding bucket that can be used to extract water from it, 
    and all buckets have the same capacity.
    Your task is to use the buckets to empty the wells.
    Output the number of times you need to lower the buckets.

    Requirements:
    - All rows must have the same length.
    - Capacity must be at least 1.
    - Non-zero grid dimensions are enforced.

    Args:
        grid: A list of lists, where each sublist represents a well.
        capacity: The capacity of each bucket.

    Returns:
        The total number of bucket lowers needed.

    Raises:
        ValueError: If grid is empty, or if capacity is less than 1.
    """
    # Validate input
    if not grid or not all(len(row) == len(grid[0]) for row in grid):
        raise ValueError("Invalid grid format")
    if capacity < 1:
        raise ValueError("Capacity must be at least 1")

    total_lowers = 0

    # Iterate through each well (row)
    for row in grid:
        # Count the number of water units in this well
        water_units = sum(row)
        if water_units == 0:
            continue  # No water to extract

        # Calculate the number of lowers needed for this well
        lowers = (water_units + capacity - 1) // capacity
        # Add to the total
        total_lowers += lowers

    return total_lowers