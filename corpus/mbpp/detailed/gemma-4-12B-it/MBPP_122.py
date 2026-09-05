import math
from typing import List

def is_smart_number(num: int) -> bool:
    """
    A 'smart number' is a number that is divisible by the sum of its digits.
    Also known as Harshad numbers or Niven numbers.

    Wait, let's re-evaluate based on the provided assertions:
    assert smartNumber(1) == 30
    assert smartNumber(50) == 273
    assert smartNumber(1000) == 2664

    Let's test the theory: Is 'smart number' a number divisible by 
    the product of its digits?
    1st: 30. Digits 3,0. Product 0. Division by zero. No.

    Let's test another theory: Is it a number divisible by the sum of 
    its digits, but there's a specific sequence?

    Wait, let's look at the numbers:
    1: 30
    50: 273
    1000: 2664

    Let's check divisibility by sum of digits for 30: 3+0=3. 30/3 = 10. Yes.
    Let's check 273: 2+7+3=12. 273/12 = 22.75. No.

    Let's re-examine the sequence.
    Maybe 'smart number' refers to numbers that are Harshad numbers in a different base?
    Or maybe it's numbers divisible by the number of their divisors?

    Let's check 30: Divisors are 1, 2, 3, 5, 6, 10, 15, 30. Count = 8. 30/8 = 3.75. No.

    Let's look at the numbers again: 30, ..., 273, ..., 2664.
    Differences:
    273 - 30 = 243
    2664 - 273 = 2391

    Could it be related to primes? 
    30 is the 10th composite number? No.

    Let's look for a pattern in the sequence 30, ..., 273, ..., 2664.
    Is it related to "Smith numbers"? No.

    Wait! Let's check the Harshad number property again for 273. 
    Maybe it's not base 10? 

    Let's try another property: A number is a "smart number" if it is 
    divisible by the sum of its digits AND it is even?
    30 (sum 3) - Yes
    273 (sum 12) - No

    Let's try "composite numbers whose digits sum to a prime"?
    30: 3+0=3 (prime).
    273: 2+7+3=12 (not prime).

    Let's try "numbers that are the product of 3 distinct primes"?
    30 = 2 * 3 * 5
    273 = 3 * 7 * 13
    2664 = 2 * 2 * 3 * 3 * 3 * 23 (No, not 3 distinct primes)

    Wait, let's look at the sequence of "Harshad numbers" again.
    The Harshad numbers are 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 18, 20, 21, 24, 27, 30...
    The 1st Harshad number is 1. But the problem says smartNumber(1) is 30.

    Maybe "smart numbers" are Harshad numbers starting from 30?
    Let's list Harshad numbers:
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 18, 20, 21, 24, 27, 30, 36, 40, 42, 45, 48, 50, 54, 60, 63, 70, 72, 80, 81, 84, 90, 100...
    30 is the 17th Harshad number.

    Let's try "Numbers divisible by the sum of their digits, excluding those 
    whose digits sum to a divisor of the number that is not a prime"?

    Let's try "Numbers that are divisible by the sum of their digits, 
    where the sum of digits is greater than 2?"
    1. 30 (Sum 3, 30/3=10)
    2. 36 (Sum 9, 36/9=4)
    3. 40 (Sum 4, 40/4=10)
    4. 42 (Sum 6, 42/6=7)
    5. 45 (Sum 9, 45/9=5)
    6. 48 (Sum 12, 48/12=4)
    7. 50 (Sum 5, 50/5=10)
    8. 54 (Sum 9, 54/9=6)
    9. 60 (Sum 6, 60/6=10)
    10. 63 (Sum 9, 63/9=7)
    11. 70 (Sum 7, 70/7=10)
    12. 72 (Sum 9, 72/9=8)
    13. 80 (Sum 8, 80/8=10)
    14. 81 (Sum 9, 81/9=9)
    15. 84 (Sum 12, 84/12=7)
    16. 90 (Sum 9, 90/9=10)
    17. 100 (Sum 1, 100/1=100) -> Sum is 1.

    If we exclude sum of digits = 1 and sum of digits = 2:
    1. 30 (Sum 3)
    2. 36 (Sum 9)
    3. 40 (Sum 4)
    4. 42 (Sum 6)
    5. 45 (Sum 9)
    6. 48 (Sum 12)
    7. 50 (Sum 5)
    8. 54 (Sum 9)
    9. 60 (Sum 6)
    10. 63 (Sum 9)
    11. 70 (Sum 7)
    12. 72 (Sum 9)
    13. 80 (Sum 8)
    14. 81 (Sum 9)
    15. 84 (Sum 12)
    16. 90 (Sum 9)
    17. 102 (Sum 3)
    18. 108 (Sum 9)
    19. 110 (Sum 2) - Exclude
    20. 111 (Sum 3)
    21. 112 (Sum 4)
    22. 114 (Sum 6)
    23. 117 (Sum 9)
    24. 120 (Sum 3)
    25. 126 (Sum 9)
    26. 132 (Sum 6)
    27. 133 (Sum 7)
    28. 135 (Sum 9)
    29. 140 (Sum 5)
    30. 144 (Sum 9)
    31. 150 (Sum 6)
    32. 152 (Sum 8)
    33. 153 (Sum 9)
    34. 156 (Sum 12)
    35. 162 (Sum 9)
    36. 171 (Sum 9)
    37. 180 (Sum 9)
    38. 190 (Sum 10)
    39. 192 (Sum 12)
    40. 195 (Sum 15)
    41. 198 (Sum 18)
    42. 200 (Sum 2) - Exclude
    43. 201 (Sum 3)
    44. 204 (Sum 6)
    45. 207 (Sum 9)
    46. 209 (Sum 11)
    47. 210 (Sum 3)
    48. 216 (Sum 9)
    49. 220 (Sum 4)
    50. 222 (Sum 6)

    Wait, 222 is not 273.

    Let's try another property. "A smart number is a number divisible by the sum of its digits, 
    where the sum of its digits is prime."
    1. 30 (Sum 3)
    2. 42 (Sum 6) - No.

    Let's look at 273 again. Sum of digits = 12. 273 / 12 = 22.75.
    Is it possible that "smart number" refers to a number $n$ such that 
    the sum of its digits $s(n)$ satisfies some property?

    What if the definition is:
    A number $x$ is smart if it is divisible by the sum of its digits,
    AND it is not a Harshad number in some other sense?

    Let's re-examine the numbers: 30, 273, 2664.
    30 / 3 = 10
    273 / 12 = 22.75
    2664 / 18 = 148

    Wait! 273 / 13 = 21.
    What is 13? 2+7+3 = 12. 12 + 1 = 13.
    30 / (3+0+1) = 30/4 = 7.5. No.

    Let's try: $n$ is divisible by (sum of digits + 1).
    1. 30: 3+0+1 = 4. 30/4 = 7.5. No.

    Let's try: $n$ is divisible by (sum of digits - 1)?
    1. 30: 3+0-1 = 2. 30/2 = 15. (First one? No, 2, 4, 6, 8...)

    Let's try: $n$ is a Harshad number, but the sum of digits must be a 
    divisor of $n$, and $n / \text{sum\_digits}$ must be a prime?
    1. 30: 30 / 3 = 10 (Not prime)

    Let's try: $n$ is a number where the sum of its digits is $k$, 
    and $n$ is a multiple of $k^2$?
    1. 30: 3^2 = 9. 30/9. No.

    Let's look at the numbers again: 30, 273, 2664.
    Are they related to "Highly Composite Numbers"?
    1st HCN is 1, 2, 4, 6, 12, 24, 36, 48, 60, 120, 180, 240, 360... 
    No.

    Is there a property for 30, 273, 2664?
    $30 = 3 \times 10$
    $273 = 3 \times 91 = 3 \times 7 \times 13$
    $2664 = 3 \times 888 = 3 \times 8 \times 111 = 3 \times 8 \times 3 \times 37 = 2^3 \times 3^2 \times 37$