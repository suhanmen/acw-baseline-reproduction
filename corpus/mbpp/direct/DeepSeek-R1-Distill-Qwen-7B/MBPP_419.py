def round_and_sum(numbers):
    rounded_numbers = [round(num) for num in numbers]
    total_sum = sum(rounded_numbers)
    return total_sum * len(numbers)