import math

def dif_Square(n):
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            j = n // i
            if (i + j) % 2 == 0:
                return True
    return False