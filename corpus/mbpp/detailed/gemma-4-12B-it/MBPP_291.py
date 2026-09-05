from typing import List

def count_no_of_ways(n: int, k: int) -> int:
    """
    Calculates the number of ways to paint a fence with n posts using k colors
    such that at most 2 adjacent posts have the same color.

    Logic:
    Let dp[i] be the number of ways to paint the fence up to the i-th post.
    For the i-th post, we have two scenarios to ensure no more than 2 adjacent posts
    have the same color:
    1. The i-th post is a different color than the (i-1)-th post.
       There are (k-1) choices for this color.
    2. The i-th post is the same color as the (i-1)-th post, but different
       from the (i-2)-th post.
       There are (k-1) choices for the (i-1)-th post relative to the (i-2)-th,
       and then the i-th post must match the (i-1)-th.

    More formally:
    Let same[i] be the number of ways where the i-th post is the same color as (i-1).
    Let diff[i] be the number of ways where the i-th post is a different color than (i-1).

    For post i:
    - diff[i] = (same[i-1] + diff[i-1]) * (k - 1)
    - same[i] = diff[i-1]

    Total ways for post i = same[i] + diff[i].
    """

    # --- Input Validation ---
    # Validate k (number of colors)
    if not isinstance(k, int) or k <= 0:
        raise ValueError("The number of colors k must be a positive integer.")

    # Validate n (number of posts)
    if not isinstance(n, int) or n < 0:
        raise ValueError("The number of posts n must be a non-negative integer.")

    # --- Edge Cases ---
    # 0 posts: There is 1 way to paint nothing (an empty fence).
    if n == 0:
        return 1

    # 1 post: There are k ways to paint one post.
    if n == 1:
        return k

    # 2 posts: 
    # - Ways where 2 posts are different: k * (k - 1)
    # - Ways where 2 posts are same: k
    # Total: k * (k - 1) + k = k * k
    if n == 2:
        return k * k

    # --- Dynamic Programming Approach ---
    # We only need the values from the previous step, so we use variables instead of a table.
    # Initial values for n = 2:
    # diff_prev: ways where the 2nd post is different from the 1st.
    # same_prev: ways where the 2nd post is the same as the 1st.

    diff_prev = k * (k - 1)
    same_prev = k

    # Iterate from the 3rd post to the n-th post.
    for i in range(3, n + 1):
        # Current diff:
        # The current post must be different from the previous post.
        # There are (k - 1) choices for the current post.
        # It doesn't matter if the previous post was the same as its predecessor 
        # or different; we just need current != previous.
        current_diff = (diff_prev + same_prev) * (k - 1)

        # Current same:
        # The current post must be the same as the previous post.
        # This is only allowed if the previous post was DIFFERENT from its predecessor.
        # If the previous post was already the same as its predecessor, 
        # making the current one the same would create 3 in a row.
        current_same = diff_prev

        # Update variables for the next iteration
        diff_prev = current_diff
        same_prev = current_same

    # The result for n posts is the sum of the two scenarios at the final step.
    total_ways = diff_prev + same_prev
    return total_ways