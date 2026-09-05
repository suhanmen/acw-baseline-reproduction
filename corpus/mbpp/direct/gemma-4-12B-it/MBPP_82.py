import math

def volume_sphere(radius: float) -> float:
    """
    Calculates the volume of a sphere given its radius.
    Formula: V = (4/3) * pi * r^3
    """
    volume = (4/3) * math.pi * (radius ** 3)
    return volume

if __name__ == "__main__":
    assert volume_sphere(10) == 4188.790204786391
    assert volume_sphere(25) == 65449.84694978735
    assert volume_sphere(20) == 33510.32163829113