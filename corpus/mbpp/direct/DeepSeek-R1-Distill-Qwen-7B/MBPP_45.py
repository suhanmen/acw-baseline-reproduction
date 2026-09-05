def get_gcd(arr):
    """
    Find the greatest common divisor (GCD) of the elements in the given array.
    """
    import math
    current_gcd = arr[0]
    for number in arr[1:]:
        current_gcd = math.gcd(current_gcd, number)
        if current_gcd == 1:
            break  # GCD can't be lower than 1
    return current_gcd