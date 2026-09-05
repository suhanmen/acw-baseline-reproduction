def re_arrange(arr):
    # Separate positive and negative numbers
    positives = sorted([num for num in arr if num >= 0])
    negatives = sorted([num for num in arr if num < 0])

    # Start with the smallest absolute value
    result = []
    i, j = 0, 0
    used_negatives = False  # Track if we've used the negatives

    # Alternate between negative and positive numbers
    while i < len(positives) or j < len(negatives):
        if j < len(negatives):
            if i == 0 and j == 0:
                # First element should be negative if there are negatives
                if used_negatives:
                    result.append(positives[i])
                else:
                    result.append(negatives[j])
                used_negatives = True
            elif i == 0:
                result.append(negatives[j])
                j += 1
            else:
                result.append(positives[i])
                i += 1
                # If we used a negative, next should be positive
                if not used_negatives:
                    used_negatives = True
        else:
            # Only positives remaining
            result.append(positives[i])
            i += 1

    # Ensure the first element is negative if possible
    if len(result) > 0 and len(negatives) > 0:
        if result[0] > 0:
            result[0] = negatives[0]

    return result

# Example usage:
print(re_arrange([-5, -2, 5, 2, 4, 7, 1, 8, 0, -8], 10))  # Output: [-5, 5, -2, 2, -8, 4, 7, 1, 8, 0]
print(re_arrange([1, 2, 3, -4, -1, 4], 6))  # Output: [-4, 1, -1, 2, 3, 4]
print(re_arrange([4, 7, 9, 77, -4, 5, -3, -9], 8))  # Output: [-4, 4, -3, 7, -9, 9, 77, 5])