def largest_palindrome(arr, n):
    """
    Finds the largest palindromic number in a given array.

    Args:
    arr (list): A list of integers.
    n (int): The size of the array.

    Returns:
    int: The largest palindromic number found, or None if no palindrome exists.
    """
    largest_palindrome_num = -1

    for num in arr:
        # Convert number to string to check for palindrome
        s = str(num)
        if s == s[::-1]:
            if num > largest_palindrome_num:
                largest_palindrome_num = num

    return largest_palindrome_num if largest_palindrome_num != -1 else None

if __name__ == "__main__":
    assert largest_palindrome([1, 232, 54545, 999991], 4) == 54545
    assert largest_palindrome([1, 2, 3, 4, 5, 50], 6) == 5
    assert largest_palindrome([1, 3, 7, 9, 45], 5) == 9