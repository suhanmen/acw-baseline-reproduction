def round_and_sum(numbers):
    rounded_numbers = [round(num) for num in numbers]
    total_sum = sum(rounded_numbers)
    result = total_sum * len(numbers)
    print(result)
    return result