def get_row(lst, x):
    """Get coordinates of integer x in nested list lst.
    Coordinates are tuples (row, column), starting from 0.
    Sorted by rows in ascending order, then columns in descending order within each row."""

    # List to hold all (row, column) tuples
    coordinates = []

    # Iterate through each row index
    for row_idx, row in enumerate(lst):
        # Check if current row contains the value x
        if x in row:
            # Determine the columns where x is found
            columns = [col_idx for col_idx, val in enumerate(row) if val == x]
            # Add tuples for each found column in this row
            for col_idx in columns:
                coordinates.append((row_idx, col_idx))

    # If no coordinates found, return empty list
    if not coordinates:
        return []

    # Sort the coordinates by row in ascending order
    coordinates.sort(key=lambda coord: coord[0])

    # Within each row, sort columns in descending order
    for row in coordinates:
        row_sorted = sorted([col for col in range(len(lst[row[0]])) if lst[row[0]][col] == x], reverse=True)
        # Update the coordinates with the new sorted columns
        new_coords = []
        for r, c in row:
            if c in row_sorted:
                new_coords.append((r, c))
        coordinates = coordinates[:row[0]] + new_coords

    return coordinates