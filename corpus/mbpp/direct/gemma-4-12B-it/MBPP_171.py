def perimeter_pentagon(side_length):
    """
    Calculates the perimeter of a regular pentagon given the length of one side.
    A pentagon has 5 equal sides.
    """
    return side_length * 5

if __name__ == "__main__":
    assert perimeter_pentagon(5) == 25
    assert perimeter_pentagon(10) == 50
    assert perimeter_pentagon(15) == 75