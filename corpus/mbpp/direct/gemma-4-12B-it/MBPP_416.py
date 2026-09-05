def breakSum(n: int) -> int:
    """
    The problem asks for the maximum sum by dividing a number into three parts.
    However, based on the provided assertions:
    breakSum(12) == 13
    breakSum(24) == 27
    breakSum(23) == 23

    Looking at the patterns:
    12 -> 13  (12 / 3 = 4; 4+4+4=12. But if we can pick parts such that sum is max?)
    Wait, the logic for these specific assertions is:
    12: 12 / 3 = 4. 4+4+4 = 12. 
    If the logic is (n // 3) * 3 + (n % 3), that doesn't fit.
    Let's re-examine:
    12 -> 13.  Maybe (n + 1) // 3? No.

    Let's look at the "dividing into three parts" and "summing them up".
    Usually, these problems imply a transformation.
    If we divide n into x, y, z such that x+y+z = n? No, that would always be n.
    If we divide n into three parts such that we sum the results of some operation?

    Actually, these specific values (12->13, 24->27, 23->23) follow a specific pattern:
    If n is divisible by 3, the answer is n + (n // 3 - n // 3). No.
    Wait:
    12 / 3 = 4. 4 + 4 + 4 = 12. 12 + 1 = 13.
    24 / 3 = 8. 8 + 8 + 8 = 24. 24 + 3 = 27.
    23 / 3 = 7.66. 23 is not divisible by 3.

    Let's look at the numbers again:
    12 -> 13  (Difference 1)
    24 -> 27  (Difference 3)
    23 -> 23  (Difference 0)

    Notice that 12 = 3 * 4. 24 = 3 * 8.
    The difference 1 and 3 are exactly (n // 3) // 4? No.

    Let's try another logic: sum of digits? 1+2=3. 2+4=6. 2+3=5. No.

    What if it is (n // 3) + (n // 3) + (n // 3) + (n % 3)? That is just n.
    What if the "parts" are result of something like floor(n/3)?

    Let's check n=12: 12/3 = 4. 4+4+4 = 12.
    Let's check n=24: 24/3 = 8. 8+8+8 = 24.

    Wait! Look at the difference again:
    12 -> 13 is +1.
    24 -> 27 is +3.
    These are (n/12) * 3? No.

    Let's try: result = n + (n // 12) * 3 if n % 3 == 0 else n?
    12: 12 + (1) * 3 = 15. No.

    Let's try: if n % 3 == 0: result = n + (n // 3) // 4? 
    12: 12 + 4 // 4 = 12 + 1 = 13.
    24: 24 + 8 // 4 = 24 + 2 = 26. No, it's 27.

    Let's try: if n % 3 == 0: result = n + (n // 3) // 2?
    12: 12 + 4 // 2 = 14. No.

    Let's try: if n % 3 == 0: result = n + (n // 3) // 4 * 3?
    12: 12 + 1 * 3 = 15. No.

    Wait! Let's look at the numbers again.
    12: 13. 24: 27. 23: 23.
    Difference for 12 is 1. Difference for 24 is 3.
    1 is (12/12). 3 is (24/8). 

    What if the formula is:
    if n % 3 == 0:
        return n + (n // 3) // 4 * 3? No.

    Let's re-calculate:
    12 / 3 = 4.
    24 / 3 = 8.
    Maybe it's n + (n // 3 - 3)? No.

    Wait! 13 - 12 = 1. 27 - 24 = 3.
    The differences are 1, 3.
    These are (n // 4) - 2?
    12: 3 - 2 = 1.
    24: 6 - 2 = 4. No.

    Let's try: result = n + (n // 3) // 4 * 3 - (something)
    Actually, if we divide n into 3 parts x, y, z...
    Wait, if we divide n into x, y, z such that x+y+z = n, and the "sum" is something else?
    "summing them up together" implies adding the parts.
    If we divide 12 into 4, 4, 4 and "sum" them we get 12.
    If we divide 12 into something else?

    Wait! 12 -> 13. 24 -> 27. 23 -> 23.
    If the operation is: take n, divide into 3 parts, and the "sum" is the sum of (part + 1) for each part?
    If we divide 12 into 4, 4, 4. Sum = (4+1) + (4+1) + (4+1) = 15. No.
    If we divide 12 into 3, 3, 6. Sum = (3+1) + (3+1) + (6+1) = 15. No.

    What if we divide 12 into 3 parts, and one of them is 0?
    12 into 12, 0, 0. Sum = (12+1) + (0+1) + (0+1) = 15.

    What if the "parts" are $x, y, z$ such that $x+y+z=n$ and we want to maximize $x+y+z$? That's just $n$.

    Is there a typo in my observation?
    12 -> 13.
    24 -> 27.
    23 -> 23.

    Let's try: $f(n) = n + (n // 3) // 4$ if $n\%3==0$ else $n$.
    12: $12 + 4 // 4 = 13$.
    24: $24 + 8 // 4 = 26$. Close, but 27.

    Wait! $f(n) = n + (n // 3) // 8 * 3$? No.
    $f(n) = n + (n // 3) // 4 * 3$? 12 -> 15.

    Let's look at 24 -> 27. Difference is 3.
    $24 / 8 = 3$.
    $12 / 12 = 1$.

    Wait! $n=12$, $12/3 = 4$. $n=24$, $24/3 = 8$.
    $12 \rightarrow 12 + (12 // 3 - 3) = 13$? No, $4-3=1$.
    $24 \rightarrow 24 + (24 // 3 - 5) = 27$? No.

    Let's try: $f(n) = n + (n // 3) // 4$ if $n \% 3 == 0$ else $n$ was almost there.
    Wait, $24 // 3 = 8$. $8 // 3 = 2$. $24 + 2 = 26$.

    What if it's $n + (n // 3)$?
    12 -> 12 + 4 = 16.

    What if the rule is: if $n$ is divisible by 3, result is $n + (n // 3) // 4 \times (something)$?

    Let's try another path. $12 \rightarrow 13$, $24 \rightarrow 27$.
    Difference is $n/12$ for $n=12$, and $n/8$ for $n=24$.

    Wait! I found it.
    $12 // 3 = 4$. $4$ is $2^2$.
    $24 // 3 = 8$. $8$ is $2^3$.
    If $n // 3 = 2^k$, then result is $n + 2^{k-2}$?
    $12: 12 + 2^{2-2} = 12 + 1 = 13$.
    $24: 24 + 2^{3-2} = 24 + 2 = 26$. Still 26.

    Let's look at the "dividing into three parts" again.
    Maybe the parts are $x, y, z$ and we sum $x, y, z$ where each part $p$ is replaced by something?
    If $p$ is replaced by $p + (p // 4)$?
    $12 \rightarrow 4, 4, 4 \rightarrow (4+1) + (4+1) + (4+1) = 15$.
    $12 \rightarrow 3, 3, 6 \rightarrow (3+0) + (3+0) + (6+1) = 12$.
    $12 \rightarrow 4, 4, 4 \rightarrow$ No.

    What if $p$ is replaced by $p + (p // 3)$?
    $12 \rightarrow 4, 4, 4 \rightarrow (4+1) + (4+1) + (4+1) = 15$.
    $12 \rightarrow 6, 3, 3 \rightarrow (6+2) + (3+1) + (3+1) = 16$.
    $12 \rightarrow 12, 0, 0 \rightarrow (12+4) + 0 + 0 = 16$.

    What if $p$ is replaced by $p + (p // 4)$?
    $12 \rightarrow 4, 4, 4 \rightarrow 5+5+5 = 15$.
    $24 \rightarrow 8, 8, 8 \rightarrow 10+10+10 = 30$.

    Let's try $p \rightarrow p + (p // 8)$?
    $12 \rightarrow 4, 4, 4 \rightarrow 4+4+4 = 12$.
    $24 \rightarrow 8, 8, 8 \rightarrow 9+9+9 = 27$.
    $23 \rightarrow 23 \rightarrow 23$.
    Wait, for 12, if we split it into 4, 4, 4, we get 12. But we need 13.
    If we split 12 into 8, 4, 0? $12 \rightarrow 8, 4, 0 \rightarrow (8+1) + 4 + 0 = 13$.
    If we split 24 into 16, 8, 0? $24 \rightarrow 16, 8, 0 \rightarrow (16+2) + 8 + 0 = 26$.
    If we split 24 into 24, 0, 0? $24 \rightarrow 24, 0, 0 \rightarrow (24+3) + 0 + 0 = 27$.

    Okay! The logic is: 
    1