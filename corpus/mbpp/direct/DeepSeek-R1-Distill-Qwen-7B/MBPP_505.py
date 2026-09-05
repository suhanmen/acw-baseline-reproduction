def re_order(arr):
    nonZeroIndex = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[nonZeroIndex] = arr[i]
            nonZeroIndex += 1
    for _ in range(len(arr) - nonZeroIndex):
        arr[nonZeroIndex] = 0
    return arr