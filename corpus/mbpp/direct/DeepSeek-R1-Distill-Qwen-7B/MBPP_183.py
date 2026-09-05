def count_pairs(arr, k, desired_diff):
    # Sort the array to make it easier to find pairs
    sorted_arr = sorted(arr)
    n = len(sorted_arr)
    count = 0

    # Use two pointers to find all distinct pairs with the desired difference
    for i in range(n):
        if i >= n:
            break  # Prevents duplicate checking
        current = sorted_arr[i]
        # Find the smallest j such that sorted_arr[j] - current == desired_diff
        left = i + 1
        right = n - 1
        while left < right:
            diff = sorted_arr[right] - current
            if diff == desired_diff:
                count += 1
                # Move left pointer to find next potential pair
                left += 1
            elif diff < desired_diff:
                # Need a larger number, move right pointer
                left += 1
            else:
                # Need a smaller number, move left pointer
                right -= 1
    return count

# Verify the correctness of the function
assert count_pairs([1, 5, 3, 4, 2], 5, 3) == 2
assert count_pairs([8, 12, 16, 4, 0, 20], 6, 4) == 5
assert count_pairs([2, 4, 1, 3, 4], 5, 2) == 3