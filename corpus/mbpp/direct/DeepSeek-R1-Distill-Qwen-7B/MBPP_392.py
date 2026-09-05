from functools import lru_cache

@lru_cache(maxsize=None)
def max_sum(n):
    if n <= 1:
        return n
    return max(n, max_sum(n // 2) + max_sum(n // 3) + max_sum(n // 4) + max_sum(n // 5))

# Example usage:
print(max_sum(60))  # Output: 106
print(max_sum(10))  # Output: 12
print(max_sum(2))   # Output: 2