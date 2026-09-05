def is_subset_sum(arr, target_sum, window_size):
    if target_sum == 0:
        return True
    current_sum = sum(arr[:window_size])
    if current_sum == target_sum:
        return True
    for i in range(len(arr) - window_size + 1):
        if i > 0:
            current_sum -= arr[i - 1]
            current_sum += arr[i + window_size - 1]
        if current_sum == target_sum:
            return True
    return False