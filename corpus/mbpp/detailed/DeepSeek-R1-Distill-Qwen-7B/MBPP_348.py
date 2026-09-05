from functools import lru_cache

def find_ways(n):
    if n == 0:
        return 0
    if n == 1:
        return 3  # [0], [1], [-1] but only [0] and [1] have non-negative prefix sums.

    @lru_cache(maxsize=None)
    def count_sequences(current_pos, current_sum, min_sum):
        if current_pos == n:
            return 1
        if current_sum < 0:
            return 0
        total = 0
        for next_val in (-1, 0, 1):
            new_sum = current_sum + next_val
            new_min_sum = min(min_sum, new_sum)
            total += count_sequences(current_pos + 1, new_sum, new_min_sum)
        return total

    return count_sequences(0, 0, 0)