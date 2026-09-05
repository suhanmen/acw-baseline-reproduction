def check_triplet(arr, sum1, sum2, sum3):
    # Validate input: ensure all sums are distinct
    if sum1 == sum2 or sum2 == sum3 or sum1 == sum3:
        return False

    # Edge case: array must have at least three elements
    if len(arr) < 3:
        return False

    # Generate all possible triplets and check their sum
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            for k in range(j + 1, len(arr)):
                if arr[i] + arr[j] + arr[k] == sum1:
                    return True
                if arr[i] + arr[j] + arr[k] == sum2:
                    return True
                if arr[i] + arr[j] + arr[k] == sum3:
                    return True

    return False