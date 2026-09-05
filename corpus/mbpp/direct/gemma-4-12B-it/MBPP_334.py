def check_Validity(a, b, c):
    """
    Checks whether the given three sides can form a valid triangle.
    A triangle is valid if the sum of any two sides is greater than the third side.
    """
    return (a + b > c) and (a + c > b) and (b + c > a)

if __name__ == "__main__":
    assert check_Validity(1, 2, 3) == False
    assert check_Validity(2, 3, 5) == False
    assert check_Validity(7, 10, 5) == True