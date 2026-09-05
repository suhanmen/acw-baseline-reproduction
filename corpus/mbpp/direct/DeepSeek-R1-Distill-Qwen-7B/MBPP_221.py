def first_even(numbers):
    for num in numbers:
        if num % 2 == 0:
            return num
    return None  # This line is theoretically unreachable given the problem constraints