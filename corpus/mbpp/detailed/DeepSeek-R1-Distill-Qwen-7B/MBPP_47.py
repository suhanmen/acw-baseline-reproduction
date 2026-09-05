Okay, I need to solve this problem where I have to find the last digit of the factorial of a divided by the factorial of b. Let me think about how to approach this step by step.

First, I need to understand what the problem is asking. The function compute_Last_Digit(a, b) should return the last digit of (a! / b!). For example, if a=2 and b=4, then 2! is 2 and 4! is 24, so 2 / 24 = 0.0833..., but the last digit would be 2 because we only consider the integer part.

Wait, no. Actually, 2! is 2 and 4! is 24. So a! is 2 and b! is 24. a! divided by b! is 2 / 24 = 0.0833..., which doesn't make sense because factorials are integers, but dividing them might not be an integer. Oh, I think I misunderstood the problem. Let me re-read it.

The problem says, "the last digit when factorial of a divides factorial of b." So, does that mean when b! divides a! or when a! divides b!? The first assertion compute_Last_Digit(2,4) returns 2, which suggests that a=2 and b=4. So 2! is 2 and 4! is 24. 24 divided by 2 is 12, which has a last digit of 2. That makes sense with the first assertion.

Wait, but 2! is 2, 4! is 24, and 24 divided by 2 is 12, which has a last digit of 2. That matches the first assertion.

Similarly, compute_Last_Digit(6,8) is 6. 8! is 40320, 6! is 720. 40320 / 720 is 56, which has a last digit of 6. That makes sense.

And compute_Last_Digit(1,2) is 2. 2! is 2, 1! is 1. 2 / 1 is 2, which has a last digit of 2. Okay, now I understand.

So the task is to compute (b! / a!) and return the last digit of that result. But wait, in the first example, a=2 and b=4, so b! is larger than a!, so the division is possible. But what if a is larger than b? For example, if a=4 and b=2, then a! is 24, b! is 2, and 24 / 2 = 12, which has a last digit of 2. So in that case, it's the same as the first case.

But what if a! is larger than b!? For example, a=3 and b=2, then a! is 6, b! is 2, 6 / 2 = 3, last digit 3. What if a=5, b=3? 120 / 6 = 20, last digit 0.

Wait, but how do we handle cases where a! is not divisible by b!? For example, a=3, b=4. Then a! is 6, b! is 24. 6 / 24 = 0.25. But the last digit is supposed to be an integer digit. Should we consider 0 in this case? Or is there a misunderstanding here.

Wait, the problem says "the last digit when factorial of a divides factorial of b." So does that mean we only consider cases where b! divides a!? If so, then a must be greater than or equal to b because factorials increase with n. Otherwise, b! doesn't divide a!.

For example, if a=2 and b=4, since 2 < 4, 4! doesn't divide 2! because 2! is smaller. So perhaps the function should return 0 in this case, as no integer division is possible.

But looking back at the first assertion, compute_Last_Digit(2,4) returns 2. Wait, this contradicts my previous reasoning. Let me recalculate.

Wait, maybe I got the problem wrong. Let me re-examine the assertion: compute_Last_Digit(2,4) returns 2. That would be the same as (2! / 4!) which is 2 / 24 = 0.0833..., but the last digit isn't an integer. So that's confusing.

Alternatively, maybe the function is supposed to find the last digit of (b! / a!), which would make sense. Let's check:

For compute_Last_Digit(2,4), if it's (4! / 2!) = 24 / 2 = 12, last digit is 2. That matches the assertion.

Similarly, compute_Last_Digit(6,8) would be (8! / 6!) = 40320 / 720 = 56, last digit 6.

And compute_Last_Digit(1,2) is (2! / 1!) = 2 / 1 = 2, last digit 2.

Yes, that makes sense. So the function is supposed to compute (b! / a!) and return the last digit of that integer.

But wait, what if a > b? For example, a=4 and b=2. Then b! is 2, a! is 24. 2 / 24 is 0.0833..., which is less than 1. The last digit of 0.0833... is 0.

So, to generalize, the function should compute (b! / a!) if b >= a, else return 0.

Alternatively, it should compute the integer part of (b! / a!) and then return the last digit of that integer.

So, the first step is to handle the cases where b >= a.

Now, to compute the last digit, perhaps there's a pattern in the last digits of factorials. Let me think about the last digits of factorials:

1! = 1 → last digit 1
2! = 2 → 2
3! = 6 → 6
4! = 24 → 4
5! = 120 → 0
6! = 720 → 0
7! = 5040 → 0
And so on.

I notice that starting from 5!, the last digit is always 0 because factorials include the product of 5 and 2, which makes 10, hence the last digit is 0.

So, if a >= 5, then a! ends with 0. Similarly, b >= 5, then b! ends with 0.

But when computing (b! / a!), if both a and b are >=5, then (b! / a!) is (something ending with 0 / something ending with 0), which could be an integer ending with 0, 5, or other digits, depending on the actual numbers.

Wait, but how can we compute the last digit of (b! / a!) when both are ending with 0? Because (b! / a!) would be (b × (b-1) × ... × (a+1)) because a! = 1×2×...×a.

So, (b! / a!) is equal to (a+1) × (a+2) × ... × b.

But if both a and b are >=5, then (b! / a!) is a product of numbers including at least a 5 and an even number, making it also end with 0.

Wait, for example, (10! / 5!) = 30240 → last digit 0.
(10! / 6!) = 5040 → last digit 0.
(10! / 7!) = 720 → last digit 0.
(10! / 8!) = 90 → last digit 0.
(10! / 9!) = 10 → last digit 0.
(10! / 10!) = 1 → last digit 1.

Wait, but when a=10 and b=10, it's 10! / 10! = 1, last digit 1.

So, there's an exception when a = b: the result is 1, so last digit is 1.

Similarly, when a < b, but a and b are >=5, the last digit could be 0, except in cases where a and b are such that the division results in a number ending with 1.

But handling all these cases manually would be complicated.

Alternatively, perhaps there's a mathematical pattern to find the last digit of (b! / a!).

Let me think about the cases:

Case 1: a > b → (b! / a!) is 0 because a! is larger than b! for a > b.

Wait, no. For example, a=2 and b=4: (4! / 2!) = 24 / 2 = 12 → last digit 2.

But a=3 and b=2: (2! / 3!) = 2 / 6 = 0.333... → not an integer, so the integer division is 0. So the last digit is 0.

So, to get an integer result, b! must be divisible by a!.

But when is b! divisible by a!?

Well, if a >= b, then a! includes b! as a factor. For example, 4! = 24, 2! = 2 → 24 is divisible by 2.

Similarly, 5! is divisible by 3!, 4!, etc.

But when a < b, a! is not a factor of b! because b! = a! * (a+1) * ... * b.

So, when a < b, (b! / a!) is an integer equal to (a+1)*(a+2)*...*b.

But when a = b, (b! / a!) = 1.

So, the function can be broken down into:

if a > b: return 0

elif a == b: return 1

else: compute (b! / a!) and return last digit

Now, to compute (b! / a!) when a < b.

But computing factorials directly for large numbers could be computationally expensive, but since we only need the last digit, perhaps we can find a pattern or simplify the computation.

Another observation: For the product (a+1)*(a+2)*...*b, the last digit can be determined by considering the last digits of the factors.

Also, note that multiplying by 5 and 2 in the product can lead to the last digit being 0, because 5 * 2 = 10.

So, if in the product (a+1)*(a+2)*...*b, there is at least one multiple of 5 and at least one multiple of 2, the last digit will be 0.

Otherwise, we can compute the product modulo 10.

But wait, let's see:

For example, 7! / 5! = 7*6 = 42 → last digit 2

9! / 5! = 9*8*7*6 = 3024 → last digit 4

6! / 5! = 6 → last digit 6

10! / 5! = 10*9*8*7*6 = 30240 → last digit 0

10! / 6! = 10*9*8*7 = 5040 → last digit 0

So, when the product includes both 5 and an even number (like 2,4,6,8, etc.), the last digit is 0.

Else, it depends on the product.

But handling all these cases manually would be complicated.

So, the plan is:

1. If a > b: return 0

2. If a == b: return 1

3. Else:

   a. Compute the product P = (a+1) * (a+2) * ... * b

   b. Since we only need the last digit of P, we can compute the product modulo 10.

   c. However, to avoid computing large numbers, we can compute the product step by step, taking modulo 10 at each step.

But to compute P modulo 10, we can multiply each number from a+1 to b, taking modulo 10 at each step.

But even better, since if at any point we multiply by a 0, 5, or 2/4/6/8, and get a 0 or 5, we can break early.

Let me formalize this:

Initialize last_digit = 1

for i from a+1 to b:

   last_digit *= i

   last_digit %= 10

So, for example:

a=2, b=4:

i=3: 1 *3 =3 → mod10=3

i=4: 3*4=12 → mod10=2 → returns 2.

Which matches the first assertion.

Another example:

a=1, b=2:

i=2: 1*2=2 → mod10=2 → returns 2.

Which matches the third assertion.

Another example:

a=6, b=8:

i=7: 1*7=7

i=8: 7*8=56 → mod10=6 → returns 6.

Which matches the second assertion.

Another example:

a=3, b=6:

i=4: 1*4=4

i=5: 4*5=20 → mod10=0

i=6: 0*6=0 → mod10=0 → returns 0.

So, when any multiple of 5 is multiplied, unless it's the first multiple and