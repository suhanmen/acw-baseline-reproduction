def sum_pairs(arr):
    # Step 1: Validate the input
    if len(arr) < 2:
        return 0

    # Step 2: Sort the array to facilitate easier calculation
    sorted_arr = sorted(arr)
    n = len(sorted_arr)
    total = 0

    # Step 3: Calculate the sum of absolute differences
    for i in range(n):
        # Number of elements to the left of current element
        left_count = i
        # Number of elements to the right of current element
        right_count = n - 1 - i

        # Multiply the current element by the count of smaller elements
        total -= sorted_arr[i] * left_count

        # Multiply the current element by the count of larger elements
        total += sorted_arr[i] * right_count

    return total

# Test cases to verify the solution
def test_sum_pairs():
    assert sum_pairs([1,8,9,15,16]) == 74, "Test case 1 failed"
    assert sum_pairs([1,2,3,4]) == 10, "Test case 2 failed"
    assert sum_pairs([1,2,3,4,5,7,9,11,14]) == 188, "Test case 3 failed"
    print("All test cases passed")

test_sum_pairs()