def is_Monotonic(arr):
    if len(arr) <= 2:
        return True

    non_decreasing = True
    non_increasing = True

    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            non_decreasing = False
        if arr[i] > arr[i - 1]:
            non_increasing = False

        if not non_decreasing and not non_increasing:
            return False

    return True