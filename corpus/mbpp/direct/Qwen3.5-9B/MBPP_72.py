def dif_Square(n):
    if n <= 0:
        return False
    # A positive integer n can be represented as difference of two squares iff n is odd or divisible by 4
    return n % 2 != 0 or n % 4 == 0