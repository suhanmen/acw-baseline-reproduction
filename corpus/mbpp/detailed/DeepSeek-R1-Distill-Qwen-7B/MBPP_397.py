def median_numbers(a, b, c):
    # Verify exactly three arguments are provided
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float))):
        raise TypeError("All inputs must be numbers")

    # Sort the three numbers
    sorted_numbers = sorted([a, b, c])

    # The median is the second element in the sorted list
    median = sorted_numbers[1]

    # Return the median as a float
    return float(median)