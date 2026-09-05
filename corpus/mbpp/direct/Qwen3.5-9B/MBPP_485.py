def largest_palindrome(arr: list, length: int) -> int:
    """
    Finds the largest palindromic number in the given array.
    The function ignores the 'length' parameter as it appears to be unused
    based on the problem's assertions and description.

    Args:
        arr (list): List of integers.
        length (int): An unused parameter from the problem statement.

    Returns:
        int: The largest palindrome found in the list.

    Raises:
        ValueError: If the array is empty.
        ValueError: If no palindrome is found in the array.
    """
    if not arr:
        raise ValueError("The input array must not be empty.")

    def is_palindrome(num):
        s = str(num)
        return s == s[::-1]

    palindromes = [num for num in arr if is_palindrome(num)]

    if not palindromes:
        raise ValueError("No palindromic number found in the array.")

    return max(palindromes)