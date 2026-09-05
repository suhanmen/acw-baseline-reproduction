Okay, I need to solve this problem where I have to write a Python function called `closest_integer` that takes a string representing a number and returns the closest integer. If the number is equidistant between two integers, I should round it away from zero. Hmm, how do I approach this?

First, I need to parse the input string to get the numerical value. Oh right, I should probably convert the string to a float or a double. But wait, what if the string is something invalid? Like an empty string or not a number at all? I should handle those cases by raising an error. Oh right, the note says to validate inputs and deal with invalid ones explicitly, so I shouldn't let invalid inputs pass through silently.

So, step one: validate the input. I'll check if the string is empty or contains non-numeric characters. If it does, I'll raise a ValueError. Otherwise, I'll convert it to a float.

Once I have the numerical value, I need to determine the closest integer. How do I do that? Well, I can use the `round` function. Wait, but the problem says that when the number is exactly halfway between two integers, I should round away from zero. Let me test the `round` function with some examples.

For instance, round(14.5) gives 14, which is rounding towards zero, but according to the problem, I should round it to 15. So the standard `round` function doesn't work here. I'll have to implement a custom rounding method.

So, here's what I'll do: split the number into its integer and fractional parts. If the fractional part is exactly 0.5, I need to round away from zero. Otherwise, just round to the nearest integer.

Wait, how do I get the integer and fractional parts? Let me think. I can take the absolute value of the number, find the integer part, and then subtract it from the absolute value to get the fractional part. Then, if the fractional part is exactly 0.5, I'll round the integer part away from zero based on its sign. Otherwise, I'll just round the original number.

Hmm, another way: after converting to a float, I'll calculate the halfway point. If the number is halfway between two integers, I'll round away from zero. Otherwise, I'll round normally.

Alternatively, I can use the following approach: calculate the two nearest integers (floor and ceiling), then determine which one is closer. If they're equidistant, choose the one further from zero.

Let me think about an example. Take 14.5. The floor is 14, the ceiling is 15. The difference between 14.5 and 14 is 0.5, and the difference between 15 and 14.5 is also 0.5. Since they're equidistant, I should return 15. Similarly, for -14.5, the floor is -15, the ceiling is -14. The difference between -14.5 and -15 is 0.5, and the difference between -14.5 and -14 is 0.5. So, I should return -15.

Another example: 15.3. The floor is 15, the ceiling is 16. The difference between 15.3 and 15 is 0.3, and between 15.3 and 16 is 0.7. So closer to 15, return 15.

So the algorithm could be:
1. Convert the string to a float.
2. Check if the value is halfway between two integers. If so, round away from zero.
3. Otherwise, round to the nearest integer.

Wait, how to implement step 2? Let's see:

The fractional part is `value % 1`. So if it is exactly 0.5, then it's halfway.

So, code steps:
- Parse the string to a float, let's call it `n`.
- Check if the fractional part (n % 1) is exactly 0.5 or -0.5.
- If yes:
   - If n is positive, return the next integer (n // 1) + 1.
   - If n is negative, return the next integer towards negative infinity (n // 1) + 1 (since n // 1 for negative numbers in Python is towards negative infinity).
   - Wait, let me test: for -14.5, n // 1 is -15, so adding 1 gives -14, but that's wrong. Wait, no. Wait, for n = -14.5, n // 1 is -15. Adding 1 gives -14. But according to the note, we should return -15.

Wait, maybe a different approach. When the fractional part is exactly 0.5 in absolute terms:

If n is positive, and fractional part is 0.5, round to the next higher integer.

If n is negative, and fractional part is -0.5 (like -14.5), round to the next lower integer (more negative).

So, perhaps:

if fractional_part == 0.5 or fractional_part == -0.5:
   if n >= 0:
      return floor(n) + 1
   else:
      return math.floor(n) - 1
Wait, no. Let me think again.

Wait, floor(n) for 14.5 is 14, adding 1 gives 15, which is correct.

For -14.5, floor(n) is -15, subtracting 1 would give -16, which is wrong. Wait, no. Wait, fractional part of -14.5 is -0.5. So, when the fractional part is -0.5, which would be equidistant to -14 and -15. But the note says to round away from zero, so -14.5 should round to -15.

So in code:

if fractional_part == 0.5 or fractional_part == -0.5:
   if fractional_part == 0.5:
      return n // 1 + 1
   else:
      return (n // 1) - 1

Wait, let's test this.

n = 14.5: fractional_part = 0.5 → return 14 + 1 =15 → correct.
n = -14.5: fractional_part = -0.5 → return -15 -1 = -16 → wrong. Hmm, that's not right.

Wait, no. Because for -14.5, the two nearest integers are -15 and -14. The halfway is equidistant, but according to the note, we should return the one further from zero, which is -15.

So, in the case where the number is negative and fractional_part is -0.5, I need to round to the next lower integer (which is more negative).

Wait, n = -14.5, so floor(n) is -15, which is correct.

So in code:

if (n == math.floor(n) + 0.5) or (n == math.floor(n) - 0.5):
   if n > 0:
      return math.floor(n) + 1
   else:
      return math.floor(n) - 1

Wait, perhaps a better way is:

if (n - math.floor(n)) == 0.5:
   return math.floor(n) + 1
elif (n - math.ceil(n)) == -0.5:
   return math.ceil(n)
else:
   # handle regular rounding

Wait, maybe that's complicating. Alternatively, let me think about when the fractional part is exactly 0.5 or -0.5.

For n positive: 14.5 → 15.
For n negative: -14.5 → -15.

So perhaps, I can use the following logic:

if abs(n - math.floor(n)) == 0.5:
   return math.floor(n) if n > 0 else math.ceil(n)
else:
   return round(n)

Wait, let's see:

n = 14.5 → math.floor(n) is 14 → return 14 (but we need 15). Hmm, no.

Wait, no. Because in that case, for n =14.5, math.floor(n) is 14, but we need to round to 15. So perhaps when the fractional part is 0.5, the number is halfway between math.floor(n) and math.ceil(n). So, when n is positive, return math.ceil(n), which is math.floor(n) +1.

Similarly, when n is negative, like -14.5, math.ceil(n) is -14, and math.floor(n) is -15. Since we need to round away from zero, for n negative, we should return math.floor(n) (which is -15).

So in code:

if fractional_part == 0.5 or fractional_part == -0.5:
   if n >= 0:
      return math.ceil(n)
   else:
      return math.floor(n)
else:
   return round(n)

Wait, but let me test this.

n = 14.5 → fractional_part is 0.5 → return math.ceil(n) =15 → correct.
n = -14.5 → fractional_part is -0.5 → return math.floor(n) = -15 → correct.
n = 15.3 → fractional_part is 0.3 → not 0.5 → return round(15.3) =15 → correct.
n = 14.5000000001 → fractional_part ~0.5 → but not exactly 0.5 → returns round(n), which would be 15.
n = -14.499999999 → fractional_part ~-0.5 → return math.floor(n) →-15?
Wait, wait. For n =-14.5, fractional_part is -0.5 → return math.floor(n) which is -15 → correct.

n = 14.499999 → fractional_part ~0.5 → but not 0.5 → round(n) →14 → correct.
n=14.500001 → fractional_part is 0.500001 → not 0.5 → round(n) →15 → correct.

Wait, but for n=14.5, the code returns 15 which is correct.

Another test case: n= -14.5 → returns -15 → correct.

Another case: n= 0 → returns 0.
n= 2.5 → returns 3.
n= -2.5 → returns -3.

Yes, this logic seems to cover the cases correctly.

So, the steps in code:

1. Validate the input string.
   - Check if the string is empty → raise ValueError.
   - Try to parse the string as a float. If it fails → raise ValueError.
2. If the string represents a number with a fractional part equal to 0.5 or -0.5, round away from zero.
3. Else, round to the nearest integer.

So, now, let's write the code.

First, the function:

def closest_integer(value):
    pass

We need to validate the input. So, first, check if value is an empty string. If it is, raise ValueError.

Then, try to convert it to a float. If it's a valid float, proceed. If not, raise ValueError.

How to handle invalid inputs? For example, "abc" would cause a ValueError when trying to convert to float.

So:

try:
    n = float(value)
except ValueError:
    raise ValueError("Invalid input: not a valid number.")

But wait, what about leading/trailing spaces? Like " 123 " or "123.45.67". The above code would fail for the latter because it has two dots.

Hmm, but the problem statement doesn't specify whether to trim whitespace or handle such cases. Since the examples don't include these, perhaps the function should treat any non-empty string that can be converted to a float as valid. But to handle cases like "15.3", which is valid, but "15.3.45" is invalid.

So, the try-except approach should catch those cases.

So, code so far:

def closest_integer(value):
    try:
        n = float(value)
    except ValueError:
        raise ValueError("Invalid input: not a valid number.")

But wait, for example, what about something like "123a"? It raises ValueError, which is correct.

Next, determine if the fractional part is exactly 0.5 or -0.5.

Wait, the fractional part is n - floor(n). So, in code:

import math

fractional_part = n - math.floor(n)

if fractional_part == 0.5 or fractional_part == -0.5:
    if n >= 0:
        return math.ceil(n)
    else:
        return math.floor(n)
else:
    return round(n)

Wait, but let me test:

n=14.5 → math.floor(n)=14 → fractional_part=0.5 → return 15 → correct.

n=-14.5 → math.floor(n)=-15 → fractional_part=0.5 (because -14.5 - (-15) =0.5). Wait wait, wait:

Wait, for n=-14.5:

math.floor(n) is -15.

fractional_part = n - math.floor(n) → -14.5 - (-15) = 0.5.

So, the condition fractional_part == 0.5 is true.

But since n is negative (n=-14.5 >= 0 is false), we return math.floor(n) which is -15 → correct.

Yes, that's correct.

Another test case: n=-14.4 → fractional_part is -14.4 - (-15) = 0.6 → not 0.5 → return round(n) → -14 → correct.

n=14.4 → fractional_part is