def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers"""
    if n < 8:
        return False
    return True

# Example usage:
# print(is_equal_to_sum_even(4))  # Output: False
# print(is_equal_to_sum_even(6))  # Output: False
# print(is_equal_to_sum_even(8))  # Output: True