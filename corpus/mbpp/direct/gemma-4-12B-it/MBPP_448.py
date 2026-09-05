def cal_sum(n):
    """
    Calculates the sum of the first n Perrin numbers.
    The Perrin sequence is defined by:
    P(0) = 3
    P(1) = 0
    P(2) = 2
    P(n) = P(n-2) + P(n-3) for n > 2

    The problem's assertions:
    cal_sum(9) == 49
    cal_sum(10) == 66
    cal_sum(11) == 88
    implies the sum is of terms P(0) to P(n-1).
    Wait, let's check the sequence:
    P(0)=3, P(1)=0, P(2)=2, P(3)=3, P(4)=2, P(5)=5, P(6)=5, P(7)=7, P(8)=10, P(9)=12, P(10)=17...
    Sum(9 terms): 3+0+2+3+2+5+5+7+10 = 37 (Not 49)
    Let's re-evaluate the sequence or the index.
    Maybe it's P(1) to P(n)?
    Sum(P(1) to P(9)): 0+2+3+2+5+5+7+10+12 = 46 (Not 49)
    Maybe it's P(0) to P(n)?
    Sum(P(0) to P(9)): 3+0+2+3+2+5+5+7+10+12 = 49. 
    Check n=10: 49 + P(10) = 49 + 17 = 66.
    Check n=11: 66 + P(11). P(11) = P(9) + P(8) = 12 + 10 = 22. 66 + 22 = 88.
    So the function calculates the sum of P(0) through P(n).
    """
    if n < 0:
        return 0

    perrin = [0] * (n + 1)
    if n >= 0:
        perrin[0] = 3
    if n >= 1:
        perrin[1] = 0
    if n >= 2:
        perrin[2] = 2

    for i in range(3, n + 1):
        perrin[i] = perrin[i-2] + perrin[i-3]

    return sum(perrin)