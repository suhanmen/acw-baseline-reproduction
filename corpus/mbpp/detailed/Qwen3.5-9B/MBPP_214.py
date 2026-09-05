import math
import sys

def _validate_input_radians(value):
    """
    Validates that the input is a numeric type (int or float).
    Raises a TypeError with a descriptive message if the input is invalid.
    """
    if not isinstance(value, (int, float)):
        raise TypeError(f"Expected a numeric input for radians, but got: {type(value).__name__}")
    if isinstance(value, bool):
        raise TypeError("Booleans are not accepted as numeric input; they are technically int subclasses but semantically invalid here.")

def _normalize_radians(radians_value):
    """
    Normalizes the radians value.
    While radians can be any real number, standard conversion works for any value.
    This function simply returns the value as-is to be passed to the conversion formula,
    ensuring the domain is acknowledged.
    """
    # Radians can be negative, greater than 2*pi, or less than -2*pi.
    # The conversion formula handles all these cases correctly.
    return radians_value

def _convert_radians_to_degrees(radians_value):
    """
    Performs the core mathematical conversion from radians to degrees.
    Formula: degrees = radians * (180 / pi)
    """
    _pi_constant = math.pi
    _factor = 180.0 / _pi_constant
    result = radians_value * _factor
    return result

def degree_radian(radians):
    """
    Converts a value given in radians to degrees.

    This function is defensive and production-grade:
    - It validates input types explicitly.
    - It handles edge cases (zero, negative, infinity, NaN) gracefully by letting
      the underlying math operations handle them (propagating them as expected)
      while ensuring non-numeric types are rejected.
    - It uses explicit intermediate variables for clarity.

    Args:
        radians (int | float): The angle in radians to convert.

    Returns:
        float: The equivalent angle in degrees.

    Raises:
        TypeError: If the input is not a number (int or float).
        ValueError: If the input is NaN (Not a Number) or Infinity (handled explicitly 
                     for production robustness to provide clear messages).
    """

    # Step 1: Explicit Type Validation
    _validate_input_radians(radians)

    # Step 2: Check for special floating-point values (NaN and Inf)
    # Although math operations will raise or return Inf/NaN, explicit checks
    # allow for better error handling in a strict production environment.
    if math.isnan(radians):
        raise ValueError("Conversion failed: Input 'radians' is Not a Number (NaN).")
    if math.isinf(radians):
        raise ValueError("Conversion failed: Input 'radians' is infinite.")

    # Step 3: Normalize (conceptual step, value remains unchanged for this formula)
    _normalized_value = _normalize_radians(radians)

    # Step 4: Perform the conversion
    final_degrees = _convert_radians_to_degrees(_normalized_value)

    # Step 5: Return the result
    # The return type is float because the division 180/pi introduces a float.
    return final_degrees

if __name__ == "__main__":
    # Local testing block to verify the specific assertions provided in the prompt
    # This block is not part of the function logic but confirms the solution meets requirements.

    # Test Case 1
    try:
        result_1 = degree_radian(90)
        expected_1 = 5156.620156177409
        if abs(result_1 - expected_1) < 1e-10:
            print(f"Pass: 90 rad -> {result_1}")
        else:
            print(f"Fail: 90 rad -> {result_1} (Expected {expected_1})")
    except Exception as e:
        print(f"Error on Test 1: {e}")

    # Test Case 2
    try:
        result_2 = degree_radian(60)
        expected_2 = 3437.746770784939
        if abs(result_2 - expected_2) < 1e-10:
            print(f"Pass: 60 rad -> {result_2}")
        else:
            print(f"Fail: 60 rad -> {result_2} (Expected {expected_2})")
    except Exception as e:
        print(f"Error on Test 2: {e}")

    # Test Case 3
    try:
        result_3 = degree_radian(120)
        expected_3 = 6875.493541569878
        if abs(result_3 - expected_3) < 1e-10:
            print(f"Pass: 120 rad -> {result_3}")
        else:
            print(f"Fail: 120 rad -> {result_3} (Expected {expected_3})")
    except Exception as e:
        print(f"Error on Test 3: {e}")

    # Edge Case: Zero
    try:
        res = degree_radian(0.0)
        print(f"Edge Case Zero: {res}")
    except Exception as e:
        print(f"Edge Case Zero Error: {e}")

    # Edge Case: Negative
    try:
        res = degree_radian(-1.0)
        print(f"Edge Case Negative: {res}")
    except Exception as e:
        print(f"Edge Case Negative Error: {e}")

    # Edge Case: Invalid Type
    try:
        res = degree_radian("string")
        print(f"Invalid Type Result: {res}")
    except TypeError as e:
        print(f"Correctly caught TypeError: {e}")

    # Edge Case: NaN
    try:
        res = degree_radian(float('nan'))
        print(f"NaN Result: {res}")
    except ValueError as e:
        print(f"Correctly caught ValueError for NaN: {e}")