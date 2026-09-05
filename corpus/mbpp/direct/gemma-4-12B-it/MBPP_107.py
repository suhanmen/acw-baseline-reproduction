def count_Hexadecimal(start, end):
    """
    Counts the number of hexadecimal digits (0-9, A-F) 
    within a given range [start, end] inclusive.

    Wait, looking at the assertions:
    count_Hexadecimal(10, 15) == 6  -> 10, 11, 12, 13, 14, 15 (All are hex digits)
    count_Hexadecimal(2, 4) == 0    -> Wait, 2, 3, 4 are hex digits. 
    If the answer is 0, the problem refers to numbers that are *only* represented 
    by letters (A-F) or a specific definition of 'hexadecimal' numbers 
    in a sequence.

    Let's re-evaluate the assertions:
    - (10, 15) -> 6. These are 10, 11, 12, 13, 14, 15.
    - (2, 4) -> 0. These are 2, 3, 4.
    - (15, 16) -> 1. This is 15. 16 is not included? Or 15 is the only one?

    Wait, hex digits are 0-9 and A-F. 
    In many coding contexts, "Hexadecimal numbers" refers to numbers 
    expressed in base 16 that contain non-numeric characters (A-F).
    - 10-15 correspond to A-F (6 numbers).
    - 2-4 are numeric (0 numbers).
    - 15-16: 15 is F (1 number), 16 is 10 (numeric).

    Therefore, the function counts numbers in the range [start, end] 
    that, when converted to hex, consist only of letters (A-F) 
    or simply those values where the standard hex representation 
    is a single letter from A-F.

    However, looking at (10, 15) -> 6, these are values 10, 11, 12, 13, 14, 15.
    If the logic is "numbers x such that hex(x) is a letter", then:
    10 (A), 11 (B), 12 (C), 13 (D), 14 (E), 15 (F). Total 6.
    2 (2), 3 (3), 4 (4). Total 0.
    15 (F), 16 (10). Total 1.

    The rule is: Count numbers x in range [start, end] such that 
    hex(x) contains only characters A-F (no digits 0-9).
    """
    count = 0
    for i in range(start, end + 1):
        hex_val = hex(i)[2:] # Remove '0x'
        # Check if all characters are letters A-F
        if all('A' <= c <= 'F' or 'a' <= c <= 'f' for c in hex_val):
            count += 1
    return count