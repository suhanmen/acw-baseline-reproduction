def iscube(a):
    '''
    Write a function that takes an integer a and returns True 
    if this ingeger is a cube of some integer number.
    Note: you may assume the input is always valid.
    Examples:
    iscube(1) ==> True
    iscube(2) ==> False
    iscube(-1) ==> True
    iscube(64) ==> True
    iscube(0) ==> True
    iscube(180) ==> False
    '''
    # Use round to handle potential floating point precision issues
    # abs(a) is used because the cube root of a negative number 
    # is the negative of the cube root of its absolute value.
    root = round(abs(a) ** (1/3))

    # Check both positive and negative roots since the input can be negative
    if root**3 == abs(a):
        return True

    # In some edge cases (like 125), floating point precision might 
    # result in root-1 or root+1, so we check adjacent integers.
    for i in range(root - 1, root + 2):
        if i**3 == a:
            return True

    return False