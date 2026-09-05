def _get_absolute_value(n: int) -> int:
    """
    Returns the absolute value of the integer n.
    This helper is used to convert potentially negative inputs into their
    positive counterparts for the purpose of recursive breaking, as negative
    numbers generally yield lower or undefined sums in this specific context.
    """
    return n if n >= 0 else -n


def _calculate_recursive_max(current: int) -> int:
    """
    Recursively calculates the maximum sum obtainable by breaking the number 'current'
    into three parts (i, j, k) such that i + j + k = current.

    Logic:
    To maximize the sum of three parts, we need to find the optimal way to split
    the current number. Since breaking a number into three usually implies finding
    the maximum value for each part recursively, or simply summing the parts if
    they are small enough.

    The pattern observed from the examples:
    breakSum(12) -> 1+2+3+... is not the case. 
    Let's analyze 12 -> 13. 
    12 = 1 + 2 + 9? 13 = 12+1.
    Actually, this problem is a known variation where we break n into i + j + k.
    But wait, 12 -> 13. 12 = 3 + 3 + 3 = 9? No.
    Let's look at the standard interpretation of this specific riddle often found in coding challenges.
    It usually means: f(n) = max(i + f(j) + f(k)) where i+j+k=n and i,j,k >= 0.
    However, a simpler interpretation that fits 12->13, 24->27, 23->23 is:
    f(n) = max(n + k) where we break n into a, b, c.
    Actually, let's re-evaluate the examples carefully.

    Case 1: 12 -> 13.
    If we break 12 into 1, 1, 10 -> 1+1+10 = 12.
    If we break 12 into 1, 2, 9 -> 1+2+9 = 12.
    Maybe the function returns the max sum of parts where parts themselves can be broken?

    Hypothesis: This is the "Integer Break" problem but with a twist or a specific recursive definition.
    Standard Integer Break (LeetCode 343) for n=12 asks to break into at least two positive integers.
    12 = 4+4+4 -> 4*3 = 12. Or 5+4+3 -> 60. No, we are summing.

    Let's reconsider the problem statement: "dividing number in three parts recursively and summing them up".
    Perhaps it means: Sum = part1 + part2 + part3.
    And part1, part2, part3 can themselves be broken?

    Let's look at the specific numbers again:
    12 -> 13.
    24 -> 27.
    23 -> 23.

    Observation:
    12 + 1 = 13.
    24 + 3 = 27.
    23 + 0 = 23.

    Difference:
    13 - 12 = 1.
    27 - 24 = 3.
    23 - 23 = 0.

    This suggests the function might be f(n) = n + something?
    Or maybe it's related to the golden ratio? 3.618...
    Or maybe it's simple integer splitting.

    Let's try the recurrence: f(n) = max( i + j + k ) where i+j+k=n? That's always n.
    The word "recursively" is key.
    Does it mean: f(n) = max( i + f(j) + f(k) )?
    Let's test this hypothesis on 12.
    We need i + j + k = 12.
    Try to make i, j, k small so f(x) adds up to more than x?
    If f(x) > x for small x.
    f(1) = 1? f(2) = 2?
    If f(1) = 1, f(2) = 2.
    12 = 1 + 1 + 10. Sum = 1 + f(1) + f(10) = 1 + 1 + f(10).
    This path seems ambiguous without the base definition of "parts".

    Alternative Interpretation:
    This looks like the problem where you break a number into sum of parts to maximize the product, but here it asks for sum?
    No, the examples are sums.

    Let's look at the sequence of differences again: 1, 3, 0.
    Is it related to digits?
    12: 1+2 = 3. 12 + 1 = 13?
    24: 2+4 = 6. 24 + 3 = 27.
    23: 2+3 = 5. 23 + 0 = 23.

    Let's try to simulate the "break into three" logic where we break n into a, b, c.
    Maybe the "value" of a part x is defined by breaking it further until we reach single digits?
    If we break 12 into 1, 1, 10.
    10 -> break into 1, 1, 8?
    Eventually we get single digits. Sum of digits of 12 is 3. Sum of digits of 24 is 6. Sum of digits of 23 is 5.
    This doesn't match the deltas (1, 3, 0).

    Let's try the recurrence: f(n) = max_{a+b+c=n} (a + b + c + max(0, something))
    Actually, there is a very similar problem online: "Maximum Sum of Parts".
    But let's look at the constraints: 12->13, 24->27.
    13 = 1 + 1 + 11?
    27 = 3 + 3 + 21?

    Wait, could it be:
    f(n) = max( i + f(j) + f(k) )
    Base cases:
    If n < 10: return n.
    If n >= 10: try splitting into 1, 1, n-2?
    f(12) = 1 + 1 + f(10) = 2 + 1 + 1 + f(8) = ...
    If base case is n < 10, then f(8)=8.
    f(10) = 1 + 1 + 8 = 10. No change.

    What if the split is not 1,1,n-2?
    What if we split into 3, 3, 6?
    f(12) = 3 + 3 + 6 = 12.

    Let's reconsider the result 13 for input 12.
    Maybe the parts don't have to sum to n? "dividing number in three parts...". Usually implies sum is n.
    Is it possible the problem allows parts to be negative? No, "number" usually implies positive.

    Let's try a different recurrence:
    f(n) = max( i + j + k ) where i+j+k = n AND we apply the function recursively on i, j, k?
    But that just returns n if f(x)=x.
    Unless f(x) != x.
    When does f(x) != x?
    If we break a number into parts, the sum of parts equals the original.
    So the only way to increase the sum is if the "parts" are counted differently or if the recursion adds extra value.

    Is it possible the problem is:
    f(n) = n + (sum of digits of n) ?
    12 + 3 = 15. (Target 13). No.

    Let's go back to the most common puzzle matching these numbers.
    This is extremely similar to a specific logic puzzle found in some coding interviews:
    "Find the max sum by dividing n into 3 parts recursively".
    Actually, looking at 12->13 and 24->27.
    12 = 4 + 4 + 4.
    24 = 6 + 6 + 12 -> 6+6+9=21?

    Wait, I might be overthinking the "sum of parts" equality.
    "dividing number in three parts" -> i, j, k.
    "recursively" -> we can break i, j, k further.
    "summing them up" -> sum all the leaf nodes.
    If we break a number, the sum of the children equals the parent.
    So the total sum should always be the original number.
    UNLESS... the problem implies we can add the number itself plus the parts?
    "summing them up together for the given number"
    Maybe it means: Sum = n + sum(parts)?
    If so:
    12: break into 1, 1, 10. Sum = 12 + 1 + 1 + 10 = 24. Too high.

    Let's look at the deltas again: 1, 3, 0.
    Maybe it's related to the number of parts?
    Or maybe the "parts" are constrained to be specific values?

    What if the function is simply:
    return n if n < 10 else max( i + j + k ) where i, j, k are results of breaking?

    Let's try to reverse engineer 12 -> 13.
    We need an operation that yields 13 from 12.
    12 + 1 = 13.
    Where does the 1 come from?
    Maybe we break 12 into 1, 2, 9?
    f(1) = 1.
    f(2) = 2.
    f(9) = 9.
    Sum = 1+2+9 = 12.

    Is it possible the problem is actually:
    Maximize (part1 * part2 * part3)? No, "summing".

    Let's consider the possibility that the "parts" don't sum to N.
    "dividing number in three parts" -> i, j, k such that they are derived from N.
    Maybe i = floor(N/3), j = floor(N/3), k = N - 2*floor(N/3)?
    No, that's just partitioning.

    Let's try the solution that fits 12->13, 24->27, 23->23 in the context of typical "broken" integer puzzles.
    There is a known solution pattern:
    f(n) = n + (n // 3) ? 
    12 + 4 = 16. No.
    f(n) = n + (n % 3)?
    12 + 0 = 12. No.
    f(n) = n + 1 if n % 3 == 0? 12->13.
    24 % 3 == 0 -> 25. Target 27. No.

    Let's try: f(n) = max( i + j + k ) where i+j+k = n is not the constraint.
    Maybe the constraint is i, j, k must be integers >= 1 and we want to maximize sum of f(i)+f(j)+f(k)?
    If f(x) = x for small x, then sum = n.
    If f(x) increases for larger x?

    Wait, I found a matching pattern in a similar problem description online (though not exact).
    But let's look at the math again.
    12 -> 13 (+1)
    24 -> 27 (+3)
    23 -> 23 (+0)

    Hypothesis: The gain is related to how many times we can divide by 3?
    Or maybe the gain is (n // 3) - something?

    Let's try the recurrence: f(n) = max( a + b + c ) where a, b, c are parts of n, BUT we can only break n if n >= some threshold, and the value of a part is calculated recursively.

    Actually, let's assume the provided examples are the absolute truth and work backwards to the logic.
    What if the "parts" are not a sum, but a decomposition where we add the number of ways to split? No.

    Let's try this logic:
    To maximize sum, we should break n into as many small parts as possible? No, sum is constant.

    Is it possible the problem allows us to NOT use the full number?
    "dividing number in three parts" -> i, j, k.
    Maybe i + j + k < n is allowed? "Dividing