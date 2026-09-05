import math
from typing import List

def min_Ops(nums: List[int], n: int, k: int) -> int:
    """
    Find the minimum number of operations to make all elements equal.
    An operation consists of choosing one element and adding k to it.

    If it's impossible to make all elements equal (because of modulo mismatch),
    return -1.

    The logic:
    1. Compute the required remainder for all elements. Since we can only add k,
       all elements must have the same remainder modulo k.
    2. Calculate the difference (min_element - each element). If any is negative,
       we need to find how many k-steps to bridge the gap.
    3. Sum up all necessary steps.

    However, the problem constraints and examples suggest a specific behavior:
    - We can only ADD k. So if an element is less than the target, we add k repeatedly.
      But since we can only add, we can't reduce numbers.
      Therefore, the target must be >= max(nums).
      Actually, re-reading the problem with the examples:
      Example 2: [4,2,6,8] with k=3. 
      4%3=1, 2%3=2, 6%3=0, 8%3=2. Remainders are not uniform -> impossible -> -1.
      Example 3: [21,33,9,45,63] with k=6.
      21%6=3, 33%6=3, 9%6=3, 45%6=3, 63%6=3. Remainders are uniform.
      Target must be such that (target - x) is divisible by 6 and target >= x.
      To minimize operations, target should be the smallest number >= max(nums) 
      that has the same remainder. Here max is 63. 63%6=3. So target=63.
      Diff: 21->63 (3 steps), 33->63 (3 steps), 9->63 (6 steps), 45->63 (1 step), 63->63 (0).
      Total = 3+3+6+1+0 = 13. But the assertion says 24.

      Let's re-evaluate the example 3: 24 operations.
      Maybe the operation is different? Or maybe we must make them ALL equal to a specific value?
      Wait, the problem statement says "k number of operations". This usually implies we perform exactly k operations?
      But the question asks to "find k number of operations required". This phrasing is ambiguous.
      Usually, "find k operations" means "find the minimum operations where k is a parameter".
      But the signature is min_Ops(nums, n, k). 
      n is length, k is the step size.

      Let's look at the result 24 for [21,33,9,45,63] and k=6.
      If the target is not the max, but some larger number?
      Suppose target = T.
      (T-21)%6 == 0, (T-33)%6==0, etc.
      T = 63 + 6*x.
      Steps for 21: (T-21)/6 = x + 8
      Steps for 33: (T-33)/6 = x + 6
      Steps for 9: (T-9)/6 = x + 10
      Steps for 45: (T-45)/6 = x + 4
      Steps for 63: (T-63)/6 = x
      Total steps = 4x + 28.
      If Total = 24, then 4x + 28 = 24 -> 4x = -4 -> x = -1.
      This implies T = 63 - 6 = 57.
      But we can only ADD k. We cannot reduce 63 to 57.

      Is it possible the operation is: Choose an element and ADD k OR SUBTRACT k?
      If we can subtract, we find the median.
      Median of [21, 33, 9, 45, 63] is 33.
      |21-33| = 12 (2 ops of 6)
      |33-33| = 0
      |9-33| = 24 (4 ops)
      |45-33| = 12 (2 ops)
      |63-33| = 30 (5 ops)
      Total = 2+0+4+2+5 = 13. Still not 24.

      Let's reconsider the example output 24.
      Sum of differences: 12+24+12+30 = 78. 78 / 6 = 13.
      How do we get 24?
      Maybe the problem is: Make all elements equal using exactly k operations? No, "find k number of operations required" usually means calculate the count.

      Wait, could the operation be: Add k to TWO elements? Or split k?
      Let's look at the first example: [2,2,2,2], k=3 -> 0. Correct.
      Second: [4,2,6,8], k=3 -> -1. (Remainders 1,2,0,2 -> mismatch). Correct.
      Third: [21,33,9,45,63], k=6 -> 24.

      Hypothesis: The problem might be "Make all elements equal to the maximum element" but the operation definition is different?
      Or maybe "k" in the problem description text "find k number of operations" is a typo in my understanding and "k" in the function is the step size.

      Let's try summing absolute differences divided by k again. 13.
      Why 24?
      24 * 6 = 144.
      Is there a target T such that sum(|T-x|) = 144?
      Try T = 63 + 60 = 123.
      |21-123|/6 = 17
      |33-123|/6 = 15
      |9-123|/6 = 19
      |45-123|/6 = 13
      |63-123|/6 = 15
      Sum = 17+15+19+13+15 = 79. No.

      What if the operation is: Pick one number, add k. BUT we want to make them ALL equal to a specific value, say the sum? No.

      Alternative interpretation:
      Maybe the question implies we can swap? No.

      Let's look at the numbers again: 21, 33, 9, 45, 63.
      Sorted: 9, 21, 33, 45, 63.
      Differences between adjacent: 12, 12, 12, 12.
      This is an arithmetic progression with diff 12.
      k=6.
      So each step is half the gap.
      To make them equal, we need to move the smaller ones up and larger ones... wait, if we can only add, we can't move larger ones down.
      Unless... the operation is "Add k to one, Subtract k from another"? That preserves sum.
      If we can add to one and subtract from another to equalize:
      Target = Median = 33.
      Moves:
      21 -> 33 (+12) : 2 ops (add k twice, remove nothing? No, we need to remove from somewhere else)
      Actually, if we can transfer value:
      21 needs +12. 33 needs 0. 9 needs +24. 45 needs -12. 63 needs -30.
      Net change needed: +12 +0 +24 -12 -30 = -6. Sum is not preserved relative to target if we just adjust.
      But if we can add to one and subtract from another, the sum is invariant? No, +k and -k keeps sum constant.
      Current sum = 171. Target sum = 5 * 33 = 165.
      We need to reduce sum by 6. But we can only do +/-k.
      This suggests we might not be able to reach 33.
      But the example says 24.

      Let's try a different target.
      Maybe the target is such that the number of operations is minimized, and operations can be +/- k?
      If +/- k allowed, target is median (33). Total distance = 78. Ops = 78/6 = 13.

      Is it possible the problem asks for the number of operations if we can ONLY ADD, but we want to make them equal to a value that results in 24 operations?
      Or maybe "k number of operations" in the prompt text is misleading and the variable k is something else?
      No, the signature is min_Ops(nums, n, k).

      Let's check the calculation for 24 again.
      Maybe the target is the MAX element + something?
      If target = 63. Ops = 13.
      If target = 63 + 6 = 69.
      21->69: 48/6 = 8
      33->69: 36/6 = 6
      9->69: 60/6 = 10
      45->69: 24/6 = 4
      63->69: 6/6 = 1
      Sum = 8+6+10+4+1 = 29.

      What if the operation is: "Select one element, add k. Repeat k times?" No.

      Wait, look at the example 24 again.
      Sum of differences = 78.
      78 / 6 = 13.
      24 is exactly double 12? No.
      24 * 6 = 144.
      144 - 78 = 66.

      Is it possible the problem is: "Find the minimum operations to make all elements equal" where an operation is "Add k to ALL elements"? No, that doesn't change equality.

      Let's reconsider the standard problem "Minimum Operations to Equalize Elements".
      Usually, if subtraction is allowed, it's sum(|x - median|) / k.
      If only addition is allowed, it's impossible unless all x % k are equal, and target >= max(x).
      Min operations = sum((max(x) - x) / k).
      For [21, 33, 9, 45, 63], k=6.
      Max = 63.
      (63-21)/6 = 7
      (63-33)/6 = 5
      (63-9)/6 = 9
      (63-45)/6 = 3
      (63-63)/6 = 0
      Sum = 7+5+9+3+0 = 24.

      YES! That matches 24.
      So the logic is:
      1. Check if all elements % k are equal. If not, return -1.
      2. Find the maximum element.
      3. Calculate sum((max - x) / k) for all x.
      4. Return that sum.

      This logic fits:
      Ex 1: [2,2,2,2], k=3. Max=2. All 0. Sum=0. Matches.
      Ex 2: [4,2,6,8], k=3. 
        4%3=1, 2%3=2. Mismatch. Return -1. Matches.
      Ex 3: [21,33,9,45,63], k=6.
        21%6=3, 33%6=3, 9%6=3, 45%6=3, 63%6=3. Match.
        Max=63.
        Sum = (63-21)/6 + (63-33)/6 + (63-9)/6 + (63-45)/6 + (63-63)/6
             = 42/6 + 30/6 + 54/6 + 18/6 + 0
             = 7 + 5 + 9 + 3 + 0 = 24. Matches.

      So the algorithm is:
      1. Verify all nums[i] % k are equal. If not, return -1.
      2. Find max_val = max(nums).
      3. Return sum((max_val - x) for x in nums) // k.

      Note: Since we verified modulo, (max_val - x