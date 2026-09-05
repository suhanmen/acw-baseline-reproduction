def check_Triangle(x1, y1, x2, y2, x3, y3):
    # Calculate the squared distances between the points
    a_sq = (x1 - x2)**2 + (y1 - y2)**2
    b_sq = (x2 - x3)**2 + (y2 - y3)**2
    c_sq = (x3 - x1)**2 + (y3 - y1)**2

    # Check the triangle inequality theorem for all three combinations
    if (a_sq + b_sq > c_sq) and (b_sq + c_sq > a_sq) and (c_sq + a_sq > b_sq):
        return 'Yes'
    else:
        return 'No'