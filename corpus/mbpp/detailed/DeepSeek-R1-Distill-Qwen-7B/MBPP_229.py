def re_arrange_array(arr):
    # Split the array into negatives and positives
    negatives = []
    positives = []

    # Iterate through each element
    for num in arr:
        if num < 0:
            negatives.append(num)
        else:
            positives.append(num)

    # Concatenate negatives and positives
    result = negatives + positives

    # Return the result
    return result

# Test cases
print(re_arrange_array([-1, 2, -3, 4, 5, 6, -7, 8, 9]))
print(re_arrange_array([12, -14, -26, 13, 15]))
print(re_arrange_array([10, 24, 36, -42, -39, -78, 85]))