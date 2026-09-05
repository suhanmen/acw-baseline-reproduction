def check_Triangle(x1, y1, x2, y2, x3, y3):
    # Helper function to calculate the Euclidean distance between two points
    def distance(x, y, a, b):
        return ((a - x) ** 2 + (b - y) ** 2) ** 0.5

    # Calculate the distances between each pair of points
    d1 = distance(x1, y1, x2, y2)
    d2 = distance(x1, y1, x3, y3)
    d3 = distance(x2, y2, x3, y3)

    # Check the triangle inequality theorem for all three sides
    if (d1 + d2 > d3) and (d1 + d3 > d2) and (d2 + d3 > d1):
        return 'Yes'
    else:
        return 'No'