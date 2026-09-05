import math

def otherside_rightangle(a, b):
    # Input validation
    if a <= 0 or b <= 0:
        raise ValueError("Sides must be positive numbers.")

    a_sq = a ** 2
    b_sq = b ** 2
    max_side_sq = max(a_sq, b_sq)
    sum_squares = a_sq + b_sq

    # Check if the given sides can form a valid right-angled triangle
    if max_side_sq >= sum_squares:
        raise ValueError("Given sides do not form a valid right-angled triangle.")

    # Identify the hypotenuse
    hypotenuse = max(a, b)
    other_side = min(a, b)

    # Calculate the third side
    if hypotenuse ** 2 == a_sq + b_sq:
        # Hypotenuse is correct, calculate the other side
        third_side = math.sqrt(sum_squares - max_side_sq)
    else:
        # Given sides are legs, calculate the hypotenuse
        third_side = math.sqrt(a_sq + b_sq)

    return third_side

# Test cases
print(f"Test case 1: otherside_rightangle(7, 8) should be 10.63014581273465")
print(f"Result: {otherside_rightangle(7, 8)}")
print(f"Test case 2: otherside_rightangle(3, 4) should be 5")
print(f"Result: {otherside_rightangle(3, 4)}")
print(f"Test case 3: otherside_rightangle(7, 15) should be 16.55294535724685")
print(f"Result: {otherside_rightangle(7, 15)}")