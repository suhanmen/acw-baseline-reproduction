def find_Sum(arr):
    # Count the frequency of each element
    frequency = {}
    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    # Calculate the sum of elements that appear more than once
    total = 0
    for num, count in frequency.items():
        if count > 1:
            total += num * (count - 1)
    return total

# Test the function with the provided assertions
assert find_Sum([1,2,3,1,1,4,5,6],8) == 3, "Test case 1 failed"
assert find_Sum([1,2,3,1,1],5) == 3, "Test case 2 failed"
assert find_Sum([1,1,2],3) == 2, "Test case 3 failed"

# If no assertions failed, the function works correctly
print("All test cases passed!")