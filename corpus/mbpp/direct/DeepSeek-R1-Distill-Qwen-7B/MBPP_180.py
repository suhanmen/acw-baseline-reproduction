import math

def distance_lat_long(lat1, lon1, lat2, lon2):
    """
    Calculate the great-circle distance between two points on Earth using their latitude and longitude.
    """
    R = 6371  # Earth radius in kilometers
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    a = math.sin(delta_phi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = R * c
    return distance

# Test the function
assert abs(distance_lat_long(23.5,67.5,25.5,69.5) - 12179.372041317429) < 1e-9
assert abs(distance_lat_long(10.5,20.5,30.5,40.5) - 6069.397933300514) < 1e-9
assert abs(distance_lat_long(10,20,30,40) - 6783.751974994595) < 1e-9