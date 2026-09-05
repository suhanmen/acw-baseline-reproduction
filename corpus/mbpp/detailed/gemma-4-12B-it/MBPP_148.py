from typing import List

def sum_digits_twoparts(number: int) -> int:
    """
    Divides a non-negative integer into two parts such that the sum of 
    the digits of the two resulting parts is maximized.

    The 'parts' are formed by splitting the string representation of 
    the number at some index. For a number with N digits, there are 
    N possible split points (including the case where one part is empty).

    Example: 100
    Splits:
    - "" and "100" -> 0 + (1+0+0) = 1
    - "1" and "00" -> (1) + (0+0) = 1
    - "10" and "0" -> (1+0) + (0) = 1
    - "100" and "" -> (1+0+0) + 0 = 1
    Wait, the problem logic for 100 == 19 implies a different partitioning.
    Let's re-evaluate the logic based on the assertions:

    Assertion 1: 35 -> 17. 
    Digits of 35 are 3 and 5. Sum is 8.
    If we "divide" it such that digits are added: 3+5 = 8? No, 17.
    Wait, 35 divided into two parts:
    Possible splits of "35":
    "3", "5" -> sum(3) + sum(5) = 8

    Assertion 3: 100 -> 19.
    If "100" is divided into parts such that the sum of digits is 19...
    This is only possible if we are looking for the sum of digits of 
    the parts *after* some mathematical operation or if the split logic
    allows for something else.

    Re-reading "divide a number into two parts such that the sum of digits is maximum":
    Usually, "parts" refers to splitting the string.
    But for 100 to result in 19:
    Sum of digits of 100 is 1.
    If we treat the parts as numbers and do something else?
    Let's look at the numbers:
    35 -> 17.  3*5 = 15. 3+5 = 8. 3^2 + 5^2 = 9 + 25 = 34. 
    Wait, 35: (3+5) = 8. How to get 17?
    What if the split is into 3 and 5, and we sum their squares? No.

    Let's re-examine 100 -> 19.
    100 split into 10 and 0? Sum of digits is 1+0+0 = 1.
    100 split into 1 and 00? Sum of digits is 1+0+0 = 1.
    What if the "division" is a mathematical division?
    35 / 2 = 17.5. Sum of digits of 17 and 5? 1+7+5 = 13.

    Let's look at the sum of digits of (number / something) and (number % something).
    If we divide 35 by 2: 35 // 2 = 17, 35 % 2 = 1. Sum of digits: (1+7) + 1 = 9.
    If we divide 35 by 3: 35 // 3 = 11, 35 % 3 = 2. Sum of digits: (1+1) + 2 = 4.

    Wait! Let's try all possible divisors 'i' from 1 to number.
    For 35:
    i=1: 35//1=35, 35%1=0. Digits: 3+5+0 = 8.
    i=2: 35//2=17, 35%2=1. Digits: 1+7+1 = 9.
    i=3: 35//3=11, 35%3=2. Digits: 1+1+2 = 4.
    ...
    i=10: 35//10=3, 35%10=5. Digits: 3+5 = 8.
    None of these give 17.

    Let's try splitting the number into two integers a, b such that a + b = number.
    35: a=17, b=18. Sum of digits: (1+7) + (1+8) = 8 + 9 = 17.
    YES! 17+18 = 35. Sum of digits = 17.
    Let's check 100:
    100: a=49, b=51. Sum of digits: (4+9) + (5+1) = 13 + 6 = 19.
    YES! 49+51 = 100. Sum of digits = 19.
    Let's check 7:
    7: a=3, b=4. Sum of digits: 3 + 4 = 7.
    YES! 3+4 = 7.

    So the problem is: Find two non-negative integers a and b such that a + b = number,
    and sum_digits(a) + sum_digits(b) is maximized.

    To maximize sum_digits(a) + sum_digits(b) where a + b = N:
    We want as many 9s as possible in the digits of a and b.
    Example 100: 49 + 51. Digits: 4, 9, 5, 1.
    Example 35: 17 + 18. Digits: 1, 7, 1, 8.

    Wait, 17+18 is a very specific split. 
    Let's try other splits for 100:
    90+10 -> 9+0+1+0 = 10
    91+9 -> 9+1+9 = 19
    99+1 -> 9+9+1 = 19

    So for N, we want to find a such that 0 <= a <= N and sum_digits(a) + sum_digits(N - a) is max.
    """

    if not isinstance(number, int):
        raise ValueError("Input must be an integer.")

    if number < 0:
        # The problem doesn't specify negative, but sum of digits 
        # usually implies absolute values.
        number = abs(number)

    def get_sum_of_digits(n: int) -> int:
        """Helper to calculate sum of digits of an integer."""
        s = 0
        temp_n = abs(n)
        while temp_n > 0:
            s += temp_n % 10
            temp_n //= 10
        return s

    max_digit_sum = -1
    best_split = (0, number)

    # Since we want to maximize the sum of digits, and the sum of digits
    # is generally higher for numbers ending in 9, we can optimize.
    # However, to be safe and handle all cases, we check all splits.
    # For production code, if number is very large, we'd need a more
    # efficient approach than O(N), but given the context of these 
    # types of problems, N is usually small enough or there's a pattern.

    # Optimization: The sum of digits of a + b = N is maximized 
    # when we minimize the 'carries' in the addition a + b.
    # Sum_digits(a) + Sum_digits(b) = Sum_digits(a+b) + 9 * (number of carries).
    # So we want to maximize the number of carries.
    # To maximize carries, we want a + b to result in as many carries 
    # as possible.

    # Let's re-evaluate: 100 -> 99 + 1. Carries: 100 is 1+0+0. 
    # 99+1: 9+9=18 (1 carry), 1+1=2 (1 carry). Total 2 carries.
    # Sum of digits = Sum_digits(100) + 9 * (carries) = 1 + 9 * 2 = 19.
    # 35 -> 17 + 18. 17+18=35. 7+8=15 (1 carry), 1+1=2 (1 carry). Total 2 carries.
    # Sum of digits = Sum_digits(35) + 9 * (carries) = (3+5) + 9 * 2 = 8 + 18 = 26? 
    # Wait, 17+18: 7+8=15 (carry 1), 1+1+1=3. Total 1 carry.
    # Sum of digits = (3+5) + 9 * 1 = 17. Correct.

    # To maximize carries:
    # For 35, we want 1 carry. 17+18 gives 1 carry.
    # For 100, we want 2 carries. 99+1 gives 2 carries.

    # Since we need to be "production-grade" and handle all edge cases,
    # and the constraints aren't provided, let's consider if O(N) is acceptable.
    # If N is 10^7, O(N) is okay. If N is 10^18, we need the carry logic.
    # Given the assertions (35, 7, 100), N is small.

    # Let's use a more efficient approach: 
    # The maximum sum of digits occurs when we maximize carries.
    # A carry happens at position i if (a_i + b_i + carry_{i-1}) >= 10.
    # This is maximized when we pick a such that it's "almost" all 9s.

    # Let's try a loop that checks numbers that are likely to produce many carries.
    # These are numbers like 9, 19, 29, ..., 99, 109...
    # Actually, the maximum sum of digits will always occur at a split 
    # where 'a' ends in a sequence of 9s, or 'a' is slightly less than 
    # some power of 10.

    # To be absolutely safe and satisfy the "expert programmer" requirement 
    # without knowing the bounds, let's implement the O(N) approach 
    # but write it very cleanly. If N is huge, we'd use a digit DP approach.

    # Actually, looking at the 100 -> 19 and 35 -> 17 again:
    # 100: 99 + 1 -> (9+9) + (1) = 19
    # 35: 17 + 18 -> (1+7) + (1+8) = 17
    # These are the maximums.

    # Let's use the O(N) loop for now as it is the most "defensive" 
    # against unexpected constraints unless N is extremely large.

    # Correction: If N is 10^9, O(N) fails. Let's use the "carry" logic.
    # Max sum = sum_digits(N) + 9 * (max possible carries).
    # Max carries can be found by trying to make as many digits as 
    # possible produce a carry.

    # However, the problem can be solved by simply checking a few 
    # candidates: numbers that end in 9, 99, 999, etc., and 
    # numbers that are N - (some sequence of 9s).

    # Let's stick to a slightly optimized check:
    # The best 'a' will likely be of the form:
    # (Some prefix) followed by (some digits) followed by (some 9s)
    # Or simply, we can iterate through all possible "carry" counts.

    # Given the requirement for "explicit control flow", let's use a 
    # loop that is reasonably efficient.

    current_max = 0

    # For small N, O(N) is fine. For large N, we only need to check 
    # values of 'a' that result in many carries.
    # Those values of 'a' are usually numbers like 9, 19, 29... 
    # or 99, 199, 299...