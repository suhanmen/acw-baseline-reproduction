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

    def is_integer_type(value):
        """
        Helper to check if a value is an integer.
        Note: We use type() check or isinstance(x, int) but must ensure 
        it is not a boolean, as bool is a subclass of int in Python.
        """
        # Check if the input is specifically an int type and not a bool
        if isinstance(value, int) and not isinstance(value, bool):
            return True

        # Also check if the value is a float that represents a whole number?
        # The prompt says "all numbers are integers", which usually implies 
        # the data type must be int, or specifically that the value is a whole number.
        # Given the example any_int(3.6, -2.2, 2) ➞ False, 
        # we must ensure the inputs are of the integer type.
        return False

    # Step 1: Validate that all three inputs are strictly integers.
    # This handles the "all numbers are integers" constraint first.
    inputs = [x, y, z]
    all_are_integers = True

    for item in inputs:
        if not is_integer_type(item):
            all_are_integers = False
            break

    if not all_are_integers:
        return False

    # Step 2: Check the mathematical condition.
    # One number must be equal to the sum of the other two.
    # There are three possible combinations:
    # 1. x = y + z
    # 2. y = x + z
    # 3. z = x + y

    sum_y_z = y + z
    is_x_sum_of_others = (x == sum_y_z)

    sum_x_z = x + z
    is_y_sum_of_others = (y == sum_x_z)

    sum_x_y = x + y
    is_z_sum_of_others = (z == sum_x_y)

    # Step 3: Evaluate the final condition.
    # If any of the conditions are met, return True.
    if is_x_sum_of_others or is_y_sum_of_others or is_z_sum_of_others:
        return True
    else:
        return False