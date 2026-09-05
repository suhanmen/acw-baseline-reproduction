import math

def area_pentagon(side_length):
    """
    Calculates the area of a regular pentagon given its side length.
    The formula for the area of a regular pentagon is:
    Area = (1/4) * sqrt(5 * (5 + 2 * sqrt(5))) * side_length^2
    Alternatively: Area = (side_length^2 * n) / (4 * tan(pi / n))
    For n=5, Area = (5 * side_length^2) / (4 * tan(pi / 5))
    """
    n = 5
    area = (n * side_length**2) / (4 * math.tan(math.pi / n))
    return area

if __name__ == "__main__":
    assert math.isclose(area_pentagon(5), 43.01193501472417)
    assert math.isclose(area_pentagon(10), 172.0477400588967)
    assert math.isclose(area_pentagon(15), 387.10741513251753)