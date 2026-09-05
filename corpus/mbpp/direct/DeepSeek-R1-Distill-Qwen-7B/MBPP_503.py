def add_consecutive_nums(lst):
    result = []
    current_sum = 0
    for num in lst:
        current_sum += num
        # Check if we need to add to the result
        if current_sum in lst:
            result.append(current_sum)
            current_sum = 0  # Reset the sum for next potential consecutive numbers
    return result