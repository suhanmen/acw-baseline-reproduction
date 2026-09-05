import math

def lateralsuface_cylinder(radius, height):
    return 2 * math.pi * radius * height

# Example usage and assertions
# lateralsuface_cylinder(10, 5) should be approximately 314.15000000000003
# lateralsuface_cylinder(4, 5) should be approximately 125.66000000000001
# lateralsuface_cylinder(4, 10) should be approximately 251.32000000000002