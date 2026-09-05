def pancake_sort(arr):
    n = len(arr)
    for i in range(n, 1, -1):
        j = 0
        for k in range(i, 0, -1):
            if arr[k] > arr[j]:
                arr[k], arr[j] = arr[j], arr[k]
                j += 1
    return arr

assert pancake_sort([15, 79, 25, 38, 69]) == [15, 25, 38, 69, 79], "First test failed"
assert pancake_sort([98, 12, 54, 36, 85]) == [12, 36, 54, 85, 98], "Second test failed"
assert pancake_sort([41, 42, 32, 12, 23]) == [12, 23, 32, 41, 42], "Third test failed"