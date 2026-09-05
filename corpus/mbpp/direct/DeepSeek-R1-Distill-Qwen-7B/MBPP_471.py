def find_remainder(arr, m, n):
    product = 1
    for num in arr:
        product *= num
        if product % n == 0:
            return 0
    return product % n