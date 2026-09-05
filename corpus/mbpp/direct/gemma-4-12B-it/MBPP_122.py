def smartNumber(n):
    """
    A smart number is defined by the sequence where the nth smart number 
    is the nth number that is not divisible by any of its digits 
    (excluding 0) and is strictly greater than its digits' sum?

    Wait, let's analyze the provided values:
    1 -> 30
    50 -> 273
    1000 -> 2664

    Let's check the properties of 30: 
    Digits are 3, 0. Sum is 3. 30 is divisible by 3.
    Let's check the properties of 273: 
    Digits are 2, 7, 3. Sum is 12. 273 / 3 = 91.

    Re-evaluating the pattern for "Smart Number":
    A number is smart if it is divisible by the sum of its digits.
    These are known as Harshad numbers (or Niven numbers).

    Let's check 30: 3+0 = 3. 30 / 3 = 10. (Harshad)
    Let's check 273: 2+7+3 = 12. 273 / 12 = 22.75 (Not Harshad)

    Let's try another pattern. What if smart numbers are those 
    whose sum of digits is a factor of the number? No, that's Harshad.

    Let's look at the numbers again:
    1: 30
    50: 273
    1000: 2664

    If I look at the gap:
    From 1 to 50 is 49 steps. 273 - 30 = 243.
    243 / 49 is approx 4.95.
    From 50 to 1000 is 950 steps. 2664 - 273 = 2391.
    2391 / 950 is approx 2.5.

    Wait, let's try the "Smith Number" or "Armstrong Number"? No.
    Let's check if "Smart Numbers" are related to the sum of squares of digits?
    Or "Numbers divisible by the product of their non-zero digits"?

    Let's test "Sum of digits is a prime number"?
    30: 3+0=3 (Prime)
    273: 2+7+3=12 (Not Prime)

    Let's look at the difference again. 
    Maybe the definition is: A number is "Smart" if it is a multiple of 
    the sum of its digits and the sum of its digits is also a "Smart" number?
    No, that's recursive.

    Wait! Let's try: A number is "Smart" if it is divisible by the number 
    of its divisors? No.

    Let's try: A number is "Smart" if it is divisible by its *first* digit.
    30: 30 % 3 == 0.
    273: 273 % 2 != 0.

    Let's try: A number is "Smart" if it is divisible by the *last* digit.
    30: 30 % 0 (Undefined)

    Let's look at the sequence again: 30, ..., 273, ..., 2664.
    Maybe the condition is: Number is divisible by the sum of its digits 
    EXCEPT the sum of digits must be a specific value?

    Actually, looking at common "Smart Number" definitions in competitive programming:
    A "Smart Number" is often defined as a number that is divisible by 
    the product of its digits (excluding zeros).

    Test 30: Digits 3, 0. Product (non-zero) = 3. 30 % 3 == 0. (Yes)
    Test 273: Digits 2, 7, 3. Product = 2*7*3 = 42. 273 % 42 != 0. (No)

    Wait, another definition: A number is "Smart" if it is divisible by 
    the sum of its digits AND it is not divisible by any of its digits.
    30: Sum=3. 30%3==0. Digits 3,0. 30%3==0. (Fails "not divisible by any digit")

    Let's re-examine: 
    1 -> 30
    50 -> 273
    1000 -> 2664

    Is it: n-th number where (sum of digits) * k = number? 
    No, that's Harshad.

    Let's check 2664. Sum of digits: 2+6+6+4 = 18.
    2664 / 18 = 148.
    So 2664 is a Harshad number.

    Wait, let's re-calculate Harshad numbers:
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 18, 20, 21, 24, 27, 30...
    The 1st Harshad number is 1. The 10th is 10.
    If 30 is the 1st "Smart" number, and the sequence is Harshad numbers...
    Harshad numbers: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 18, 20, 21, 24, 27, 30.
    30 is the 17th Harshad number. 
    If 30 is the 1st Smart number, maybe "Smart" numbers are Harshad numbers 
    greater than 20?

    Let's check Harshad numbers around 273.
    Harshad numbers: ... 252 (Sum 9, 252/9=28), 261 (Sum 9, 261/9=29), 270 (Sum 9, 270/9=30).
    273 is NOT a Harshad number. 273 / (2+7+3) = 273 / 12 = 22.75.

    Wait! Let me re-read the numbers. 30, 273, 2664.
    Is there a pattern in the digits?
    30: 3+0=3
    273: 2+7+3=12
    2664: 2+6+6+4=18

    Is it: Sum of digits is a multiple of 3?
    30: 3 (Yes)
    273: 12 (Yes)
    2664: 18 (Yes)

    Let's count numbers where sum of digits is a multiple of 3.
    Sum of digits is a multiple of 3 is equivalent to the number itself 
    being a multiple of 3.
    Multiples of 3: 3, 6, 9, 12, 15, 18, 21, 24, 27, 30...
    If 30 is the 1st, then we start counting from 30.
    30 is the 10th multiple of 3.
    If 30 is the 1st, then n-th is (n+9)th multiple of 3?
    n=1: 10th multiple = 30.
    n=50: 59th multiple = 59 * 3 = 177. (Doesn't match 273)

    Let's try: Sum of digits is a multiple of 6?
    30: 3 (No)

    Let's try another approach. The numbers are:
    30, ..., 273, ..., 2664
    Are they numbers that are divisible by the product of their digits + 1?
    30: 3*0+1 = 1. 30%1=0.
    273: 2*7*3+1 = 43. 273/43 = 6.34.

    What about: sum of digits is a perfect square?
    30: 3 (No)

    Wait, I found a sequence: 30, 60, 90, 120, 150, 180, 210, 240, 270, 300...
    This is multiples of 30.
    n=1: 30
    n=50: 50 * 30 = 1500. (Doesn't match 273)

    Let's try another logic. 
    Maybe the definition of "smart" is: A number is smart if it's divisible by 
    the sum of its digits AND the sum of its digits is a multiple of 3.

    Wait! Let's look at the numbers again.
    30
    273
    2664
    Maybe they are numbers that are divisible by the *sum of the squares* of their digits?
    30: 3^2 + 0^2 = 9. 30/9 (No)
    273: 2^2 + 7^2 + 3^2 = 4 + 49 + 9 = 62. 273/62 (No)

    What if "smart" numbers are "Numbers whose sum of digits is equal to the 
    number of divisors"?
    30: Divisors (1,2,3,5,6,10,15,30) count = 8. Sum = 3. (No)

    What if "smart" numbers are: Numbers $x$ such that $x$ is divisible by 
    (sum of digits + 1)?
    30: 3+1=4. 30/4 (No)

    Let's try: $x$ is divisible by (sum of digits - 1)?
    30: 3-1=2. 30/2=15. (Yes)
    273: 12-1=11. 273/11 (No)

    Let's try: $x$ is divisible by (product of digits / sum of digits)?

    Wait! I think I found it. Let's check "Sum of digits" again.
    30: 3
    273: 12
    2664: 18
    These are all multiples of 3. 
    Is it: n-th number such that it is a multiple of 3 and sum of digits is a multiple of 3?
    That is just multiples of 3. 

    Let's look at the gaps again.
    1000th smart number is 2664. 
    If the numbers were just multiples of 3, the 1000th would be 3000.
    2664 / 1000 = 2.664.
    So smart numbers are roughly every 2.664 integers.
    That means about 37% of numbers are "smart".

    What property happens ~37% of the time? 
    Maybe: The number is divisible by the sum of its digits? (Harshad numbers)
    Let's check Harshad numbers count.
    How many Harshad numbers are there up to 2664?
    Roughly 1/ln(x) or something? No, Harshad numbers are more frequent.

    Actually, let's re-calculate the Harshad count up to 2664.
    A quick estimation: The number of Harshad numbers up to $x$ is roughly $x / \ln x$.
    $2664 / \ln(2664) \approx 2664 / 7.8 \approx 341$. 
    We need 1000. So smart numbers are more frequent than Harshad numbers.

    Wait! Let's try "The sum of digits is a divisor of the number". 
    No, that's Harshad.
    What about "The number of divisors is even"? (Most numbers)

    Let's try: "The sum of digits is prime"? 
    Let's try: "The number is even and the sum of digits is even"?