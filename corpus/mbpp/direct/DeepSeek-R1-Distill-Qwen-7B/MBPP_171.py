def perimeter_pentagon(sides):
    if sides < 5:
        raise ValueError("A pentagon must have exactly 5 sides.")
    return 5 * sides

# Explanation of the solution:
# A pentagon has 5 sides of equal length. Therefore, the perimeter is calculated by multiplying the length of one side by 5.