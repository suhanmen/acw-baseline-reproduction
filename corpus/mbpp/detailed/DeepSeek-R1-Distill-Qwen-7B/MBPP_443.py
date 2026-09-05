def largest_neg(lst):
    # Helper function to check if a number is negative
    def is_negative(num):
        return num < 0

    # Filter the list to include only negative numbers
    negatives = [num for num in lst if is_negative(num)]

    # Check if there are no negative numbers
    if not negatives:
        return None

    # Find the largest (closest to zero) negative number
    largest = max(negatives)

    return largest

# Test cases
assert largest_neg([1, 2, 3, -4, -6]) == -4
assert largest_neg([1, 2, 3, -8, -9]) == -8
assert largest_neg([1, 2, 3, 4, -1]) == -1
assert largest_neg([-5, -2, -3]) == -2
assert largest_neg([-1]) == -1
assert largest_neg([-10, -20, -30]) == -10