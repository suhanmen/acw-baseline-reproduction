import math

def distance_lat_long(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """
    Calculates the great-circle distance between two points on the Earth 
    surface given their latitudes and longitudes in decimal degrees.

    Uses the Haversine formula.

    Args:
        lat1: Latitude of the first point in decimal degrees.
        lon1: Longitude of the first point in decimal degrees.
        lat2: Latitude of the second point in decimal degrees.
        lon2: Longitude of the second point in decimal degrees.

    Returns:
        float: The distance between the two points in kilometers.

    Raises:
        TypeError: If any input is not a float or an integer.
        ValueError: If latitude is outside [-90, 90] or longitude outside [-180, 180].
    """

    # --- Input Validation ---
    inputs = [lat1, lon1, lat2, lon2]
    for val in inputs:
        if not isinstance(val, (int, float)):
            raise TypeError(f"All inputs must be numeric. Received: {type(val)}")

    if not (-90.0 <= lat1 <= 90.0):
        raise ValueError(f"Latitude 1 must be between -90 and 90. Received: {lat1}")
    if not (-90.0 <= lat2 <= 90.0):
        raise ValueError(f"Latitude 2 must be between -90 and 90. Received: {lat2}")
    if not (-180.0 <= lon1 <= 180.0):
        raise ValueError(f"Longitude 1 must be between -180 and 180. Received: {lon1}")
    if not (-180.0 <= lon2 <= 180.0):
        raise ValueError(f"Longitude 2 must be between -180 and 180. Received: {lon2}")

    # --- Constants ---
    # Earth's mean radius in kilometers
    EARTH_RADIUS_KM = 6371.0

    # --- Conversion to Radians ---
    # The trigonometric functions in Python's math module expect radians.
    def degrees_to_radians(degrees: float) -> float:
        return degrees * (math.pi / 180.0)

    lat1_rad = degrees_to_radians(lat1)
    lon1_rad = degrees_to_radians(lon1)
    lat2_rad = degrees_to_radians(lat2)
    lon2_rad = degrees_to_radians(lon2)

    # --- Haversine Formula Calculation ---
    # Formula:
    # a = sin²(Δlat/2) + cos(lat1) * cos(lat2) * sin²(Δlon/2)
    # c = 2 * atan2( √a, sqrt(1-a) )
    # d = R * c

    delta_lat = lat2_rad - lat1_rad
    delta_lon = lon2_rad - lon1_rad

    # Calculate the square of half the chord length between the points
    sin_half_delta_lat = math.sin(delta_lat / 2.0)
    sin_half_delta_lon = math.sin(delta_lon / 2.0)

    term1 = sin_half_delta_lat ** 2
    term2 = math.cos(lat1_rad) * math.cos(lat2_rad) * (sin_half_delta_lon ** 2)

    a = term1 + term2

    # Handle potential floating point precision errors where 'a' might slightly exceed 1.0
    if a > 1.0:
        a = 1.0
    elif a < 0.0:
        a = 0.0

    # Calculate the angular distance in radians
    # atan2 is used for better numerical stability than acos
    c = 2.0 * math.atan2(math.sqrt(a), math.sqrt(1.0 - a))

    # Final distance in kilometers
    distance_km = EARTH_RADIUS_KM * c

    return distance_km

if __name__ == "__main__":
    # Verification of requirements
    assert math.isclose(distance_lat_long(23.5, 67.5, 25.5, 69.5), 12179.372041317429, rel_tol=1e-9)
    assert math.isclose(distance_lat_long(10.5, 20.5, 30.5, 40.5), 6069.397933300514, rel_tol=1e-9)
    assert math.isclose(distance_lat_long(10, 20, 30, 40), 6783.751974994595, rel_tol=1e-9)