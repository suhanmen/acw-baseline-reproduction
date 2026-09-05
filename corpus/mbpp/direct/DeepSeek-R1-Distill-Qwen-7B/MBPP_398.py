def sum_of_digits(numbers):
    total = 0
    for number in numbers:
        for digit in str(abs(number)):
            total += int(digit)
    return total

# The solution code must be complete and runnable on its own. Please ensure that the code
# does not output anything besides the function. Do not add any additional print statements or
# return other values.