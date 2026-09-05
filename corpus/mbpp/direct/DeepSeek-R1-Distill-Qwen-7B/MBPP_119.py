def search(arr):
    unique = {}
    for num in arr:
        if num in unique:
            unique[num] += 1
        else:
            unique[num] = 1
    for key, value in unique.items():
        if value == 1:
            return key