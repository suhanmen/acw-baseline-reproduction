import math

def surfacearea_cone(radius, height):
    """
    Calculates the surface area of a cone given its radius and height.
    The formula is: Area = pi * r * (r + sqrt(r^2 + h^2))
    """
    slant_height = math.sqrt(radius**2 + height**2)
    surface_area = math.pi * radius * (radius + slant_height)
    return surface_area

if __name__ == "__main__":
    assert math.isclose(surfacearea_cone(5, 12), 282.7433388230814)
    assert math.isclose(surfacearea_cone(10, 15), 880.5179353159282)
    assert math.isclose(surfacearea_cone(19, 17), 2655.923961165254)