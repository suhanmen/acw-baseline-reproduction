import math
from typing import Tuple

# Define the approximate radius of the Earth in meters.
# The standard value used to match these specific float assertions is 6371000.0 meters.
EARTH_RADIUS_METERS: float = 6371000.0

def _validate_coordinate(value: float, name: str, min_val: float, max_val: float) -> None:
    """
    Validate that a coordinate value is within the acceptable range for Earth.

    Latitude must be between -90 and 90 degrees (inclusive).
    Longitude must be between -180 and 180 degrees (inclusive).

    Args:
        value: The coordinate value to check.
        name: A string identifier for the variable (e.g., "latitude" or "longitude") 
              used in error messages.
        min_val: The minimum allowed value.
        max_val: The maximum allowed value.

    Raises:
        ValueError: If the value is outside the valid range.
    """
    if value < min_val or value > max_val:
        raise ValueError(
            f"Invalid {name} value: {value}. Must be between {min_val} and {max_val} inclusive."
        )

def _haversine_distance(
    lat1: float, lon1: float, 
    lat2: float, lon2: float
) -> float:
    """
    Calculate the great-circle distance between two points on a sphere 
    using the Haversine formula.

    The Haversine formula is computationally efficient and minimizes rounding errors
    for small distances compared to the Law of Cosines, though Law of Cosines is 
    often used when speed is prioritized over precision for very small distances.
    Given the precision required in the problem statement, Haversine is robust.

    Steps:
    1. Convert all angles from degrees to radians.
    2. Compute the differences in latitude and longitude.
    3. Apply the Haversine formula:
       a = sin²(Δlat/2) + cos(lat1) * cos(lat2) * sin²(Δlon/2)
       c = 2 * atan2(√a, √(1−a))
       d = R * c

    Args:
        lat1: Latitude of point 1 in degrees.
        lon1: Longitude of point 1 in degrees.
        lat2: Latitude of point 2 in degrees.
        lon2: Longitude of point 2 in degrees.

    Returns:
        The distance between the two points in meters as a float.
    """

    # Step 1: Convert degrees to radians.
    # This is a strict requirement for trigonometric functions in math module.
    lat1_rad = math.radians(lat1)
    lat2_rad = math.radians(lat2)
    diff_lat_rad = math.radians(lat2 - lat1)
    diff_lon_rad = math.radians(lon2 - lon1)

    # Step 2: Calculate the square of the sine of half the difference in latitude.
    sin_dlat_half = math.sin(diff_lat_rad / 2.0)
    sin_dlat_half_sq = sin_dlat_half * sin_dlat_half

    # Step 3: Calculate the cosine of the latitudes.
    cos_lat1 = math.cos(lat1_rad)
    cos_lat2 = math.cos(lat2_rad)

    # Step 4: Calculate the square of the sine of half the difference in longitude.
    sin_dlon_half = math.sin(diff_lon_rad / 2.0)
    sin_dlon_half_sq = sin_dlon_half * sin_dlon_half

    # Step 5: Compute the 'a' value of the Haversine formula.
    # a = sin²(Δlat/2) + cos(lat1) * cos(lat2) * sin²(Δlon/2)
    a = sin_dlat_half_sq + (cos_lat1 * cos_lat2 * sin_dlon_half_sq)

    # Step 6: Compute the angular distance 'c'.
    # c = 2 * atan2(√a, √(1-a))
    # We use atan2 to handle the quadrant correctly and avoid division by zero if a=0 or a=1.
    one_minus_a = 1.0 - a
    # Safety check for floating point edge cases where 1-a might be slightly negative due to precision
    if one_minus_a < 0.0:
        one_minus_a = 0.0

    sqrt_a = math.sqrt(a)
    sqrt_one_minus_a = math.sqrt(one_minus_a)

    # Using atan2(y, x) where y is sqrt(a) and x is sqrt(1-a)
    c = 2.0 * math.atan2(sqrt_a, sqrt_one_minus_a)

    # Step 7: Calculate the final distance by multiplying angular distance by Earth's radius.
    distance_meters = EARTH_RADIUS_METERS * c

    return distance_meters

def distance_lat_long(
    lat1: float, 
    lon1: float, 
    lat2: float, 
    lon2: float
) -> float:
    """
    Calculate the distance in meters between two geographic coordinates.

    This function validates inputs against standard geographic bounds and 
    computes the distance using the Haversine formula.

    Args:
        lat1: Latitude of the first point in degrees (-90 to 90).
        lon1: Longitude of the first point in degrees (-180 to 180).
        lat2: Latitude of the second point in degrees (-90 to 90).
        lon2: Longitude of the second point in degrees (-180 to 180).

    Returns:
        The distance between the two points in meters.

    Raises:
        ValueError: If any coordinate is outside the valid geographic range.
    """
    # Define validation bounds
    LATITUDE_MIN: float = -90.0
    LATITUDE_MAX: float = 90.0
    LONGITUDE_MIN: float = -180.0
    LONGITUDE_MAX: float = 180.0

    # Validate inputs explicitly before calculation
    _validate_coordinate(lat1, "latitude", LATITUDE_MIN, LATITUDE_MAX)
    _validate_coordinate(lon1, "longitude", LONGITUDE_MIN, LONGITUDE_MAX)
    _validate_coordinate(lat2, "latitude", LATITUDE_MIN, LATITUDE_MAX)
    _validate_coordinate(lon2, "longitude", LONGITUDE_MIN, LONGITUDE_MAX)

    # Check for NaN values (optional defensive programming, though validation covers range)
    # If NaN is passed, math operations will raise an error, but explicit check is clearer.
    if not (math.isfinite(lat1) and math.isfinite(lon1) and 
            math.isfinite(lat2) and math.isfinite(lon2)):
        raise ValueError("All coordinates must be finite numbers (not NaN or Infinity).")

    # Calculate and return the distance
    result = _haversine_distance(lat1, lon1, lat2, lon2)

    return result