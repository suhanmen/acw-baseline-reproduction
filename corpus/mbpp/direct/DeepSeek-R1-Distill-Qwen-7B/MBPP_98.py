def multiply_num(numbers):
    import math
    product = 1
    for num in numbers:
        product *= num
    return product / len(numbers)