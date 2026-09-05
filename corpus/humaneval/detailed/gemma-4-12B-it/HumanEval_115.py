def max_fill(grid, capacity):
    import math

    """
    You are given a rectangular grid of wells. Each row represents a single well,
    and each 1 in a row represents a single unit of water.
    Each well has a corresponding bucket that can be used to extract water from it, 
    and all buckets have the same capacity.
    Your task is to use the buckets to empty the wells.
    Output the number of times you need to lower the buckets.

    Example 1:
        Input: 
            grid : [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
            bucket_capacity : 1
        Output: 6

    Example 2:
        Input: 
            grid : [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
            bucket_capacity : 2
        Output: 5

    Example 3:
        Input: 
            grid : [[0,0,0], [0,0,0]]
            bucket_capacity : 5
        Output: 0

    Constraints:
        * all wells have the same length
        * 1 <= grid.length <= 10^2
        * 1 <= grid[0].length <= 10^2
        * grid[i][j] -> 0 | 1
        * 1 <= capacity <= 10
    """

    # --- Input Validation ---
    if not isinstance(grid, list) or not isinstance(capacity, int):
        raise ValueError("Invalid input types: grid must be a list and capacity must be an integer.")

    if not grid:
        return 0

    if capacity <= 0:
        raise ValueError("Bucket capacity must be a positive integer.")

    # Ensure all rows are lists and have the same length
    first_row_len = len(grid[0])
    if not isinstance(grid[0], list):
        raise ValueError("Grid must be a list of lists.")

    for row in grid:
        if not isinstance(row, list):
            raise ValueError("Each well (row) must be a list.")
        if len(row) != first_row_len:
            raise ValueError("All wells must have the same length.")

    def calculate_buckets_for_well(well_data, bucket_cap):
        """
        Calculates how many times a bucket must be lowered to empty a specific well.
        A '1' represents one unit of water.
        """
        total_water_units = 0
        for unit in well_data:
            # Only count units of water (1s)
            if unit == 1:
                total_water_units += 1
            elif unit != 0:
                # Handle unexpected values in grid
                pass 

        if total_water_units == 0:
            return 0

        # The number of buckets is the ceiling of (total_water / bucket_capacity)
        # Because we need a full or partial bucket for every unit of water, 
        # but the problem logic implies we process the well's total water 
        # with a bucket of a certain capacity.
        # Example 2 clarifies: row [1,1,1,1] with capacity 2 results in 2 buckets.
        # row [0,1,1,1] with capacity 2 results in 2 buckets (3 units / 2 = 1.5 -> 2).

        num_buckets = math.ceil(total_water_units / bucket_cap)
        return num_buckets

    total_bucket_lowers = 0

    # --- Processing Logic ---
    for well in grid:
        # Calculate buckets needed for the current well
        buckets_needed = calculate_buckets_for_well(well, capacity)

        # Accumulate the result
        total_bucket_lowers += buckets_needed

    return total_bucket_lowers