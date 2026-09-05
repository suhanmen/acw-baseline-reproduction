def sum_digits_twoparts(n: int) -> int:
    """
    Divides a number into two parts such that the sum of digits of both parts is maximized.
    The function returns the maximum possible sum of digits.

    For a number n, we split its decimal representation into two non-empty parts at some position,
    then compute the sum of digits of both parts and return the maximum such sum.
    However, the problem examples suggest a different interpretation:
    - 35 -> 17: 3+5 = 8, but 17 suggests splitting as 3 and 5? No, 3+5=8. 
      Actually, 17 = 3 + 5? No. Let's re-analyze:
      Perhaps it's splitting the digits into two numbers and summing all digits in both? 
      But that's always the same as sum_digits(n). 

    Re-check examples:
    - 35 -> 17: digits 3 and 5. 3+5=8. But expected 17. 
      Wait, maybe it's interpreting the two parts as numbers and then summing their digits? 
      If we split 35 into 3 and 5: digits of 3 is 3, digits of 5 is 5 -> 3+5=8. Not 17.

    Alternative idea: Maybe the problem means to split the number into two parts (by decimal point) 
    such that when you interpret those parts as numbers and then take the sum of digits of those two numbers,
    you get the maximum? But that still doesn't match 17 for 35.

    Let me think differently. 
    What if we split the string of digits into two non-empty strings, convert each to an integer, 
    and then compute the sum of the digits of those two integers? But that would be the same as original digit sum.

    Wait, perhaps the example 35 -> 17 is a typo? Or maybe it's not splitting digits but doing something else.
    Let's check the third example: 100 -> 19.
    Digits of 100: 1,0,0 -> sum=1. But expected 19.
    This suggests we are not just summing the original digits.

    Another possibility: We split the number into two parts (say left and right), and then for each part,
    we write it in base 10, but that doesn't change anything.

    What if "divide a number into two parts" means splitting the decimal representation, and then 
    we are allowed to insert digits? No, that doesn't make sense.

    Let me look for a pattern:
    35 -> 17: 3*5 = 15, plus 2? No.
    7 -> 7: obviously the whole number.
    100 -> 19: 1*00 = 0, not 19.

    Wait, what if we split the number into two parts and then for each part, we consider the product of its digits and then sum those products?
    35: split into 3 and 5 -> 3*1? No, single digit product is the digit itself. 3+5=8.

    Let me try splitting 100:
    If we split 100 into "1" and "00", then 1 -> digit sum 1, 00 -> 0. Total 1. Not 19.
    If we split into "10" and "0": 1+0=1, 0=0 -> total 1.

    This is confusing. Let me re-read the problem: "divide a number into two parts such that the sum of digits is maximum."
    Maybe it means: split the number's digit string into two non-empty parts, convert each part to an integer, 
    and then take the sum of the digits of those two integers. But that's always the same as the original digit sum.

    Unless... the two parts are not formed by splitting the digit string sequentially, but by choosing two non-empty 
    subsequences of the digits that together form the entire set of digits (each digit used exactly once), and then 
    forming two numbers from these subsequences, and then summing the digits of those two numbers? But again, 
    the total digit sum would be invariant.

    There must be a different interpretation. Let me look at the numbers again:
    35 -> 17
    7 -> 7
    100 -> 19

    What if we are to split the number into two parts (by place value) and then for each part, we are 
    to consider the number in a different base? Unlikely.

    Another idea: Perhaps "sum of digits" refers to the sum of the digits of the two parts when they are 
    interpreted as numbers, but we are allowed to pad with zeros or something? No.

    Let me try a different approach: maybe the problem is to split the number into two parts such that the 
    sum of the two parts (as numbers) has the maximum digit sum? 
    For 35: split into 3 and 5 -> 3+5=8, digit sum of 8 is 8. Not 17.
    Split into 35 and 0? Not allowed (two non-empty parts).

    Wait, what if we split the digits of the number into two groups, and then for each group we form the largest possible number 
    from those digits (by sorting in descending order), and then take the sum of digits of those two numbers? 
    But the sum of digits would still be the same as the original.

    I'm stuck. Let me try to see if there's a mathematical relation:
    35 -> 17: 17 = 3 + 5 + 9? Where does 9 come from?
    7 -> 7: 7 = 7.
    100 -> 19: 19 = 1 + 0 + 0 + 18? 

    Another thought: maybe the problem is to split the number into two parts (say A and B) such that A+B is maximized, 
    and then return the digit sum of (A+B)? But for 35, if we split as 3 and 5, A+B=8, digit sum=8. Not 17.

    What if we split the number into two parts and then multiply them? 
    35: 3*5=15, digit sum of 15 is 6. Not 17.

    Let me try: 35 -> split into 3 and 5, then 3! + 5! = 6 + 120 = 126, digit sum=9. Not 17.

    Wait, what if the problem is misstated and it's actually about splitting the number into two parts such that 
    the sum of the digits of the two parts (when concatenated in some way) is maximum? That doesn't make sense.

    Let me consider that the examples might be indicating a different problem:
    Perhaps for a number n, we can choose two non-empty strings s1 and s2 such that s1+s2 = str(n) (concatenation), 
    and then we compute some value. But what value gives 17 for "35" and 19 for "100"?

    For "35":
    Split at position 1: "3" and "5" -> ? 
    Split at position 2: "35" and "" -> not allowed.

    For "100":
    Split at position 1: "1" and "00" -> ?
    Split at position 2: "10" and "0" -> ?

    What if we are to compute the sum of the digits of the two parts after some transformation?
    Or maybe the problem is to find two numbers A and B such that A+B = n, and the digit sum of A plus the digit sum of B is maximized?
    That's a standard problem! Let's check:
    For n=35: 
        We want A+B=35, maximize digit_sum(A)+digit_sum(B).
        How? By making A and B as small as possible in each digit place? 
        Actually, the maximum is achieved when we split as A=3, B=32? 
        digit_sum(3)=3, digit_sum(32)=5 -> total 8.
        Or A=0, B=35? But A and B must be positive? The problem says "two parts", which might imply non-empty digit representations, so A and B >=0 and not both zero? But typically in such problems, we allow leading zeros in the split but the numbers themselves are non-negative.
        However, if we allow A=0, then digit_sum(0)=0, digit_sum(35)=8 -> total 8.
        But we need 17.

    This standard problem (max digit sum for A+B=n) has a known solution: split n into two parts such that one part is as small as possible. 
    The maximum digit sum is achieved by taking A = n % 10 and B = n // 10 * 10, but that gives A+B=n only if we don't carry. 
    Actually, the maximum digit sum for A+B=n is 9*k + sum_digits(n%10) where k is the number of digits in n//10? 
    No, the standard solution is: the maximum digit sum is 9 * (number of digits in n-1) + sum_digits(n%10) ??? 

    Let me compute for 35:
    We can write 35 = 27 + 8 -> digit_sum(27)=9, digit_sum(8)=8 -> total 17. Yes!
    How? 27+8=35, 9+8=17.
    Or 35 = 18 + 17 -> 9+8=17.
    Or 35 = 32 + 3 -> 5+3=8 (not maximum).

    For 7:
    7 = 0 + 7 -> 0+7=7. Or 7 = 3+4 -> 3+4=7. Maximum is 7.

    For 100:
    We need A+B=100, maximize digit_sum(A)+digit_sum(B).
    Let's try A=91, B=9 -> 10+9=19. Yes! 91+9=100, digit_sum(91)=10, digit_sum(9)=9 -> 19.
    Or A=82, B=18 -> 10+9=19.
    Or A=99, B=1 -> 18+1=19.
    So the maximum is 19.

    Therefore, the problem is: Given n, find two non-negative integers A and B such that A+B=n, and digit_sum(A)+digit_sum(B) is maximized. Return that maximum.

    How to solve this optimally?
    We can iterate over all possible values of A from 0 to n, compute B=n-A, and then digit_sum(A)+digit_sum(B). 
    But that's O(n * log(n)), which might be too slow for large n. However, the problem doesn't specify constraints, and for the given examples, it works.

    But note: we can do better. The maximum digit sum is achieved when we break n into two parts such that each part has as many 9s as possible in the lower digits.
    Actually, the optimal strategy is: 
        Let s = str(n)
        We can choose to split at the last but one position? 
        But the above examples show that for 35 (digits "35"), we can get 17 by having A=27, B=8 (which corresponds to splitting the number 35 into 3 parts of 9,9,2? Not exactly).

    Insight: The maximum digit sum for A+B=n is equal to the sum of digits of n if we can avoid carries, but if there are carries, we can increase the digit sum by breaking a carry into two numbers. 
    Specifically, every carry in the addition A+B=n reduces the total digit sum by 9 for each carry. So to maximize the digit sum, we want to minimize carries. 
    However, we can also introduce artificial carries by choosing A and B appropriately to increase the total digit sum beyond sum_digits(n).

    Actually, the maximum digit sum is achieved by:
        Take the number n, and represent it as a sum of two numbers A and B such that in the addition, there are no carries. Then the digit sum is sum_digits(n).
        But if there are carries, the digit sum decreases by 9 per carry. However, we can choose A and B to have a carry that increases the digit sum in higher places? 

    Let me think differently: 
        The maximum digit sum for A+B=n is: 
            Let n have d digits. Then the maximum digit sum is 9*(d-1) + sum_digits(n % 10^k) for some k? 

    From the examples:
        35: d=2, 9*(2-1) + 8 = 9+8=17. (Here n%10=5, but we got 8? Wait, 35%10=5, sum_digits(5)=5. 9+5=14, not 17.)

    Alternative approach from known problems: 
        The maximum digit sum for A+B=n is: 
            Take the last digit of n,