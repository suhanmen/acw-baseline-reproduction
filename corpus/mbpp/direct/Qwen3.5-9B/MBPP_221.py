def first_even(numbers):
    for num in numbers:
        if num % 2 == 0:
            return num
    raise ValueError("No even number found in the list.")