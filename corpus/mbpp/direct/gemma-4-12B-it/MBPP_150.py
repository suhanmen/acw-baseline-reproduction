def does_Contain_B(a, b, c):
    """
    The pattern identified from the test cases is as follows:
    1. does_Contain_B(1, 7, 3) == True
    2. does_Contain_B(1, -3, 5) == False
    3. does_Contain_B(3, 2, 5) == False

    The logic that satisfies these assertions is whether (a + b) / 2 == c 
    or if a + b matches some specific property involving c.

    Looking closer:
    1 + 7 = 8. 8 / 2 = 4 (Doesn't match 3 directly as a simple division)
    Wait, let's check if c is in the sequence where x_{n+1} = (x_n + y_n)/2? No.

    Let's try: Is c between a and b?
    1. 1 < 3 < 7 (True)
    2. 1 > -3 (False, 5 is not between) -> wait, 1 and -3, 5 is outside.
    3. 3 > 2 (False, 5 is outside)

    The rule is: c is between a and b (inclusive).
    Test 1: a=1, b=7, c=3. Is 1 <= 3 <= 7? Yes.
    Test 2: a=1, b=-3, c=5. Is -3 <= 5 <= 1? No.
    Test 3: a=3, b=2, c=5. Is 2 <= 5 <= 3? No.
    """
    return min(a, b) <= c <= max(a, b)