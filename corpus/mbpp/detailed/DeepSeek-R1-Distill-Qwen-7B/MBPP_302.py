Okay, I need to solve this problem: find the most significant bit number which is also a set bit in a given number. The function should return the value of that bit as a power of two. 

Let me break down the problem step by step.

First, I need to understand what a "set bit" is. A set bit means a bit that is 1 in its binary representation. So, for example, the number 6 in binary is 110, which has two set bits.

Now, the goal is to find the most significant bit that is set. The most significant bit is the leftmost bit that is 1 in the binary representation. For 6 (110), the most significant bit is at position 3 (if we count from 1). But in terms of power of two, 2^3 is 8, which is the value we need to return.

Wait, the examples provided in the problem are:
- set_Bit_Number(6) should return 4. Hmm, 6 in binary is 110, the most significant bit is at position 2 (counting from 0), which is 2^2 = 4. Oh right, so the position is 0-indexed.
- set_Bit_Number(10) returns 8. 10 in binary is 1010, the most significant bit is at position 3 (2^3 = 8).
- set_Bit_Number(18) returns 16. 18 in binary is 10010, the most significant bit is at position 4 (2^4 = 16).

So, the function needs to find the position of the most significant bit that is set to 1, and return 2 raised to that position.

Now, how to find the most significant set bit?

One approach is to iterate through each bit of the number, starting from the highest possible bit, and check if that bit is set. Once we find the highest set bit, we return 2^position.

But to make this efficient, we can use bit manipulation techniques. For example, we can use the bit_length() method of integers in Python, which returns the number of bits required to represent the integer in binary. For a non-zero integer, the bit_length() is one more than the highest set bit's position.

For example:
- 6 in binary is 110, bit_length() is 3. Highest set bit position is 3 - 1 = 2. 2^2 = 4.
- 10 in binary is 1010, bit_length() is 4. Highest set bit position is 4 - 1 = 3. 2^3 = 8.
- 18 in binary is 10010, bit_length() is 5. Highest set bit position is 5 - 1 = 4. 2^4 = 16.

This seems to work for these examples.

So, the steps for the function are:
1. Check if the input number is zero. If it is, return 0 because there are no set bits.
2. Calculate the bit length of the number.
3. Subtract 1 from the bit length to get the position of the most significant bit.
4. Return 2 raised to this position.

But wait, what about the case when the number is zero? According to the problem statement, we should handle edge cases. If the input is zero, there are no set bits, so the function should return 0.

Now, let me implement this in Python.

I can use the following code:

def set_Bit_Number(n):
    if n <= 0:
        return 0
    bit_length = n.bit_length()
    msb_position = bit_length - 1
    return 1 << msb_position

But I need to verify this with the given examples:

Testing set_Bit_Number(6):
- 6.bit_length() = 3
- msb_position = 2
- 1 << 2 = 4 → Correct.

Testing set_Bit_Number(10):
- 10.bit_length() = 4
- msb_position = 3
- 1 << 3 = 8 → Correct.

Testing set_Bit_Number(18):
- 18.bit_length() = 5
- msb_position = 4
- 1 << 4 = 16 → Correct.

What about edge cases?

Test case: n = 0 → return 0 → Correct.
Test case: n = 1 → bit_length() = 1 → 1 << 0 = 1 → Correct.
Test case: n = 2 → bit_length() = 2 → 1 << 1 = 2 → Correct.
Test case: n = 7 (111) → bit_length() = 3 → 1 << 2 = 4 → Correct.
Test case: n = 8 (1000) → bit_length() = 4 → 1 << 3 = 8 → Correct.
Test case: n = -6 → function returns 0 because n <=0 → Correct.

This code handles all these cases correctly.

So, the final function is:

def set_Bit_Number(n):
    if n <= 0:
        return 0
    bit_length = n.bit_length()
    msb_position = bit_length - 1
    return 1 << msb_position

This is a concise and efficient solution that handles all edge cases as specified.