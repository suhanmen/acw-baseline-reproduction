import math

def does_Contain_B(a, b, c):
    def is_triangular(num):
        if num == 0:
            return True
        discriminant = 1 + 8 * num
        sqrt_discriminant = math.sqrt(discriminant)
        if sqrt_discriminant % 1 != 0:
            return False
        sqrt_discriminant = int(sqrt_discriminant)
        n1 = (-1 + sqrt_discriminant) / 2
        n2 = (-1 - sqrt_discriminant) / 2
        return (n1.is_integer() or n2.is_integer())

    return is_triangular(b)