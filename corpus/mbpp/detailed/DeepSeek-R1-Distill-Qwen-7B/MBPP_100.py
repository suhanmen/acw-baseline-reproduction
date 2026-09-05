def next_smallest_palindrome(n):
    def is_palindrome(x):
        s = str(x)
        return s == s[::-1]

    if not isinstance(n, int) or n < 10:
        return None

    current = n + 1
    while True:
        if is_palindrome(current):
            return current
        current += 1

# Example usage:
print(next_smallest_palindrome(99))   # Output: 101
print(next_smallest_palindrome(1221)) # Output: 1331
print(next_smallest_palindrome(120))  # Output: 121