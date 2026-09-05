def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.

    Examples
    any_int(5, 2, 7) ➞ True

    any_int(3, 2, 2) ➞ False

    any_int(3, -2, 1) ➞ True

    any_int(3.6, -2.2, 2) ➞ False



    '''
    # Check if all types are exactly int (or satisfy integer check)
    # The prompt specifies "all numbers are integers". 
    # In Python, isinstance(True, int) is True, but typically we mean numeric integers.
    # Also, we must ensure they are not floats that happen to be whole numbers (like 3.0) 
    # unless the requirement allows them. Based on the example 3.6, 
    # the check should strictly ensure they are integers.

    if not (isinstance(x, int) and isinstance(y, int) and isinstance(z, int)):
        # Handling bools which are technically ints in Python, 
        # but usually not intended in such math problems.
        if any(isinstance(i, bool) for i in [x, y, z]):
            return False
        # If they are floats that are integers (e.g. 3.0), the example 3.6 
        # implies we should be careful. Usually "are integers" means type int.
        return False

    # Check the sum conditions
    cond1 = x == y + z
    cond2 = y == x + z
    cond3 = z == x + y

    return cond1 or cond2 or cond3