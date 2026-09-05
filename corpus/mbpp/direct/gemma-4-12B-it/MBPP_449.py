def check_Triangle(x1, y1, x2, y2, x3, y3):
    """
    Checks whether three given points form a valid triangle.
    A triangle is valid if the three points are not collinear and 
    do not represent the same point.
    """
    # Calculate the area of the triangle using the coordinates formula:
    # Area = 0.5 * |x1(y2 - y3) + x2(y3 - y1) + x3(y1 - y2)|
    # If the area is 0, the points are collinear and do not form a triangle.
    area = 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))

    if area > 0:
        return 'Yes'
    else:
        return 'No'