import math

def otherside_rightangle(a, b):
    """
    Finds the hypotenuse of a right-angled triangle given the two legs.
    Based on the provided test cases:
    (7, 8) -> 10.6301... (sqrt(7^2 + 8^2))
    (3, 4) -> 5 (sqrt(3^2 + 4^2))
    (7, 15) -> 16.5529... (sqrt(7^2 + 15^2))
    """
    return math.sqrt(a**2 + b**2)