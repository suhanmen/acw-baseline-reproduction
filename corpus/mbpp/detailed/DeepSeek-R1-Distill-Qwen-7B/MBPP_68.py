def is_Monotonic(arr):
    # Handle edge cases
    if len(arr) <= 1:
        return True
    if all_equal(arr):
        return True

    # Determine the initial direction
    first = arr[0]
    second = arr[1]
    increasing = second >= first
    decreasing = second <= first

    if not (increasing or decreasing):
        return False

    if increasing:
        current_trend = 'up'
    else:
        current_trend = 'down'

    for i in range(2, len(arr)):
        current = arr[i]
        previous = arr[i-1]
        if current_trend == 'up':
            if current < previous:
                return False
        else:
            if current > previous:
                return False

    return True

def all_equal(arr):
    first = arr[0]
    for num in arr[1:]:
        if num != first:
            return False
    return True