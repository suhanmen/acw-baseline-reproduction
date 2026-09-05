def max_sum(triangle, row):
    """
    Find the maximum sum in the given right triangle of numbers.
    """
    current_row = [triangle[i][j] for i in range(row)]
    max_row = current_row.copy()

    for i in range(1, row):
        for j in range(len(max_row)):
            max_row[j] = max(max_row[j], max_row[j-1] + triangle[i][j])

    return max(max_row)

# Example usage:
print(max_sum([[1], [2,1], [3,3,2]], 3))  # Output: 6
print(max_sum([[1], [1, 2], [4, 1, 12]], 3))  # Output: 15
print(max_sum([[2], [3,2], [13,23,12]], 3))   # Output: 28