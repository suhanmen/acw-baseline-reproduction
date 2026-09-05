def count_no_of_ways(n: int, k: int) -> int:
    """
    Calculates the number of ways to paint a fence with n posts using k colors
    such that at most 2 adjacent posts have the same color.

    This means:
    - We can have one post with the same color as the previous (e.g., Red, Red).
    - We CANNOT have two consecutive posts with the same color as the previous 
      (e.g., Red, Red, Red is invalid).

    The problem states "at most 2 adjacent posts have the same color".
    This implies we cannot have a sequence of 3 or more posts with the same color.
    So, a pattern like [Color1, Color1, Color1] is forbidden, but 
    [Color1, Color1, Color2] is allowed.

    We validate inputs first.
    If n is less than 1, there are no posts to paint, so the answer is 0.
    If k is less than 1, there are no colors available, so the answer is 0.

    We use dynamic programming to solve this efficiently.
    Let dp[i] be the total number of valid ways to paint the first i posts.

    We need to track two states for the i-th post:
    1. ways_same[i]: Number of valid ways where the i-th post has the SAME color as the (i-1)-th post.
       Since we cannot have 3 same colors in a row, this is only possible if the (i-1)-th post 
       did NOT have the same color as the (i-2)-th post.

    2. ways_diff[i]: Number of valid ways where the i-th post has a DIFFERENT color than the (i-1)-th post.

    Base case for n = 1:
    - We have 1 post.
    - ways_same[1] = 0 (cannot have a "same" relation with a non-existent previous post).
    - ways_diff[1] = k (any of the k colors).
    - Total ways for n=1 = k.

    For n = 2:
    - ways_same[2]: The 2nd post is same as 1st. 
        We can pick any of the k colors for the 1st post. Then we MUST pick the same color for the 2nd.
        So, there are k ways.
        Alternatively: ways_same[2] = ways_diff[1] * 1 (only 1 choice to match previous) 
        But wait, the logic needs to be consistent.

    Let's refine the DP state transition:

    Let 'same' represent the count of ways where the current post matches the previous post.
    Let 'diff' represent the count of ways where the current post differs from the previous post.

    For the first post (i=1):
    same = 0
    diff = k

    For the second post (i=2):
    - To get a 'same' at i=2: The previous post (i=1) could be anything (valid). 
      We have k choices for post 1. Then 1 choice (same) for post 2.
      However, our state 'same' at i-1 implies post (i-1) == post (i-2).
      If we try to make post i == post (i-1) when post (i-1) == post (i-2), we create 3 same in a row. Forbidden.
      So, we can only transition from 'diff' at i-1 to 'same' at i.
      Why? If post (i-1) was different from (i-2), then post i being same as (i-1) results in only 2 consecutive same colors. Allowed.
      Number of ways = diff * 1.

    - To get a 'diff' at i=2: The previous post (i-1) could be anything (valid).
      We have (same + diff) total ways for i-1.
      For each valid configuration of i-1, we have (k - 1) choices for post i (any color except post i-1's color).
      Number of ways = (same + diff) * (k - 1).

    General recurrence for i > 1:
    current_same = prev_diff * 1
    current_diff = (prev_same + prev_diff) * (k - 1)

    Let's trace with examples.

    Example 1: n=2, k=4
    i=1: same=0, diff=4. Total=4.
    i=2: 
        same = 4 * 1 = 4.
        diff = (0 + 4) * (4-1) = 4 * 3 = 12.
        Total = 4 + 12 = 16.
    Matches assertion: assert count_no_of_ways(2, 4) == 16.

    Example 2: n=3, k=2
    i=1: same=0, diff=2. Total=2.
    i=2:
        same = 2 * 1 = 2.
        diff = (0 + 2) * (2-1) = 2 * 1 = 2.
        Total = 4.
    i=3:
        same = 2 * 1 = 2. (Must come from diff at i=2)
        diff = (2 + 2) * (2-1) = 4 * 1 = 4.
        Total = 2 + 4 = 6.
    Matches assertion: assert count_no_of_ways(3, 2) == 6.

    Example 3: n=4, k=4
    i=1: same=0, diff=4. Total=4.
    i=2: same=4, diff=12. Total=16.
    i=3:
        same = 12 * 1 = 12.
        diff = (4 + 12) * 3 = 16 * 3 = 48.
        Total = 60.
    i=4:
        same = 48 * 1 = 48.
        diff = (12 + 48) * 3 = 60 * 3 = 180.
        Total = 48 + 180 = 228.
    Matches assertion: assert count_no_of_ways(4, 4) == 228.

    Implementation steps:
    1. Validate n and k.
    2. Handle base case n=1.
    3. Initialize variables for i=1.
    4. Iterate from 2 to n, updating same and diff.
    5. Return sum of same and diff.
    """

    # Input validation
    if not isinstance(n, int) or not isinstance(k, int):
        raise TypeError("Both n and k must be integers.")

    if n < 1:
        return 0

    if k < 1:
        return 0

    # Base case: n = 1
    if n == 1:
        return k

    # Variables for the previous iteration (initially for post 1)
    # same: number of ways where current post matches the previous one.
    # For the first post, there is no previous post, so this is 0.
    prev_same = 0
    # diff: number of ways where current post differs from the previous one.
    # For the first post, any of the k colors is valid.
    prev_diff = k

    # Iterate from the second post up to the nth post
    current_post_index = 1  # This loop represents computing for post 2, 3, ..., n

    while current_post_index < n:
        # Calculate next_same:
        # We can only have the current post match the previous one if the previous post
        # did NOT match the one before that. This prevents 3 consecutive same colors.
        # So, next_same = prev_diff * 1 (only 1 choice: same as prev)
        next_same = prev_diff

        # Calculate next_diff:
        # We can have the current post differ from the previous one if the previous state
        # was valid (either same or diff).
        # For each valid configuration of the previous post, we have (k - 1) choices.
        next_diff = (prev_same + prev_diff) * (k - 1)

        # Update previous variables for the next iteration
        prev_same = next_same
        prev_diff = next_diff

        # Move to the next post index
        current_post_index += 1

    # The result is the sum of ways ending in same and ways ending in different
    total_ways = prev_same + prev_diff

    return total_ways