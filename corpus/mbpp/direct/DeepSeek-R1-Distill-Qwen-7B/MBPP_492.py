def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        current = arr[mid]

        if current == target:
            return True
        elif current < target:
            left = mid + 1
        else:
            right = mid - 1

    return False

# Test cases
assert binary_search([1,2,3,5,8], 6) == False, "Test case 1 failed"
assert binary_search([7, 8, 9, 10, 13], 10) == True, "Test case 2 failed"
assert binary_search([11, 13, 14, 19, 22, 36], 23) == False, "Test case 3 failed"