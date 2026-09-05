def count_X(t, x):
    count = 0
    for element in t:
        if element == x:
            count += 1
    return count

# Test the function with the provided examples
print(count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2), 4))  # Output: 0
print(count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2), 10))  # Output: 3
print(count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2), 8))  # Output: 4