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
        * 1 <= grid[:,1].length <= 10^2
        * grid[i][j] -> 0 | 1
        * 1 <= capacity <= 10
    """

    def validate_input(input_grid, input_capacity):
        """
        Validates the inputs according to the problem constraints and logic requirements.
        Raises a ValueError if the inputs are invalid.
        """
        # Check if grid is None
        if input_grid is None:
            raise ValueError("Grid cannot be None.")

        # Check if grid is an empty list
        if len(input_grid) == 0:
            raise ValueError("Grid cannot be empty.")

        # Check if capacity is not a positive integer
        if not isinstance(input_capacity, int) or input_capacity <= 0:
            raise ValueError("Capacity must be a positive integer.")

        # Check if each row in the grid is a list
        for i, row in enumerate(input_grid):
            if not isinstance(row, list):
                raise ValueError(f"Row at index {i} must be a list.")

            # Check if row is empty
            if len(row) == 0:
                raise ValueError(f"Row at index {i} cannot be empty.")

            # Check if all elements in the row are integers 0 or 1
            for j, val in enumerate(row):
                if not isinstance(val, int) or val not in (0, 1):
                    raise ValueError(f"Element at grid[{i}][{j}] must be 0 or 1, got {val}.")

    def calculate_water_units(well_row):
        """
        Calculates the total number of water units (1s) in a single well row.
        """
        water_count = 0
        for unit in well_row:
            water_count += unit
        return water_count

    def calculate_bucket_lowerings(water_units, capacity):
        """
        Calculates the number of times the bucket needs to be lowered to empty the well.
        Formula: ceil(water_units / capacity)
        """
        if capacity == 0:
            # Should be caught by validation, but added for safety in this helper
            raise ValueError("Capacity cannot be zero in calculation.")

        # Using integer arithmetic to simulate ceiling division
        # (a + b - 1) // b is equivalent to ceil(a / b) for positive integers
        if water_units > 0:
            return (water_units + capacity - 1) // capacity
        else:
            return 0

    # --- Main Logic Execution ---

    # Step 1: Validate inputs
    validate_input(grid, capacity)

    # Step 2: Initialize a variable to accumulate the total number of bucket lowerings
    total_lowerings = 0

    # Step 3: Iterate over each well (row) in the grid
    for well in grid:
        # Step 4: Calculate the total water units in the current well
        well_water_units = calculate_water_units(well)

        # Step 5: Calculate how many times the bucket must be lowered for this specific well
        lowerings_for_well = calculate_bucket_lowerings(well_water_units, capacity)

        # Step 6: Add the result for this well to the running total
        total_lowerings += lowerings_for_well

    # Step 7: Return the final accumulated result
    return total_lowerings