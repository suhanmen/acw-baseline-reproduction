from typing import List


def get_perrin_number_at_index(n: int) -> int:
    """
    Calculates the n-th Perrin number.
    The Perrin sequence is defined by:
    P(0) = 3
    P(1) = 0
    P(2) = 2
    P(n) = P(n-2) + P(n-3) for n > 2
    """
    if not isinstance(n, int):
        raise TypeError("Index must be an integer.")
    if n < 0:
        raise ValueError("Index must be a non-negative integer.")

    # Base cases
    if n == 0:
        return 3
    if n == 1:
        return 0
    if n == 2:
        return 2

    # Iterative calculation to avoid recursion depth issues
    # p_prev3 is P(i-3), p_prev2 is P(i-2), p_prev1 is P(i-1)
    p_prev3 = 3  # P(0)
    p_prev2 = 0  # P(1)
    p_prev1 = 2  # P(2)

    current_p = 0

    # We start calculating from n = 3 up to the desired index
    for i in range(3, n + 1):
        # Formula: P(n) = P(n-2) + P(n-3)
        # Note: In our variables, P(n-2) is p_prev2 and P(n-3) is p_prev3
        current_p = p_prev2 + p_prev3

        # Update variables for the next iteration
        p_prev3 = p_prev2
        p_prev2 = p_prev1
        p_prev1 = current_p

    return p_prev1


def cal_sum(n: int) -> int:
    """
    Calculates the sum of the first n Perrin numbers (from index 0 to n-1).

    Based on the provided assertions:
    cal_sum(9) == 49
    cal_sum(10) == 66
    cal_sum(11) == 88

    By analyzing these values:
    The Perrin sequence is: 3, 0, 2, 3, 2, 5, 5, 7, 10, 12, 17, 22...
    Indices: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11

    Let's check the sums:
    Sum up to index 8 (9 elements): 3+0+2+3+2+5+5+7+10 = 37
    Wait, the assertions say:
    cal_sum(9) = 49
    cal_sum(10) = 66
    cal_sum(11) = 88

    Let's re-verify the sequence.
    P(0)=3, P(1)=0, P(2)=2
    P(3) = P(1)+P(0) = 0+3 = 3
    P(4) = P(2)+P(1) = 2+0 = 2
    P(5) = P(3)+P(2) = 3+2 = 5
    P(6) = P(4)+P(3) = 2+3 = 5
    P(7) = P(5)+P(4) = 5+2 = 7
    P(8) = P(6)+P(5) = 5+5 = 10
    P(9) = P(7)+P(6) = 7+5 = 12
    P(10) = P(8)+P(7) = 10+7 = 17
    P(11) = P(9)+P(8) = 12+10 = 22

    Cumulative sums:
    S(1) = 3
    S(2) = 3+0 = 3
    S(3) = 3+0+2 = 5
    S(4) = 5+3 = 8
    S(5) = 8+2 = 10
    S(6) = 10+5 = 15
    S(7) = 15+5 = 20
    S(8) = 20+7 = 27
    S(9) = 27+10 = 37
    S(10) = 37+12 = 49  <-- matches cal_sum(9)? No, cal_sum(9) is 49.

    Wait, if cal_sum(9) = 49, and S(10) = 49, it means the function calculates
    the sum of the first 10 numbers (indices 0 to 9).
    Let's check cal_sum(10) = 66.
    S(11) = S(10) + P(10) = 49 + 17 = 66.
    Let's check cal_sum(11) = 88.
    S(12) = S(11) + P(11) = 66 + 22 = 88.

    Conclusion: cal_sum(n) calculates the sum of the first n+1 Perrin numbers
    (i.e., indices 0 through n).
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    if n < 0:
        # Depending on interpretation, sum of 0 elements is 0
        # But based on patterns, n should be non-negative.
        return 0

    total_sum = 0

    # The problem implies the sum of numbers up to index n
    # We iterate from 0 to n inclusive.
    for i in range(n + 1):
        current_perrin = get_perrin_number_at_index(i)
        total_sum += current_perrin

    return total_sum