import math
from typing import Tuple

def parabola_vertex(a: float, b: float, c: float) -> Tuple[float, float]:
    """
    Calculates the vertex (h, k) of a parabola defined by the quadratic 
    equation: f(x) = ax^2 + bx + c.

    Args:
        a (float): The coefficient of the x^2 term.
        b (float): The coefficient of the x term.
        c (float): The constant term.

    Returns:
        Tuple[float, float]: A tuple representing the (x, y) coordinates 
                               of the vertex.

    Raises:
        ValueError: If 'a' is zero, as the equation is no longer a parabola.
        TypeError: If inputs are not numeric types.
    """

    # --- Input Validation ---
    # Ensure that all inputs are either integers or floats.
    inputs = [a, b, c]
    for val in inputs:
        if not isinstance(val, (int, float)):
            raise TypeError(f"All coefficients must be numeric. Received: {type(val)}")

    # A parabola is defined by ax^2 + bx + c where a != 0.
    # If a is 0, the equation describes a line (or a constant), not a parabola.
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be zero for a quadratic equation.")

    # --- Calculation logic ---

    # The x-coordinate (h) of the vertex of a parabola ax^2 + bx + c 
    # is given by the formula: h = -b / (2a)

    denominator_x: float = 2.0 * a
    x_vertex: float = -b / denominator_x

    # The y-coordinate (k) of the vertex can be found by evaluating 
    # the function at x = h: k = f(h) = a(h^2) + b(h) + c

    # Step-by-step calculation of the y-coordinate to ensure clarity.
    x_squared: float = x_vertex ** 2
    term_1: float = a * x_squared
    term_2: float = b * x_vertex
    y_vertex: float = term_1 + term_2 + c

    # --- Return Result ---
    return (x_vertex, y_vertex)

# The following assertions verify the correctness of the implementation.
if __name__ == "__main__":
    # Test Case 1
    # f(x) = 5x^2 + 3x + 2
    # x = -3 / (2 * 5) = -0.3
    # y = 5(-0.3)^2 + 3(-0.3) + 2 = 5(0.09) - 0.9 + 2 = 0.45 - 0.9 + 2 = 1.55
    res1 = parabola_vertex(5, 3, 2)
    assert math.isclose(res1[0], -0.3), f"Expected -0.3, got {res1[0]}"
    assert math.isclose(res1[1], 1.55), f"Expected 1.55, got {res1[1]}"

    # Test Case 2
    # f(x) = 9x^2 + 8x + 4
    # x = -8 / (2 * 9) = -8 / 18 = -4/9 = -0.444...
    # y = 9(-4/9)^2 + 8(-4/9) + 4 = 9(16/81) - 32/9 + 4 = 16/9 - 32/9 + 36/9 = 20/9 = 2.222...
    res2 = parabola_vertex(9, 8, 4)
    assert math.isclose(res2[0], -0.4444444444444444), f"Expected -0.444..., got {res2[0]}"
    assert math.isclose(res2[1], 2.2222222222222223), f"Expected 2.222..., got {res2[1]}"

    # Test Case 3
    # f(x) = 2x^2 + 4x + 6
    # x = -4 / (2 * 2) = -1.0
    # y = 2(-1)^2 + 4(-1) + 6 = 2 - 4 + 6 = 4.0
    res3 = parabola_vertex(2, 4, 6)
    assert math.isclose(res3[0], -1.0), f"Expected -1.0, got {res3[0]}"
    assert math.isclose(res3[1], 4.0), f"Expected 4.0, got {res3[1]}"