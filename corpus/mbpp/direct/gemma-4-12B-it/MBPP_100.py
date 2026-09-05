def next_smallest_palindrome(n: int) -> int:
    """
    Finds the next smallest palindrome greater than the given integer n.
    """
    def is_palindrome(num: int) -> bool:
        s = str(num)
        return s == s[::-1]

    # Start searching from the integer immediately following n
    current = n + 1
    while True:
        if is_palindrome(current):
            return current
        current += 1

# Assertions to verify the solution
if __name__ == "__main__":
    assert next_smallest_palindrome(99) == 101
    assert next_smallest_palindrome(1221) == 1331
    assert next_smallest_palindrome(120) == 121