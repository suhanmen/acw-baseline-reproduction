def find_remainder(arr, k, n):
    result = 1
    for num in arr:
        result = (result * num % n) % k
    return result