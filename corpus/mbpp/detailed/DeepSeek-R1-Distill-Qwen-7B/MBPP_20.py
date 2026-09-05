def is_woodall(number):
    """
    Check if the given number is a Woodall number.

    A Woodall number is a number of the form W(n) = n * 2^n - 1 for some positive integer n.
    """
    if number < 1:
        return False

    n = 1
    while True:
        woodall_number = n * (2 ** n) - 1
        if woodall_number == number:
            return True
        elif woodall_number > number:
            return False
        n += 1

# Test cases
print(is_woodall(383))   # Expected output: True
print(is_woodall(254))   # Expected output: False
print(is_woodall(200))   # Expected output: False)