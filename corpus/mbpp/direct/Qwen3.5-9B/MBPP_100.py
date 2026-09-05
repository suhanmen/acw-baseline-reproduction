def next_smallest_palindrome(n: int) -> int:
    """
    Finds the next smallest palindrome strictly greater than n.
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer")

    # Helper to check if a number is a palindrome
    def is_palindrome(num: int) -> bool:
        s = str(num)
        return s == s[::-1]

    candidate = n + 1
    while not is_palindrome(candidate):
        candidate += 1
    return candidate