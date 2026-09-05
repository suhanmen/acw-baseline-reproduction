# Standard library imports
from typing import Optional, Tuple, Union

def _compute_sum_of_digits(n: int) -> int:
    """
    Computes the sum of the decimal digits of a non-negative integer n.

    Args:
        n (int): A non-negative integer.

    Returns:
        int: The sum of the digits of n.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is negative.
    """
    # Validate type
    if not isinstance(n, int):
        raise TypeError(f"Input must be an integer, got {type(n).__name__}")

    # Validate value (non-negative)
    if n < 0:
        raise ValueError(f"Input must be non-negative, got {n}")

    # Convert to string to iterate over digits
    s_n = str(n)

    # Compute sum manually to avoid library dependencies if any
    total_sum = 0
    for char_digit in s_n:
        # Each char is guaranteed to be a digit 0-9 due to str() of non-negative int
        digit_value = int(char_digit)
        total_sum += digit_value

    return total_sum

def _split_number_into_parts_and_maximize_digit_sum(n: int) -> Tuple[Optional[int], Optional[int]]:
    """
    Attempts to split a non-negative integer n into two non-negative parts (a, b)
    such that a + b = n and the sum of digits of a plus the sum of digits of b
    is maximized.

    The problem implies we are looking for specific splits. 
    Based on the examples:
    - 35 -> 17 (likely 3 and 5 are the parts? 3+5=8. Wait, 17 is the answer for sum of digits).
      If parts are 3 and 5: sum_digits(3) + sum_digits(5) = 3 + 5 = 8. This does not match 17.
      Let's re-read the prompt logic carefully.

      Example 1: input 35, output 17.
      Possible splits of 35: (0,35), (1,34), ..., (35,0).
      (0,35): 0 + 3+5 = 8
      (1,34): 1 + 3+4 = 8
      ...
      (3,32): 3 + 3+2 = 8
      (5,30): 5 + 3+0 = 8

      Is it possible the problem implies splitting the *string* of digits?
      Split "35" into "3" and "5". Values 3 and 5. Sum of digits = 3+5=8. Still 8.

      Wait, let's look at example 3: 100 -> 19.
      Split "100"? "1", "00" -> 1 and 0 -> sum=1. "10", "0" -> 1+0=1.
      If we treat 100 as 1+0+0? No.

      Alternative interpretation: 
      Maybe the "parts" are not additive parts summing to N, but simply partitions of the digits?
      No, "divide a number into two parts" usually implies arithmetic partition.

      Let's reconsider the example 35 -> 17.
      How do we get 17 from 35?
      Digits of 35 are 3, 5.
      Maybe we split the number 35 into two numbers A and B such that A+B is NOT 35?
      "Divide a number into two parts" strongly suggests A + B = N.

      Is it possible the output 17 is wrong in my understanding?
      Let's try to reverse engineer 35 -> 17.
      Max sum of digits for a number N is usually achieved by carrying over to create more 9s?
      No, that increases the value.

      What if the "parts" are not A and B where A+B=N, but we are splitting the string representation?
      "35" -> "3" and "5"? Sum of digits = 3+5=8.
      "100" -> "1", "00" (0), sum=1. "10", "0" (0), sum=1. "1", "0", "0" (three parts? No, two parts).

      Let's look at the numbers again.
      35 -> 17.
      7 -> 7.
      100 -> 19.

      Hypothesis: The problem statement provided in the prompt might have a typo in the examples or my interpretation of "divide" is standard arithmetic division (quotient/remainder) which doesn't fit "two parts".

      Let's try a different interpretation found in similar algorithmic problems:
      "Split the number string into two substrings".
      For 35: split at index 1: "3", "5". Integers 3, 5. Sum of digits(3)+Sum of digits(5) = 8.
      This doesn't match 17.

      What if the function returns the sum of the digits of the *result* of some operation?

      Let's look at 100 -> 19.
      Digits: 1, 0, 0.
      If we split 100 into 1 and 00 (0)? Sum=1.
      If we split 100 into 10 and 0? Sum=1.
      How to get 19?
      19 = 1 + 9 + 9? No.
      19 = sum of digits of something?
      Maybe the parts are not additive?

      Wait, could the examples be:
      35 -> 3 * 5 + ...? No.

      Let's reconsider the standard "Maximize sum of digits by adding two numbers that sum to N" problem.
      Usually, the maximum sum of digits for a partition A+B=N is achieved by splitting into A=N/2, B=N/2 roughly?
      For N=19 (binary representation of 35 is 100011? No).

      Let's try to interpret "divide a number into two parts" as splitting the decimal string.
      If N=35. String "35". Split into "3" and "5".
      Maybe the operation is not sum of digits of parts, but something else?
      "sum of digits is maximum".

      Is it possible the examples are:
      35 -> 3 + 5 = 8? No, output is 17.
      7 -> 7. (Split "7" into "7" and ""? Or just keep 7? If we keep 7, sum is 7).
      100 -> 19.

      What if the inputs are not base 10? No, examples look decimal.

      Let's look at the numbers 35, 7, 100 and results 17, 7, 19.
      35 + something = 17? No.
      35 * 0.5 = 17.5?

      Wait, 35 in some base?
      What if the "parts" are the digits themselves, and we arrange them?

      Let's try a different angle. Is it possible the problem is asking to split the number into two parts A and B (concatenation) such that A+B = N? No, that's the reverse.

      Let's assume there is a specific trick.
      35 -> 17.
      17 is 35 - 18.
      100 -> 19.
      19 is 100 - 81.
      7 -> 7.
      7 is 7 - 0.

      18 is 2 * 9. 81 is 9 * 9.
      So for 35, we subtract 18 (2*9). For 100, we subtract 81 (9*9).
      Why?
      Because splitting a number to maximize digit sum often involves creating 9s.
      But here we are subtracting?

      Let's re-read the prompt examples extremely literally.
      `sum_digits_twoparts(35) == 17`
      `sum_digits_twoparts(7) == 7`
      `sum_digits_twoparts(100) == 19`

      Could "divide a number into two parts" mean splitting the string of digits into two non-empty substrings?
      For 35: "3", "5".
      Maybe the function calculates the sum of digits of the FIRST part and the SECOND part, but the example output 17 is actually `sum_digits(35 // 2) + sum_digits(35 - 35//2)`?
      35 // 2 = 17. 35 - 17 = 18.
      sum_digits(17) = 1+7=8. sum_digits(18) = 1+8=9. Total 17.
      YES!
      Let's test this hypothesis on 100.
      100 // 2 = 50. 100 - 50 = 50.
      sum_digits(50) = 5. sum_digits(50) = 5. Total 10.
      But expected is 19.
      Hypothesis failed for 100.

      Try splitting 100 not at the middle.
      We need sum_digits(A) + sum_digits(B) = 19 where A+B=100.
      Possible splits of 100:
      (1, 99): 1 + 18 = 19. MATCH!
      So for 100, the optimal split is 1 and 99.
      For 35:
      We need sum_digits(A) + sum_digits(B) = 17 where A+B=35.
      Try (3, 32): 3 + 5 = 8.
      Try (17, 18): 1+7 + 1+8 = 8 + 9 = 17. MATCH!
      For 7:
      Split 7 into (0, 7)? 0+7=7.
      Split 7 into (1, 6)? 1+6=7.
      Split 7 into (3, 4)? 3+4=7.
      Max is 7.

      So the logic is:
      Given N, find integers A, B such that A + B = N and sum_digits(A) + sum_digits(B) is maximized.
      Return that maximum sum.

      Let's verify 35 -> 17 again.
      A=17, B=18. Sum digits: (1+7) + (1+8) = 8 + 9 = 17. Correct.
      Let's verify 100 -> 19 again.
      A=1, B=99. Sum digits: (1) + (9+9) = 1 + 18 = 19. Correct.
      Let's verify 7 -> 7.
      Any split A+B=7.
      (0,7)->7. (1,6)->7. ... (3,4)->7.
      Max is 7. Correct.

      Algorithm to solve:
      Given N, we want to maximize f(A) = sum_digits(A) + sum_digits(N-A) for 0 <= A <= N.
      Since N can be large, iterating all A from 0 to N is O(N), which is too slow if N is large (e.g., N=10^9).
      However, the function is asked to write a function that satisfies these assertions.
      Usually, for "production grade" code, we should consider complexity.
      But finding the exact split that maximizes digit sum for arbitrary N is a known hard problem?
      Actually, the maximum digit sum for a sum S is often achieved by splitting into two numbers with many 9s.
      Specifically, to maximize digit sum of X+Y=S, we want to create as many 9s as possible in X and Y.
      The optimal strategy is often related to the base-10 representation.

      Is there a closed form or a greedy approach?
      Consider N=100.
      We want to make parts look like 99.
      100 - 1 = 99. 1 is small.
      Consider N=35.
      35 - 18 = 17. Both end in 7/8? No, 17 and 18.
      17 has 1, 7. 18 has 1, 8.

      There is a known property:
      To maximize sum of digits of A+B=N, we should try to make A and B end in 9s.
      If N has k digits, the max digit sum is roughly 9*k + something?
      Actually, there is a simpler observation:
      sum_digits(A) + sum_digits(B) >= sum_digits(A+B