def any_int(x, y, z):
    # Check if all inputs are numbers
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float)) and isinstance(z, (int, float))):
        return False

    # Check if all inputs are integers
    if not (isinstance(x, int) and isinstance(y, int) and isinstance(z, int)):
        return False

    # Check if any number is the sum of the other two
    if (x == y + z) or (y == x + z) or (z == x + y):
        return True

    # If none satisfy the condition
    return False