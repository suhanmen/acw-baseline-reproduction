def next_smallest_palindrome(n):
    n += 1
    while True:
        s = str(n)
        if s == s[::-1]:
            return n
        n += 1