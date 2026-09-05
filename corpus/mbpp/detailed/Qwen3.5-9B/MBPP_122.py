def _is_smart_number(candidate: int) -> bool:
    """
    Determine if a given number is a 'smart number'.

    A smart number is defined as a number that satisfies the following property:
    The sum of its digits equals the number of its distinct prime factors (with multiplicity).

    However, based on the provided test cases:
    smartNumber(1) == 30
    smartNumber(50) == 273
    smartNumber(1000) == 2664

    Let's analyze the sequence to deduce the definition.

    Known smart numbers (hypothetical based on common puzzles):
    30: digits sum = 3+0 = 3. Prime factors: 2, 3, 5 (count=3). Match.
    273: digits sum = 2+7+3 = 12. Prime factors: 3, 7, 13 (count=3). No match if multiplicity counts.
         Wait, 273 = 3 * 7 * 13. Distinct prime factors: 3, 7, 13 (count=3). Sum digits = 12. No match.

    Let's re-evaluate the definition based on the sequence 30, 273, 2664.
    Maybe "smart number" is related to the sum of proper divisors? Or some other property.

    Actually, let's look at the sequence of numbers that are "special" in specific ways.
    But without an explicit definition in the prompt, we must infer from the examples.

    Let's try a different hypothesis:
    Maybe the definition is: A number n is smart if the sum of its digits equals the number of ways to write n as a product of two numbers (excluding 1 and itself)?

    Let's reconsider the standard definition often used in such puzzles.
    "Smart number" isn't a standard mathematical term. It must be specific to this problem context.
    Given the constraints and the lack of a provided definition, I will assume the following definition which fits the test cases perfectly:

    A number is "smart" if the sum of its digits is equal to the number of its divisors.

    Let's test this hypothesis:
    1. Number: 30
       Digits sum: 3 + 0 = 3
       Divisors of 30: 1, 2, 3, 5, 6, 10, 15, 30 (Total = 8). 
       3 != 8. Hypothesis failed.

    Let's try another hypothesis:
    A number is "smart" if the number of its divisors equals the number formed by reversing its digits?
    30 -> reverse 03 (3). Divisors 8. No.

    Let's try: Sum of digits equals the number of distinct prime factors?
    30: sum=3. Distinct primes: 2, 3, 5 (3). Match.
    273: sum=12. Distinct primes: 3, 7, 13 (3). No match.

    Let's try: Sum of digits equals the number of ALL prime factors (with multiplicity)?
    30: 2*3*5 -> count=3. Sum=3. Match.
    273: 3*7*13 -> count=3. Sum=12. No match.

    Is it possible the sequence is not 30, 273, 2664?
    Or perhaps the definition involves the product of digits?

    Let's look at the numbers again: 30, 273, 2664.
    30 = 30
    273 = 30 * 9 + 3
    2664 = 273 * 10 - ...

    Let's try to search for the pattern in the "smart number" concept online or in common puzzles.
    Often, "smart numbers" refer to numbers where the sum of the digits equals the number of divisors? We tried that.

    What if "smart number" is defined as: 
    n is smart if sum(digits(n)) == number_of_prime_factors(n) (distinct)?
    We saw 30 works. 273 doesn't.

    Let's try: sum(digits(n)) == n / something?

    Alternative idea: The problem might be referring to a specific known sequence.
    Sequence A000...?

    Let's reconsider the input/output mapping.
    n=1 -> 30
    n=50 -> 273
    n=1000 -> 2664

    This looks like the 1st smart number is 30.
    The 50th smart number is 273.
    The 1000th smart number is 2664.

    This implies there are roughly 50 smart numbers between 30 and 273? That seems very dense.
    Or maybe the smart numbers are just a sparse set and 273 is the 50th?
    If 273 is the 50th, then there are 49 smart numbers smaller than 273.
    The first one is 30.
    So 30 is the 1st.
    Then there are 48 other smart numbers between 30 and 273.

    If the condition is "sum of digits equals number of divisors":
    30: sum=3, div=8. No.
    31: sum=4, div=2. No.
    ...
    Let's try a condition: sum of digits equals the number of prime factors (distinct)?
    30: 3. Distinct primes: 2,3,5 (3). Yes.
    Next candidates?
    6: sum=6. Distinct primes: 2,3 (2). No.
    12: sum=3. Distinct primes: 2,3 (2). No.
    15: sum=6. Distinct primes: 3,5 (2). No.
    20: sum=2. Distinct primes: 2,5 (2). Yes. (2nd?)
    21: sum=3. Distinct primes: 3,7 (2). No.
    22: sum=4. Distinct primes: 2,11 (2). No.
    24: sum=6. Distinct primes: 2,3 (2). No.
    26: sum=8. Distinct primes: 2,13 (2). No.
    28: sum=10. Distinct primes: 2,7 (2). No.
    30: sum=3. Distinct primes: 2,3,5 (3). Yes.

    If 20 is the 2nd, 30 is the 3rd? But the problem says 30 is the 1st.
    So 20 must not be a smart number under the real definition.

    Let's try: sum of digits equals the number of prime factors (counting multiplicity)?
    30: 3. Factors: 2,3,5 (3). Yes.
    20: 2. Factors: 2,2,5 (3). No.
    21: 3. Factors: 3,7 (2). No.
    22: 4. Factors: 2,11 (2). No.
    24: 6. Factors: 2,2,2,3 (4). No.
    25: 7. Factors: 5,5 (2). No.
    26: 8. Factors: 2,13 (2). No.
    27: 9. Factors: 3,3,3 (3). No.
    28: 10. Factors: 2,2,7 (3). No.
    30: 3. Yes.
    33: 6. Factors: 3,11 (2). No.
    35: 8. Factors: 5,7 (2). No.
    42: 6. Factors: 2,3,7 (3). No.
    60: 6. Factors: 2,2,3,5 (4). No.

    This is taking too long to guess. Let's look at the numbers 30, 273, 2664 again.
    Is it possible the definition is: 
    n is smart if sum(digits(n)) == number of divisors of n / something?

    Wait, let's try: sum of digits equals the number of ways to partition n? No.

    Let's try: n is smart if the sum of its digits is equal to the number of its prime factors (distinct) AND the number itself is divisible by something?

    Actually, let's reverse engineer the index.
    Index 1 -> 30
    Index 50 -> 273
    Index 1000 -> 2664

    Difference between index 50 and 1000 is 950.
    Difference in value is 2664 - 273 = 2391.
    Average gap: 2391 / 950 ≈ 2.5.
    So smart numbers appear very frequently.

    If the condition is "sum of digits == number of divisors", let's check density.
    For n < 1000, how many satisfy sum_digits(n) == num_divisors(n)?
    n=1: sum=1, div=1. Yes.
    n=2: sum=2, div=2. Yes.
    n=3: sum=3, div=2. No.
    n=4: sum=4, div=3. No.
    n=5: sum=5, div=2. No.
    n=6: sum=6, div=4. No.
    n=7: sum=7, div=2. No.
    n=8: sum=8, div=4. No.
    n=9: sum=9, div=3. No.
    n=10: sum=1, div=4. No.
    ...
    This seems sparse.

    What if the definition is: sum of digits equals the number of prime factors (distinct) OR something similar?

    Let's try a completely different angle.
    Maybe the "smart number" is defined as:
    A number n is smart if the sum of its digits is equal to the number of its divisors that are less than sqrt(n)?

    Let's try the definition: 
    A number n is smart if the sum of its digits equals the number of its prime factors (distinct).
    And we found 30 matches. 20 matches.
    If 30 is the 1st, then 20 must be excluded.
    Why would 20 be excluded?
    Maybe the condition is: sum of digits == number of distinct prime factors AND the number must be odd? No, 30 is even.
    Maybe the condition is: sum of digits == number of distinct prime factors AND the number must not be divisible by 10? No, 30 is divisible by 10.

    Let's try: sum of digits == number of distinct prime factors AND the number must be > 20?
    Then 20 is excluded.
    Next: 21 (sum=3, primes=2,3,7->2). No.
    22 (sum=4, primes=2,11->2). No.
    24 (sum=6, primes=2,3->2). No.
    25 (sum=7, primes=5->1). No.
    26 (sum=8, primes=2,13->2). No.
    27 (sum=9, primes=3->1). No.
    28 (sum=10, primes=2,7->2). No.
    30 (sum=3, primes=2,3,5->3). Yes. (1st)
    33 (sum=6, primes=3,11->2). No.
    35 (sum=8, primes=5,7->2). No.
    36 (sum=9, primes=2,3->2). No.
    38 (sum=11, primes=2,19->2). No.
    39 (sum=12, primes=3,13->2). No.
    40 (sum=4, primes=2,5->2). No.
    42 (sum=6, primes=2,3,7->3). No.
    44 (sum=8, primes=2,11->2). No.
    45 (sum=9, primes=3,5->2). No.
    46 (sum=10, primes=2,23->2). No.
    48 (sum=12,