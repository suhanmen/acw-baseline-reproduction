def check(n):
    # Validate input
    if not isinstance(n, int) or n < 0:
        return False

    # Handle single-digit numbers
    if 0 <= n < 10:
        return 2 * n - 1 == n

    # Check if all digits are the same (e.g., 111)
    s = str(n)
    if all(c == s[0] for c in s):
        return 2 * int(s[::-1]) - 1 == int(s)

    # Check if the number has trailing zeros (e.g., 100)
    if s.endswith('0'):
        return False

    reversed_n = int(s[::-1])

    # Ensure reversed number has the same number of digits (no leading zeros)
    if len(str(reversed_n)) != len(s):
        return False

    return 2 * reversed_n - 1 == n

# Test the function with provided examples
assert check(70) == False, "70 should return False"
assert check(23) == False, "23 should return False"
assert check(73) == True, "73 should return True"