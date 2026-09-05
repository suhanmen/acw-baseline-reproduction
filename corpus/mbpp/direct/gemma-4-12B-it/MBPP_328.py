def rotate_left(lst, n, k):
    """
    Rotates a list to the left by 'n' positions, and then rotates 
    it to the left by another 'k' positions.

    Actually, looking at the provided assertions:
    rotate_left([1...10], 3, 4) -> [4...10, 1, 2, 3, 4]
    Original length is 10. 
    If we rotate left by 3, we get [4, 5, 6, 7, 8, 9, 10, 1, 2, 3]
    If we then rotate left by another 1? No.

    Let's re-examine:
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3, 4 -> [4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4]
    Wait, the result has 11 elements. 
    [4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4]
    The input has 10 elements. The output has 11.
    This suggests the operation is: 
    Rotate left by 'n', then append the first 'k' elements of the original list to the end? 
    No, let's look at the values:
    1. rotate_left([1..10], 3, 4) -> Result starts at index 3 (the 4th element), 
       and repeats the first 4 elements at the end?
       Original: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
       Left rotate by 3: [4, 5, 6, 7, 8, 9, 10, 1, 2, 3]
       Then add the first 4 elements of the ORIGINAL list? 
       [4, 5, 6, 7, 8, 9, 10, 1, 2, 3] + [1, 2, 3, 4] = [4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 1, 2, 3, 4] -> No.

    Let's look closer at the assertions again:
    1. [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3, 4 -> [4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4]
       Elements are: 4,5,6,7,8,9,10 (7 elements), 1,2,3 (3 elements), 4 (1 element).
       Total 11 elements.

    Actually, the pattern is:
    Rotate left by n: [4, 5, 6, 7, 8, 9, 10, 1, 2, 3]
    Then append the first k elements of the original list to the end of the rotated list?
    [4, 5, 6, 7, 8, 9, 10, 1, 2, 3] + [4] ... No.

    Let's try: take the list from index n to end, then add the first n elements, then add the first k elements?
    For (3, 4): [4,5,6,7,8,9,10] + [1,2,3] + [4] = [4,5,6,7,8,9,10,1,2,3,4]
    For (2, 2): [3,4,5,6,7,8,9,10] + [1,2] + [3] ... no, result is [3,4,5,6,7,8,9,10,1,2]

    Wait, let's re-read the assertions VERY carefully:
    assert rotate_left([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],3,4)==[4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4] 
    Wait, index 3 is the value 4.
    The result is: lst[3:] + lst[:3] + lst[3:4] 
    Let's check (2, 2): [3, 4, 5, 6, 7, 8, 9, 10, 1, 2]
    lst[2:] + lst[:2] = [3, 4, 5, 6, 7, 8, 9, 10, 1, 2]
    In this case, the 2nd parameter (k=2) didn't add anything?

    Wait, look at the lengths:
    (3, 4) -> Result length 11.
    (2, 2) -> Result length 10.
    (5, 2) -> Result length 7.

    Wait, the third assertion:
    rotate_left([1...10], 5, 2) == [6, 7, 8, 9, 10, 1, 2]
    Original list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    Result: [6, 7, 8, 9, 10, 1, 2]
    This is just lst[5:] + lst[:2].

    Let's re-verify:
    (3, 4): lst[3:] + lst[:3] + lst[3:4] ? No.
    Wait! [4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4]
    If we take lst[3:] (which is [4,5,6,7,8,9,10]) and then append lst[:3] (which is [1,2,3]) and then append lst[3:3+1]?

    Let's try a different logic:
    The result is lst[n:] + lst[:n] but the "length" of the slice lst[:n] is actually modified by k?
    No.

    Let's look at (3, 4) again:
    Input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    Result: [4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4]
    Result is: lst[3:] + lst[:3] + lst[3:4]

    Wait, (2, 2):
    Input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    Result: [3, 4, 5, 6, 7, 8, 9, 10, 1, 2]
    Result is: lst[2:] + lst[:2]

    Wait, (5, 2):
    Input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    Result: [6, 7, 8, 9, 10, 1, 2]
    Result is: lst[5:] + lst[:2]

    Pattern:
    Result = lst[n:] + lst[:k]
    Let's check:
    (3, 4): lst[3:] + lst[:4] = [4, 5, 6, 7, 8, 9, 10] + [1, 2, 3, 4] = [4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4] (Correct!)
    (2, 2): lst[2:] + lst[:2] = [3, 4, 5, 6, 7, 8, 9, 10] + [1, 2] = [3, 4, 5, 6, 7, 8, 9, 10, 1, 2] (Correct!)
    (5, 2): lst[5:] + lst[:2] = [6, 7, 8, 9, 10] + [1, 2] = [6, 7, 8, 9, 10, 1, 2] (Correct!)

    So the logic is: lst[n:] + lst[:k]
    """
    return lst[n:] + lst[:k]