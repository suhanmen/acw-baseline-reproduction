import math

def iscube(a):
    '''
    Write a function that takes an integer a and returns True 
    if this integer is a cube of some integer number.
    '''
    if a == 0:
        return True
    # Determine the sign of a
    sign = 1 if a > 0 else -1
    abs_a = abs(a)
    # Compute cube root of absolute value
    cube_root = abs_a ** (1/3)
    # Round to nearest integer
    n = round(cube_root)
    # Check if n cubed equals a
    if n ** 3 == abs_a * sign:
        return True
    else:
        # Check nearby integers due to floating point precision
        # For example, if cube_root is very close to n+1, check that
        # but given that rounding already occurs, the initial check might suffice
        # However, adding these checks can cover cases where floating point precision fails
        if (n + 1) ** 3 == abs_a * sign:
            return True
        if (n - 1) ** 3 == abs_a * sign:
            return True
        return False