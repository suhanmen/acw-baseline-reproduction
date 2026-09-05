def multiply_int(a, b):
    # Handle the case where either a or b is zero
    if a == 0 or b == 0:
        return 0

    # Determine the sign of the result
    negative = False
    if (a < 0 and b > 0) or (a > 0 and b < 0):
        negative = True

    # Work with absolute values to simplify addition
    a = abs(a)
    b = abs(b)

    # Use bit manipulation to optimize the addition process
    result = 0
    while b > 0:
        # Add 'a' to the result if the least significant bit of 'b' is 1
        if b % 2 == 1:
            result += a
        # Double 'a' and halve 'b' for faster computation
        a <<= 1  # equivalent to a *= 2
        b >>= 1  # equivalent to b //= 2

    # Apply the sign to the result
    return -result if negative else result

# Test cases to validate the solution
assert multiply_int(10, 20) == 200, "Test case 1 failed"
assert multiply_int(5, 10) == 50, "Test case 2 failed"
assert multiply_int(4, 8) == 32, "Test case 3 failed"