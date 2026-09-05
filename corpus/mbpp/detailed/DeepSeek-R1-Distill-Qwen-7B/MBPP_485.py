def largest_palindrome(arr):
    # Helper function to check if a number is a palindrome
    def is_palindrome(n):
        s = str(n)
        return s == s[::-1]

    # Initialize the largest palindrome to the smallest possible value
    largest = -1  # Start with -1 to handle all negative cases

    for num in arr:
        # Check if the current number is a palindrome
        if is_palindrome(num):
            # If it's larger than the current largest, update it
            if num > largest:
                largest = num

    # If no palindrome was found and all elements are negative, return -1
    if largest == -1:
        return -1

    return largest