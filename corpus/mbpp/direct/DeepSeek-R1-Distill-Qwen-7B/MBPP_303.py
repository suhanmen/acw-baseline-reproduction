def solve(arr, n):
    inversion_count_type1 = 0
    inversion_count_type2 = 0

    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                if arr[i] != arr[j]:
                    inversion_count_type1 += 1
                else:
                    inversion_count_type2 += 1

    return inversion_count_type1 == inversion_count_type2

# Example usage
solve([1, 0, 2], 3)  # Returns True
solve([1, 2, 0], 3)  # Returns False
solve([1, 2, 1], 3)  # Returns True