def max_subarray_product(arr):
    if not arr:
        return 0

    max_product = min_product = max_result = arr[0]

    for num in arr[1:]:
        temp = max_product
        max_product = max(num, max_product * num, min_product * num)
        min_product = min(num, temp * num, min_product * num)
        max_result = max(max_result, max_product)

    return max_result

assert max_subarray_product([1, -2, -3, 0, 7, -8, -2]) == 112
assert max_subarray_product([6, -3, -10, 0, 2]) == 180 
assert max_subarray_product([-2, -40, 0, -2, -3]) == 80