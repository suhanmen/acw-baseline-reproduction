def is_Monotonic(arr):
    increasing = True
    decreasing = True
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            increasing = False
        elif arr[i] < arr[i + 1]:
            decreasing = False
        # If both increasing and decreasing flags are False, can break early
        if not increasing and not decreasing:
            break
    return increasing or decreasing