def max_volume(s):
    """
    Finds the maximum volume of a cuboid with sides a, b, c such that a + b + c = s.
    To maximize the volume V = a * b * c given a + b + c = s, the sides should 
    be as equal as possible (a = b = c = s/3).
    Since the problem implies integer dimensions (based on the test cases: 
    max_volume(8) -> sides (3, 3, 2) -> 3*3*2=18), we distribute the sum s 
    into three integers as evenly as possible.
    """
    if s < 3:
        return 0

    # Distribute the sum s into 3 parts as equally as possible
    a = s // 3
    b = (s - a) // 2
    c = s - a - b

    return a * b * c