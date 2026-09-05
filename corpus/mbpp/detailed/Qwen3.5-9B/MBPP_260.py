import math
import sys
from typing import Optional

def is_perfect_square(n: int) -> bool:
    """
    Check if an integer n is a perfect square.

    Edge cases handled:
    - Negative numbers: return False immediately.
    - Zero: returns True (0*0 = 0).
    - Positive numbers: compute integer square root and check square.

    Args:
        n (int): The integer to check.

    Returns:
        bool: True if n is a perfect square, False otherwise.
    """
    if n < 0:
        return False
    if n == 0:
        return True

    # Use integer arithmetic to avoid floating point precision issues for large numbers
    # We approximate the square root using math.isqrt (available in Python 3.8+)
    # If running on an older version, a binary search would be needed, but we assume modern Python.
    try:
        root = math.isqrt(n)
    except AttributeError:
        # Fallback for very old Python versions if needed (though unlikely in production now)
        root = int(n ** 0.5)
        # Adjust if floating point approximation was slightly off
        if (root + 1) ** 2 <= n:
            root += 1
        elif root ** 2 > n:
            root -= 1

    return root * root == n

def is_prime(n: int) -> bool:
    """
    Determine if a number is prime using trial division.

    Edge cases handled:
    - Numbers less than 2: not prime.
    - 2 and 3: prime.
    - Even numbers > 2: not prime.
    - Multiples of 3 > 3: not prime.
    - General case: check divisors up to sqrt(n).

    Args:
        n (int): The number to test for primality.

    Returns:
        bool: True if prime, False otherwise.
    """
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    # Check for factors of the form 6k +/- 1 up to sqrt(n)
    limit = math.isqrt(n)
    i = 5
    while i <= limit:
        if n % i == 0:
            return False
        if n % (i + 2) == 0:
            return False
        i += 6

    return True

def is_newman_shanks_williams_number(n: int) -> bool:
    """
    Check if a number n is a Newman-Shanks-Williams (NSW) number.

    The NSW numbers are defined by the recurrence:
    V_1 = 1, V_2 = 1, V_n = V_{n-1} + 2*V_{n-2} for n > 2.
    However, the sequence of NSW numbers typically starts indexing differently 
    in literature or the specific values provided in the problem (1, 7, 41, ...)
    suggest we are looking at a specific sequence.

    Let's derive the sequence based on the problem's expected outputs:
    - The problem asks for the 3rd NSW prime = 7
    - The problem asks for the 4th NSW prime = 17
    - The problem asks for the 5th NSW prime = 41

    Let's generate NSW numbers:
    Standard definition: S_0=0, S_1=1, S_n = S_{n-1} + 2*S_{n-2} (Sylvester sequence variant?)
    Actually, the Newman-Shanks-Williams sequence (OEIS A001353) is:
    a(0) = 0
    a(1) = 1
    a(n) = 2*a(n-1) + a(n-2) for n > 1.

    Sequence: 0, 1, 2, 5, 12, 29, 70, 169, 408, 985... (These are Pell numbers P_n)
    Wait, NSW numbers are defined as:
    V_1 = 1
    V_2 = 1
    V_n = V_{n-1} + 2*V_{n-2} ??? No, that gives 1, 1, 3, 7, 17, 41...
    Let's check the recurrence V_n = V_{n-1} + 2*V_{n-2}:
    V_1 = 1
    V_2 = 1
    V_3 = 1 + 2*1 = 3
    V_4 = 3 + 2*1 = 5 (Wait, 1,1,3,5 doesn't match 7, 17, 41)

    Let's try the recurrence relation often associated with NSW primes (related to Lucas sequences):
    P_0 = 0
    P_1 = 1
    P_n = 2*P_{n-1} + P_{n-2} -> This generates 0, 1, 2, 5, 12, 29...
    NSW numbers are often defined as V_n = P_n^2 + P_{n-1}^2? Or related to square numbers?

    Let's look at the numbers in the example: 7, 17, 41.
    Let's see if they fit V_n = 2*V_{n-1} + V_{n-2}:
    If V_k = 7, V_{k+1} = 17.
    17 = 2*7 + 3 -> Previous must be 3.
    7 = 2*3 + 1 -> Previous must be 1.
    3 = 2*1 + 1 -> Previous must be 1.
    1 = 2*1 + (-1)? No.

    Let's try the recurrence: V_n = 2*V_{n-1} + V_{n-2} starting from:
    V_1 = 1
    V_2 = 1
    V_3 = 2*1 + 1 = 3
    V_4 = 2*3 + 1 = 7  <-- Match! (This would be the 4th term if 1,1,3,7)
    V_5 = 2*7 + 3 = 17 <-- Match!
    V_6 = 2*17 + 7 = 41 <-- Match!

    So the sequence is defined as:
    V_1 = 1
    V_2 = 1
    V_n = 2*V_{n-1} + V_{n-2} for n > 2.

    The values are: 1, 1, 3, 7, 17, 41, 99, 239, 577...
    The problem asks for the "nth newman–shanks–williams prime number".
    assert newman_prime(3) == 7 (3rd NSW number is 3 (not prime), 4th is 7 (prime)).
    Wait, "3rd NSW prime number" means we filter the NSW sequence for primes, then take the 3rd one.
    NSW Sequence:
    Index (original): 1, 2, 3, 4, 5, 6
    Value: 1, 1, 3, 7, 17, 41
    Primes in NSW Sequence:
    - 1 is not prime.
    - 1 is not prime.
    - 3 is prime. (1st NSW prime)
    - 7 is prime. (2nd NSW prime)
    - 17 is prime. (3rd NSW prime) -> Assertion: newman_prime(3) == 7. Matches!
    - 41 is prime. (4th NSW prime) -> Assertion: newman_prime(4) == 17. Wait. 
      My manual count: 3(1st), 7(2nd), 17(3rd), 41(4th).
      Assertion says: newman_prime(3) == 7. This implies 7 is the 3rd prime?
      This implies 1, 1, 3 are NOT counted or 3 is not prime? 3 IS prime.

      Let's re-read the assertion carefully:
      assert newman_prime(3) == 7
      assert newman_prime(4) == 17
      assert newman_prime(5) == 41

      If 7 is the 3rd prime, then there are two primes before 7.
      Sequence: 1, 1, 3, 7...
      Primes: 3, 7... Only 2 primes before 7.
      Unless the sequence is 0-indexed in the problem statement's mind but the values are 1-based?
      Or maybe the sequence definition is different.

      Let's check OEIS A001353 (Newman-Shanks-Williams numbers):
      1, 1, 3, 7, 17, 41, 99, 239, 577, 1393...
      Primes in this sequence:
      3, 7, 17, 41, 239, 577...
      1st: 3
      2nd: 7
      3rd: 17
      4th: 41

      If the problem expects:
      n=3 -> 7
      n=4 -> 17
      n=5 -> 41

      This shifts my index by 1. 
      My 2nd prime (7) is the problem's 3rd.
      My 3rd prime (17) is the problem's 4th.
      My 4th prime (41) is the problem's 5th.

      This implies the problem considers 1 or 2 primes before 7 that are NOT in the standard sequence I generated, OR 
      the problem considers the first NSW number (1) as prime? No, 1 is not prime.
      OR maybe the sequence starts differently?
      What if the sequence is: 1, 7, 41... skipping 1, 3? No, that doesn't make sense.

      Let's reconsider the definition.
      Is it possible the problem counts the NSW numbers starting from index 0 or 1 differently?
      Or perhaps the "Newman-Shanks-Williams Prime" refers to a specific subset?

      Alternative Hypothesis:
      Maybe the sequence is 1, 1, 3, 7, 17, 41.
      If we count 1 as prime (historical error? No, mathematically false).
      If we count 1, 1, 3 as primes? Then 7 is 4th.

      Let's look at the numbers again: 7, 17, 41.
      Differences:
      17 - 7 = 10
      41 - 17 = 24

      Let's try to find a sequence where 7 is the 3rd prime.
      Primes: p1, p2, p3=7.
      Candidates for p1, p2: 2, 3, 5?
      Are 2 or 5 NSW numbers?
      If the sequence was: 2, 3, 7, 17, 41...
      How do we get 2?
      Recurrence: V_n = 2*V_{n-1} + V_{n-2}.
      If V_3 = 7, V_4 = 17.
      17 = 2*7 + x => x = 3. (V_2 = 3)
      7 = 2*3 + y => y = 1. (V_1 = 1)
      3 = 2*1 + z => z = 1. (V_0 = 1)
      Sequence: 1, 1, 3, 7, 17, 41.
      Primes: 3, 7, 17, 41.
      Counts: 3->1, 7->2, 17->3, 41->4.

      The problem assertions:
      newman_prime(3) == 7  (Implies 7 is the 3rd)
      newman_prime(4) == 17 (Implies 17 is the 4th)
      newman_prime(5) == 41 (Implies 41 is the 5th)

      There is a discrepancy of 1 index between standard math and the problem statement.
      Standard: 3 is 1st, 7 is 2nd.
      Problem: 7 is 3rd.

      Why would 7 be the 3rd?
      Maybe the sequence includes 2? 
      Is 2 an NSW number?
      If V_0=1, V_1=1, V_2=3,