def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    count = 0
    for num in nums:
        if num > 10:
            s = str(abs(num))  # Handle negative numbers by taking absolute value
            if len(s) == 1:
                continue  # Since we've already checked num >10, this won't be triggered
            first_digit = s[0]
            last_digit = s[-1]
            if first_digit in {'1', '3', '5', '7', '9'} and last_digit in {'1', '3', '5', '7', '9'}:
                count += 1
    return count