def check_last(arr: list, operations_count: int, p: int) -> str:
    """
    Determines whether the last element of the array is even or odd after performing
    an operation p times, where the operation involves modifying the last element
    based on the count of operations.

    Operation Logic:
    1. The problem implies that the 'operation' affects the parity of the last element.
    2. Based on the provided test cases, the pattern suggests that the operation involves
       shifting the index or modifying the value in a way that depends on the number of
       operations and the value p.
    3. After analyzing the test cases:
       - check_last([5,7,10], 3, 1) -> "ODD": Last element 10 is even. Result ODD.
       - check_last([2,3], 2, 3) -> "EVEN": Last element 3 is odd. Result EVEN.
       - check_last([1,2,3], 3, 1) -> "ODD": Last element 3 is odd. Result ODD.

    Hypothesis: The operation effectively toggles the parity of the last element if 
    (operations_count * p) is odd, or keeps it same if even. Alternatively, it might 
    be a specific mathematical transformation.

    Let's re-evaluate based on a simpler model often found in such problems:
    The operation might be: last_element = (last_element + operations_count * p)
    But let's look at the parity change:
    Case 1: 10 (even) -> ODD. Change required: +1 or -1 (odd). ops=3, p=1 -> 3*1=3 (odd).
    Case 2: 3 (odd) -> EVEN. Change required: -1 or +1 (odd). ops=2, p=3 -> 2*3=6 (even). 
               Wait, if 3 (odd) becomes EVEN, we need an odd change. But 6 is even.
               This contradicts the simple addition hypothesis.

    Alternative Hypothesis:
    Maybe the operation is not on the value, but the problem statement is slightly 
    ambiguous and refers to a known pattern where the result depends on the parity of 
    (operations_count * p) and the original parity.

    Let's try: result_parity = original_parity XOR ((operations_count * p) % 2)
    Case 1: 10 (even=0) XOR (3*1=3 -> 1) = 1 (ODD). Matches.
    Case 2: 3 (odd=1) XOR (2*3=6 -> 0) = 1 (ODD). But expected EVEN. Mismatch.

    Let's try another perspective. Maybe the 'operation' is defined differently.
    What if the operation shifts the effective index?
    Or what if the formula is: (last_element + operations_count) % 2 ?
    Case 1: (10 + 3) = 13 (ODD). Matches.
    Case 2: (3 + 2) = 5 (ODD). Expected EVEN. Mismatch.

    What if the formula involves p?
    Let's reconsider the second case: [2,3], ops=2, p=3 -> EVEN.
    Last element is 3 (odd). To get EVEN, we need to subtract/add an odd number.
    If the operation is: new_val = old_val + (operations_count * p)
    Case 2: 3 + (2*3) = 9 (ODD). Still ODD. Expected EVEN.

    Is it possible the operation is: new_val = old_val * (operations_count + p) ?
    Case 1: 10 * (3+1) = 40 (EVEN). Expected ODD. Mismatch.

    Let's look at the problem statement again: "performing an operation p times".
    Maybe the operation is simply adding p to the last element, repeated 'operations_count' times?
    Total added = operations_count * p.
    Parity change = (operations_count * p) % 2.
    Case 1: 10 (E) + 3 (O) = O. Correct.
    Case 2: 3 (O) + 6 (E) = O. Expected E. Incorrect.

    Is it possible the array indices are involved?
    Perhaps the operation affects the element at index (operations_count) mod len?
    But the problem says "last element".

    Let's try to reverse engineer Case 2 again:
    Input: [2,3], ops=2, p=3. Output: EVEN.
    Last element is 3. 
    If the operation was: new_val = (last_element * operations_count) % (p + something)? No.

    Wait, could the "operation" be defined as: 
    For each of the 'operations_count' steps, update the last element by some function of p?
    Or maybe the variable 'p' in the function signature is not the multiplier but the step size?

    Let's try a different pattern. What if the logic is:
    result = (arr[-1] + operations_count * p) 
    But we saw that fails for case 2.

    What if the logic is: result = (arr[-1] + p) % operations_count?
    Case 1: (10+1)%3 = 11%3 = 2 (EVEN). Expected ODD.

    Let's reconsider the inputs and outputs carefully.
    1. [5,7,10], ops=3, p=1 -> ODD. (10 is even)
    2. [2,3], ops=2, p=3 -> EVEN. (3 is odd)
    3. [1,2,3], ops=3, p=1 -> ODD. (3 is odd)

    Observation:
    In Case 1: Even input -> Odd output.
    In Case 3: Odd input -> Odd output.
    In Case 2: Odd input -> Even output.

    This implies that in Case 1 and 3, the parity is preserved or flipped differently than Case 2.
    Let's check the product of operations_count and p:
    Case 1: 3 * 1 = 3 (Odd)
    Case 2: 2 * 3 = 6 (Even)
    Case 3: 3 * 1 = 3 (Odd)

    If (ops * p) is Odd:
      Case 1 (Even input) -> Odd output. (Flipped)
      Case 3 (Odd input) -> Odd output. (Flipped)
      So if (ops*p) is Odd, flip parity?
      Case 1: E -> O (Flip). Correct.
      Case 3: O -> O (Flip). Correct (O -> E? No, O->O is no flip).
      Wait, Case 3 input is 3 (Odd). Output ODD. So no flip?
      But Case 1 input is 10 (Even). Output ODD. So flip?

      This suggests the flip logic depends on something else.

    Let's try: result_parity = (arr[-1] + operations_count) % 2
    Case 1: (10+3) = 13 -> ODD. Correct.
    Case 2: (3+2) = 5 -> ODD. Expected EVEN. Incorrect.

    Let's try: result_parity = (arr[-1] + p) % 2
    Case 1: (10+1) = 11 -> ODD. Correct.
    Case 2: (3+3) = 6 -> EVEN. Correct.
    Case 3: (3+1) = 4 -> EVEN. Expected ODD. Incorrect.

    Let's try: result_parity = (arr[-1] + operations_count * p) % 2
    Case 1: (10 + 3) = 13 -> ODD. Correct.
    Case 2: (3 + 6) = 9 -> ODD. Expected EVEN. Incorrect.

    Is it possible the operation is: arr[-1] = (arr[-1] * operations_count) % p? No, p=1 in case 1.

    What if the operation is applied p times, and we are checking the state after operations_count operations?
    Or "performing an operation p times" means the total count is p, but the function takes 'operations_count'?
    The description says: "check whether the last element ... after performing an operation p times."
    But the function signature is check_last(arr, operations_count, p).
    Usually, this means we perform 'operations_count' operations, where each operation uses parameter 'p'.
    Or we perform 'p' operations, and 'operations_count' is the value to use?

    Let's re-read the assertion description carefully:
    "check whether the last element of given array is even or odd after performing an operation p times."
    This phrasing is slightly ambiguous. It could mean:
    1. We perform an operation, and we do it 'p' times. The variable 'operations_count' in the function might be irrelevant or used differently?
    2. We perform 'operations_count' operations, and each operation involves the number 'p'.

    Given the function signature `check_last(arr, operations_count, p)`, it is highly likely that:
    - `operations_count` is the number of times the operation is performed.
    - `p` is a parameter of the operation.

    Let's assume the operation is: `x = x + p`.
    Total change = operations_count * p.
    We already tested this and it failed Case 2.

    What if the operation is: `x = x * p`?
    Case 1: 10 * 3 * 1 = 30 (Even). Expected Odd. Fail.

    What if the operation is on the index?
    Maybe the problem implies: "The last element becomes the element at index (last_index + operations_count) % len"?
    Case 1: Len=3. Last index=2. New index = (2+3)%3 = 2. Element=10 (Even). Expected Odd. Fail.

    Let's try a completely different approach. Look at the parity of the result directly.
    Case 1: Input 10 (E), Ops 3, p 1 -> O
    Case 2: Input 3 (O), Ops 2, p 3 -> E
    Case 3: Input 3 (O), Ops 3, p 1 -> O

    Notice the inputs in Case 2 and 3 are the same parity (Odd), but results differ.
    Case 2: Ops=2 (Even), p=3 (Odd). Product=Even.
    Case 3: Ops=3 (Odd), p=1 (Odd). Product=Odd.

    So if Product is Odd -> Result is Odd (from Odd input in Case 3).
    If Product is Even -> Result is Even (from Odd input in Case 2).

    Now check Case 1: Input 10 (Even). Product 3*1=3 (Odd). Result Odd.
    Rule: If Product is Odd -> Flip Input Parity?
    Case 1: Even -> Flip -> Odd. Correct.
    Case 3: Odd -> Flip -> Even. But Result is Odd. Incorrect.

    Wait, Case 3: Input 3 (Odd), Ops 3, p 1. Product 3 (Odd). Result Odd.
    So if Product is Odd, the result is the SAME as input?
    Case 3: Same.
    Case 1: Different.

    This is inconsistent. There must be a property of the input array or the specific values.
    Maybe the operation is: `arr[-1] = (arr[-1] + operations_count) % (p + 1)`? No.

    Let's reconsider the "operation p times" part.
    "after performing an operation p times" -> Maybe `p` is the count, not `operations_count`?
    If `p` is the count of operations:
    Case 1: p=1. 1 operation. What is the operation? `x = x + operations_count`?
    10 + 3 = 13 (Odd). Correct.
    Case 2: p=3. 3 operations. `x = x + operations_count` each time?
    3 + 2 + 2 + 2 = 9 (Odd). Expected Even. Fail.
    Or `x = x + p`? 3 + 3*3 = 12 (Even). Correct.
    Case 3: p=1. 1 operation. `x = x + p`? 3 + 1 = 4 (Even). Expected Odd. Fail.

    What if the operation is `x = x + operations_count`, repeated `p` times?
    Total added = p * operations_count.
    Case 1: 1 * 3 = 3. 10 + 3 = 13 (Odd). Correct.
    Case 2: 3 * 2 = 6. 3 + 6 = 9 (Odd). Expected Even. Fail.

    Is it possible the operation is `x = (x * operations_count) % (p + 1)`? No.

    Let's look at the problem source or