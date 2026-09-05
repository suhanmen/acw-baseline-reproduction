def breakSum(n):
    # Base cases
    if n <= 0:
        return n
    if 1 <= n <= 9:
        return n
    if n == 10:
        return 10

    # Recursive case
    max_sum = 0
    for i in range(1, n - 1):
        for j in range(i + 1, n - i + 1):
            k = n - i - j
            current_sum = i + j + k
            if current_sum > max_sum:
                max_sum = current_sum

    return max_sum

# Test the function with provided assertions
print("breakSum(12) =", breakSum(12))  # Expected output: 13
print("breakSum(24) =", breakSum(24))  # Expected output: 27
print("breakSum(23) =", breakSum(23))  # Expected output: 23