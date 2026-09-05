Okay, let's tackle this problem step by step. The goal is to write a Python function called `count_Num` that counts how many numbers have both the 0th bit and the nth bit set. 

First, I need to understand what it means for a bit to be set. In binary representation, a bit is set if it's 1. So, for example, the number 3 in binary is `11`, which means both the 0th and 1st bits are set.

The problem requires us to count numbers where both the 0th bit and the nth bit are set. So, for a given number `n`, we need to check if both of these bits are 1 in its binary representation.

Let's break down the steps:

1. **Understand the Bits**: For a number `n`, the 0th bit is always 1 if the number is odd. So, any number that's even will automatically have the 0th bit unset.
2. **Check the nth Bit**: For the nth bit, we need to determine if it is set. This can be done using a bitwise AND operation. If `(n & (1 << n))` is non-zero, the nth bit is set.
3. **Count the Numbers**: We'll iterate through numbers from 0 to `n` and count how many numbers satisfy both conditions: the 0th bit is set and the nth bit is set.

Wait, but the problem statement mentions "oth and nth bits". That seems like a typo. Since the 0th bit is always the least significant bit, it's likely that they meant the 0th and nth bits.

Let's implement the function to count numbers up to `n` that have both the 0th and nth bits set.

Now, let's think about the test cases:
- For `n=2`, the valid numbers are 3 (binary 11).
- For `n=3`, the valid numbers are 3 (binary 11) and 7 (binary 111).
- For `n=1`, the valid number is 3 (binary 11), but since n is 1, it's a bit tricky because 3 in binary is '11' which has the 0th and 1st bits set.

Wait, let's see:
- For `n=2`: The 0th and 2nd bits must be set. So the number must be of the form 5 (101) or 7 (111), but for numbers up to 3, only 3 (11) satisfies both 0th and 1st bits set.
- For `n=3`: We need to count numbers up to 7 where both 0th and 3rd bits are set. These numbers are 9 (1001), 11 (1011), 13 (1101), and 15 (1111). But since the test case for `n=3` expects 2, it seems like maybe the function is intended to count numbers where both bits are set in their binary representation, regardless of their position.

Wait, perhaps I misunderstood the problem. Let me re-read it.

The problem says: "count numbers whose 0th and nth bits are set." So, for a given number `n`, the function should count how many numbers up to `n` have both the 0th and nth bits set.

Wait, but in the test cases, `n` is used as both the upper limit and the bit position. That seems inconsistent. For example, in `count_Num(2)`, the 0th and 2nd bits must be set.

Let's think again:

The function `count_Num` takes an integer `n` and returns the count of numbers from 0 to `n` (inclusive) where both the 0th bit and the nth bit are set.

Let's implement that logic.

Now, considering the test cases:
- For `n=2`: We count numbers from 0 to 2.
  - 0: 00 -> 0th bit not set
  - 1: 01 -> 0th bit set, 2nd bit not set
  - 2: 10 -> 0th bit not set
  So, no numbers satisfy both conditions, but the test case expects 1. Hmm, that's conflicting.

Wait, perhaps the function is intended to count numbers where their binary representation has both the 0th and nth bits set, regardless of their position relative to `n`.

Wait, looking back at the problem statement:

"Write a python function to count numbers whose oth and nth bits are set."

Ah, perhaps the function should count numbers where their binary representation has both the 0th and nth bits set. The upper limit for counting is not `n`, but rather, any number, and we count how many have both bits set.

Wait, but that doesn't align with the test cases either. Let me see:

Test case 1: `assert count_Num(2) == 1`

If we're counting numbers up to 2 where both 0th and 2nd bits are set:
- 3 (11) has 0th bit set but 2nd bit not set.
- 3 in binary is 11, but 2nd bit is the third position, which is 2^2 = 4. So, numbers up to 2 can't have the 2nd bit set.

This suggests that perhaps the function is intended to count numbers where both bits are set in any position, not necessarily up to `n`.

Wait, perhaps the function should count numbers where both the 0th and nth bits are set in their binary representation, regardless of the value of the number.

But in that case, for `n=2`, it would count numbers where both the 0th and 2nd bits are set, like 5 (101), 7 (111), etc. But the test case expects 1, which doesn't make sense.

Hmm, this is confusing. Let's re-examine the problem statement.

Problem statement:
- Write a python function to count numbers whose oth and nth bits are set.
- The function must satisfy these assertions:
  - assert count_Num(2) == 1
  - assert count_Num(3) == 2
  - assert count_Num(1) == 1

So, for `n=2`, the count is 1.
For `n=3`, the count is 2.
For `n=1`, the count is 1.

Let's think about these test cases:

For `n=2`:
We need to count numbers that have both the 0th and 2nd bits set.

Possible numbers:
- 3: binary 11 (0th bit set, but 2nd bit is 2^2=4, so 3 doesn't have 2nd bit set)
- 5: binary 101 (0th and 2nd bits set)
- 7: binary 111 (0th, 1st, and 2nd bits set)
But wait, for `n=2`, what's the maximum number we're considering? It's unclear.

Wait, perhaps the function is intended to count numbers where the nth bit is set, and the 0th bit is also set. But in the test case for `n=2`, the count is 1. Let's see which number that could be.

If we consider numbers up to 3 (since `n=2`), the numbers are 0, 1, 2, 3.

Which of these have both 0th and 2nd bits set?
- 0: 000 -> no
- 1: 001 -> 0th bit set, 2nd bit not set
- 2: 010 -> 0th bit not set
- 3: 011 -> 0th bit set, 2nd bit not set

So, none of them have both bits set. But the test case expects 1. This suggests that perhaps the upper limit is not `n`, but something else.

Wait, perhaps the function is supposed to count all numbers (not limited to `n`) where both the 0th and nth bits are set. But that doesn't align with the test cases.

Alternatively, perhaps the function is supposed to count numbers up to `n+1`. Let's check:

For `n=2`, numbers up to 3:
- 5: binary 101 has 0th and 2nd bits set. So 5 is greater than 3, which is the upper limit.

This doesn't align either.

Another approach: perhaps the function is supposed to count numbers where the 0th and nth bits are set, and `n` is the position of the bit, regardless of the value of the number.

So, for `n=2`, we're looking for numbers that have both the 0th and 2nd bits set. The smallest such number is 5 (101). But the test case expects 1, which suggests that perhaps the function counts numbers up to `2^n` or something.

Alternatively, perhaps the function is supposed to count numbers where the nth bit is set and the 0th bit is also set, but in the test case, it's considering the binary representation's positions.

Wait, perhaps the function is supposed to count numbers where both the 0th and nth bits are set in their binary representation, regardless of their value. So, for `n=2`, how many such numbers have both bits set.

But in that case, for any number, the 0th bit is set if the number is odd. The nth bit is set if the number is >= 2^n.

So, for `n=2`, 2^n is 4. So, numbers >=4 where the number is odd and has the 2nd bit set.

But the test case for `n=2` expects 1. Let's see:

Numbers >=4, odd, and have 2nd bit set.

The 2nd bit is 4. So numbers like 5 (101) have 4 + 1 = 5.

Is there only one such number in the test case?

Wait, perhaps the function is intended to count numbers from 0 to 2^n where both bits are set. Let's test:

For `n=2`, 2^n is 4.

Numbers from 0 to 4:

- 0: 00 -> no
- 1: 01 -> 0th bit set, 2nd bit not set
- 2: 10 -> 0th bit not set
- 3: 11 -> 0th bit set, 2nd bit not set
- 4: 100 -> 0th bit not set

So, no numbers satisfy both conditions. But the test case expects 1. This is conflicting.

Perhaps I'm misunderstanding the problem statement. Let's read it again:

"Write a python function to count numbers whose oth and nth bits are set."

So, for any number, count how many have both the 0th and nth bits set. The function takes `n` as input, and returns the count.

Wait, but then for `n=1`, 0th and 1st bits set. Let's see:

Numbers where both bits are set:

- 3 (11)
- 7 (111)
- 11 (1011)
- etc.

But the test case `assert count_Num(1) == 1` suggests that for `n=1`, the count is 1. Which suggests that the function is counting numbers up to `2^n` or something.

Wait, maybe the function is supposed to count numbers where the nth bit is set, but no, the test case for `n=3` expects 2.

This is getting confusing. Perhaps I should look for another approach.

Alternative approach: the test cases suggest that for `n=1`, count is 1; for `n=2`, count is 1; for `n=3`, count is 2.

Looking at these numbers:

- For `n=1`, the valid number is 3 (binary 11). Because 3 has both 0th and 1st bits set.

- For `n=2`, the valid number is 5 (binary 101). Because 5 has 0th and 2nd bits set.

- For `n=3`, the valid numbers are 11 (1011) and 7 (0111), which have 0th and 3rd bits set.

Wait, but the test case for `n=2` is 1. So perhaps the function counts numbers where the nth bit is set, and the 0th bit is also set.

Wait, for `n=2`, the numbers that have the 2nd bit set are numbers >=4.

Numbers >=4, where 0th bit is set: 5 (101), 9 (1001), 13 (1101), 15 (1111), etc.

So for any n, the count is infinite. But the test cases suggest finite counts.

This is conflicting.

Another thought: perhaps the function is supposed to count the number of set bits in the nth position and the 0th position. But the test cases don't align with that.

Alternatively, perhaps the function is supposed to count the number of times both the 0th and nth bits are set when counting from 0 to `n`.

Wait, let's test that.

For `n=2`:
Numbers from 0 to 2:
0: 00 -> 0th bit 0
1: 01 -> 0th bit 1, 2nd bit 0
2: 10 -> 0th bit 0, 2nd bit 0
So, no numbers have both bits set. But the test case expects 1. This doesn't make sense.

Alternatively, perhaps the function is counting the number of set bits in the nth position across all numbers from 0 to `n`. That also doesn't align with the test cases.

Wait, perhaps the function is counting the number of numbers up to `n` where the nth bit