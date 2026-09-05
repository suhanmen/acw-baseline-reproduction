def even_odd_palindrome(n):
    """
    Given a positive integer n, return a tuple that has the number of even and odd
    integer palindromes that fall within the range(1, n), inclusive.
    """
    def is_palindrome(num):
        s = str(num)
        return s == s[::-1]

    even_count = 0
    odd_count = 0

    for num in range(1, n):
        if is_palindrome(num):
            if num % 2 == 0:
                even_count += 1
            else:
                odd_count += 1

    return (even_count, odd_count)