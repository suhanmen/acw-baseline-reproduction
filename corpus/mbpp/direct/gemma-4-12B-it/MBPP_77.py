def is_Diff(n: int) -> bool:
    """
    Calculates the difference between the sum of even digits and odd digits.
    The function returns True if the absolute difference is equal to 0,
    otherwise returns False.

    Note: Based on the provided assertions:
    12345: Even (2,4) sum=6; Odd (1,3,5) sum=9. |6-9|=3 != 0 -> False
    1212112: Even (2,2,2,2) sum=8; Odd (1,1,1,1) sum=4. Wait, let's re-check.
    Actually, looking at the logic: 
    1212112: Even digits are 2, 2, 2. Sum = 6. Odd digits are 1, 1, 1, 1. Sum = 4.
    Wait, 1212112 has digits: 1, 2, 1, 2, 1, 1, 2.
    Evens: 2, 2, 2 -> Sum = 6.
    Odds: 1, 1, 1, 1 -> Sum = 4.
    6 - 4 = 2. 

    Let's re-evaluate the assertion is_Diff(1212112) == True.
    If the condition is (Sum Even == Sum Odd):
    12345: Even(2+4=6), Odd(1+3+5=9) -> 6 != 9 (False)
    1212112: Even(2+2+2=6), Odd(1+1+1+1=4) -> 6 != 4 (False)

    Let's look closer at 1212112 again. 
    Digits: 1, 2, 1, 2, 1, 1, 2
    Even: 2, 2, 2. Sum = 6.
    Odd: 1, 1, 1, 1. Sum = 4.

    Wait, maybe it's Sum of Even Indices vs Sum of Odd Indices?
    12345: Idx 0,2,4: 1,3,5 (Sum 9). Idx 1,3: 2,4 (Sum 6). 9 != 6.
    1212112: Idx 0,2,4,6: 1,1,1,2 (Sum 5). Idx 1,3,5: 2,2,1 (Sum 5). 5 == 5. (True!)
    1212: Idx 0,2: 1,1 (Sum 2). Idx 1,3: 2,2 (Sum 4). 2 != 4. (False)

    The logic is: Sum of digits at even indices == Sum of digits at odd indices.
    """
    s = str(n)
    even_idx_sum = 0
    odd_idx_sum = 0

    for i in range(len(s)):
        if i % 2 == 0:
            even_idx_sum += int(s[i])
        else:
            odd_idx_sum += int(s[i])

    return even_idx_sum == odd_idx_sum