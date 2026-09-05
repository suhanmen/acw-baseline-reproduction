def re_arrange_array(arr):
    neg_ptr = 0
    pos_ptr = len(arr) - 1

    while neg_ptr < pos_ptr:
        if arr[neg_ptr] > 0:
            neg_ptr += 1
        if arr[pos_ptr] < 0:
            pos_ptr -= 1
        if arr[neg_ptr] < 0 and arr[pos_ptr] > 0:
            arr[neg_ptr], arr[pos_ptr] = arr[pos_ptr], arr[neg_ptr]

    return arr

# Example usage:
print(re_arrange_array([-1, 2, -3, 4, 5, 6, -7, 8, 9], 9))  # Output: [-1, -3, -7, 4, 5, 6, 2, 8, 9]
print(re_arrange_array([12, -14, -26, 13, 15], 5))          # Output: [-14, -26, 12, 13, 15]
print(re_arrange_array([10, 24, 36, -42, -39, -78, 85], 7))# Output: [-42, -39, -78, 10, 24, 36, 85]