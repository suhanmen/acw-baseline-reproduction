def modular_inverse(arr, p):
    count = 0
    for a in arr:
        if a == 1 or a == p - 1:
            count += 1
    return count