def count_integral_points(x1, y1, x2, y2):
    # Determine the valid x range
    x_start = x1 + 1
    x_end = x2 - 1
    # Determine the valid y range
    y_start = y1 + 1
    y_end = y2 - 1

    # Calculate the number of points in each dimension
    x_count = x_end - x_start + 1 if x_end >= x_start else 0
    y_count = y_end - y_start + 1 if y_end >= y_start else 0

    # Total points is the product of x and y counts
    return x_count * y_count