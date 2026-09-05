def get_total_number_of_sequences(n, m):
    from functools import lru_cache

    def is_valid_input(n_val, m_val):
        if not isinstance(n_val, int) or not isinstance(m_val, int):
            return False
        if n_val < 1 or m_val < 0:
            return False
        return True

    if not is_valid_input(n, m):
        return 0

    @lru_cache(maxsize=None)
    def count_sequences(n, m, prev):
        if n == 1:
            return 1 if prev <= m else 0
        total = 0
        min_next = 2 * prev
        max_next = m
        if min_next > max_next:
            return 0
        for next_val in range(min_next, max_next + 1):
            total += count_sequences(n - 1, m, next_val)
        return total

    return count_sequences(n, m, 1)