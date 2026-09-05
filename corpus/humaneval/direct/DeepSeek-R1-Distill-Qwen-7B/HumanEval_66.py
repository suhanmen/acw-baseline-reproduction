def digitSum(s):
    """Task
    Write a function that takes a string as input and returns the sum of the upper characters only'
    ASCII codes.
    """
    total = 0
    for char in s:
        if char.isupper():
            total += ord(char)
    return total