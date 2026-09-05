def pancake_sort(arr):
    def flip(sublist, k):
        sublist[:k+1] = sublist[:k+1][::-1]

    n = len(arr)
    for current_size in range(n, 1, -1):
        max_idx = 0
        for i in range(1, current_size):
            if arr[i] > arr[max_idx]:
                max_idx = i

        if max_idx != current_size - 1:
            if max_idx != 0:
                flip(arr, max_idx)
            flip(arr, current_size - 1)

    return arr