def get_total_number_of_sequences(n, m):
    """
    Calculates the number of sequences of length n such that:
    1. Each element x_i is in the range [1, m].
    2. x_{i+1} >= 2 * x_i.

    The problem can be solved using dynamic programming.
    Let dp[i][j] be the number of sequences of length i ending with value j.

    The state transition:
    dp[i][j] = sum(dp[i-1][k]) for all k such that 2*k <= j.
    This is equivalent to sum(dp[i-1][k]) for k from 1 to floor(j/2).
    """
    if n == 0:
        return 0
    if n == 1:
        return m

    # dp[i][j] where i is current length, j is the last element's value
    # To save memory, we can use two rows since we only need the previous length's counts.
    # dp[j] will store the number of sequences of the current length ending in value j.
    dp = [1] * (m + 1)
    dp[0] = 0 # Values are from 1 to m

    for length in range(2, n + 1):
        new_dp = [0] * (m + 1)
        prefix_sum = 0
        # For a sequence of length 'length' ending in j,
        # the previous element k must satisfy 2*k <= j, i.e., k <= j // 2.
        for j in range(1, m + 1):
            # Update prefix_sum to include all valid k for current j
            # When j increases, the range of valid k (1 to j//2) might expand.
            # However, it's easier to just iterate and update prefix_sum correctly.
            # We want prefix_sum to be sum(dp[1...j//2])

            # Since we are iterating j from 1 upwards, j//2 only changes at even j.
            # Let's handle the prefix sum more cleanly:
            pass

        # Let's rewrite the logic for clarity:
        current_prefix_sum = 0
        k_ptr = 1
        for j in range(1, m + 1):
            while k_ptr <= j // 2:
                current_prefix_sum += dp[k_ptr]
                k_ptr += 1
            new_dp[j] = current_prefix_sum
        dp = new_dp

    return sum(dp)

# The provided assertions are actually quite specific. 
# Let's re-evaluate the constraints based on the test cases.
# Test 1: n=10, m=4. Sequences of length 10 with x_i+1 >= 2*x_i.
# If x_1=1, x_2>=2, x_3>=4, x_4>=8... but m=4. This means max length is small.
# Wait, the assertions:
# (10, 4) -> 4. This implies sequences can have values <= 4.
# If n=10, and max value is 4, and each step doubles, the only way to have 10 elements
# is if the values don't increase much? No, "greater than or equal to twice".
# 1 -> 2 -> 4 -> (next must be >= 8, but m=4). 
# This means for n=10, the only possible sequence is one where the doubling doesn't 
# exceed m. But 1*2^9 is way larger than 4.
# Re-reading: "each of the next element is greater than or equal to twice... less than or equal to m"
# This means x_1, x_2, ..., x_n.
# x_2 >= 2*x_1
# x_3 >= 2*x_2
# ...
# x_n >= 2*x_{n-1}
# And all x_i <= m.
# This implies x_1 * 2^(n-1) <= x_n <= m.
# If n=10, m=4, 1 * 2^9 = 512. 512 > 4. 
# There should be 0 sequences. But the assertion says 4.
# Let me re-read again. "greater than or equal to twice of the previous element but less than or equal to m"
# Does "less than or equal to m" apply to every element or just the last? 
# "each of the next element is ... less than or equal to m". 
# This usually means ALL elements x_i <= m.
# If n=10, m=4, and x_i+1 >= 2*x_i, and x_i >= 1.
# x_1 >= 1
# x_2 >= 2
# x_3 >= 4
# x_4 >= 8 (but x_4 <= 4, impossible).
# There is a misunderstanding. Let's look at the assertions again.
# (10, 4) -> 4. (5, 2) -> 6. (16, 3) -> 84.
# These numbers are large for such tight constraints.
# Could the condition be x_{i} >= 2 * x_{i-1} is NOT the constraint?
# "each of the next element is greater than or equal to twice of the previous element" 
# Wait, is it possible the sequence is decreasing? No, "greater than".
# Is it possible that m is the limit for the sum? No.
# Let's re-calculate (5, 2) -> 6. If n=5, m=2, and x_i+1 >= 2*x_i.
# If x_i can be 0? 0, 0, 0, 0, 0; 0, 0, 0, 0, 1; 0, 0, 0, 0, 2; 0, 0, 0, 1, 2; 0, 0, 1, 2, 2? 
# If x_i can be 0, and x_{i+1} >= 2*x_i:
# If x_i = 0, x_{i+1} >= 0.
# If x_i = 1, x_{i+1} >= 2.
# For (5, 2):
# x_1=0: x_2 can be 0,1,2.
# If x_2=0: x_3 can be 0,1,2.
# If x_2=1: x_3 can be 2.
# If x_2=2: x_3 can be 2 (since 2*2=4 > 2, only if 2*x_i <= x_{i+1} <= m).
# This is very confusing. Let's look at the numbers again.
# (16, 3) -> 84. 
# If the condition was x_{i} <= 2 * x_{i-1}?
# Or x_{i-1} >= 2 * x_i? (Decreasing)
# Let's try: x_i <= 2 * x_{i-1} and x_i <= m.
# For (5, 2): x_1 can be 1,2.
# x_1=1: x_2 <= 2. x_2=1: x_3=1,2. x_2=2: x_3=2.
# This doesn't seem to lead to 6.
# What if the elements are non-decreasing and the condition is x_{i} >= x_{i-1} + something?
# Let's try the most standard interpretation again: x_{i} \in [1, m] and x_{i} \ge 2x_{i-1}.
# If (5, 2) = 6, and n=5, m=2. If x_i can be 0.
# If x_i \in [0, m], x_i \ge 2x_{i-1}.
# n=1: {0, 1, 2} -> 3
# n=2: {0,0}, {0,1}, {0,2}, {1,2} -> 4
# n=3: {0,0,0}, {0,0,1}, {0,0,2}, {0,1,2}, {1,2,2} ... no.
# Let's try: x_i is the count of some property?
# What if the problem is: Number of sequences of length n where x_i \in [1, m] 
# and x_i \le 2 * x_{i-1}?
# For (5, 2): 
# x_1=1: x_2 \in {1,2}. If x_2=1, x_3 \in {1,2}. If x_2=2, x_3=2. (Total 3)
# x_1=2: x_2 \in {2}. If x_2=2, x_3=2, x_4=2, x_5=2. (Total 1)
# Still not 6.
# Let's try: x_i \in [1, m] and x_i \ge x_{i-1}. (Non-decreasing)
# (5, 2): {1,1,1,1,1}, {1,1,1,1,2}, {1,1,1,2,2}, {1,1,2,2,2}, {1,2,2,2,2}, {2,2,2,2,2} -> 6!
# This matches (5, 2) -> 6.
# Let's check (10, 4): Non-decreasing sequences of length 10 with values in [1, 4].
# Formula: Combination with replacement: (m + n - 1) choose n.
# (4 + 10 - 1) choose 10 = 13 choose 10 = 13*12*11 / 3*2*1 = 13*2*11 = 286.
# Not 4.
# Wait, the constraint is x_i >= 2 * x_{i-1}.
# If m is the max value, and we want sequences of length n.
# Is it possible that n is the maximum value and m is the length?
# No, the signature is (n, m).
# Let's re-read: "next element is greater than or equal to twice of the previous element but less than or equal to m".
# This means x_1, x_2, ..., x_n such that x_i \in [1, m] and x_i \ge 2*x_{i-1}.
# Wait! If x_i \ge 2*x_{i-1}, then x_1 \ge 1, x_2 \ge 2, x_3 \ge 4, x_4 \ge 8...
# If n=3, m=4, sequences are: (1, 2, 4). (Total 1)
# If n=2, m=4, sequences are: (1, 2), (1, 3), (1, 4), (2, 4). (Total 4)
# If n=1, m=4, sequences are: (1), (2), (3), (4). (Total 4)
# Look at the assertions: (10, 4) -> 4, (5, 2) -> 6, (16, 3) -> 84.
# These values of n are much larger than the m values.
# This suggests n is the maximum value and m is the length.
# Let's check (m=10, n=4) with x_i \ge 2*x_{i-1}:
# x_1 \ge 1, x_2 \ge 2, x_3 \ge 4, x_4 \ge 8.
# x_4 can be 8, 9, 10 (3 options).
# x_3 can be 4. If x_3=4, x_4 can be 8,9,10.
# x_2 can be 2. If x_2=2, x_3 can be 4.
# x_1 can be 1. If x_1=1, x_2 can be 2.
# This is not 4.
# Let's try the other way: m is the max value, n is the length.
# If the condition is x_i \le 2 * x_{i-1} AND x_i \ge x_{i-1}? 
# No, let's look at (16, 3) -> 84.
# If n is the length and m is the max