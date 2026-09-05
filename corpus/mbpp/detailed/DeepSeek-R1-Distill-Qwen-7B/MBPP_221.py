def first_even(numbers):
    is_even_found = False
    for num in numbers:
        if num % 2 == 0:
            if not is_even_found:
                return num
            else:
                continue
    return None