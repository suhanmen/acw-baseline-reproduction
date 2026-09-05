def sequential_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return (True, index)
    return (False, -1)