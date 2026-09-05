def first(arr, element, value):
    for i in range(len(arr)):
        if arr[i] == value:
            return i
    return -1