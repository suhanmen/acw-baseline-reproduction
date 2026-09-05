def get_Position(arr, x, k):
    pos = []
    for i in range(len(arr)):
        if arr[i] == x:
            if k == 1:
                return i
            else:
                pos.append(i)
    if len(pos) == k:
        return pos[-1]
    else:
        return -1