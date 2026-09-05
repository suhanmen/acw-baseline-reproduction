def largest_palindrome(arr, n):
    def is_palindrome(x):
        s = str(x)
        return s == s[::-1]

    max_pal = 0
    for num in arr:
        if is_palindrome(num):
            if num > max_pal:
                max_pal = num
    return max_pal