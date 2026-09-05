import math

def surfacearea_cone(r, h):
    slant_height = math.sqrt(r**2 + h**2)
    lateral_surface_area = math.pi * r * slant_height
    base_area = math.pi * r**2
    total_surface_area = lateral_surface_area + base_area
    return round(total_surface_area, 10)