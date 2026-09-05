import math

def degree_radian(radians: float) -> float:
    """
    Converts radians to degrees and returns the result.
    Note: The provided assertions indicate a specific multiplier 
    rather than the standard conversion (180/pi).
    To match the assertions:
    90 * X = 5156.620156177409 -> X = 57.2957794...
    Standard conversion is 180/pi = 57.295779...
    Wait, 90 radians converted to degrees is 90 * (180/pi) = 5156.62...
    So the function should perform standard radian to degree conversion.
    """
    return radians * (180 / math.pi)