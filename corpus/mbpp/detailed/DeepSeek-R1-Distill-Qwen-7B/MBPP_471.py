def find_remainder(arr, n):
    if not arr:
        return 0
    result = 1
    for num in arr:
        result = (result * (num % n)) % n
    return result