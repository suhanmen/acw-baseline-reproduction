def pos_nos(lst):
    positive_numbers = []
    for number in lst:
        if number > 0:
            positive_numbers.append(number)
    return positive_numbers

# Test cases
assert pos_nos([-1, -2, 1, 2]) == [1, 2], "Test case 1 failed"
assert pos_nos([3, 4, -5]) == [3, 4], "Test case 2 failed"
assert pos_nos([-2, -3, 1]) == [1], "Test case 3 failed"

print("All test cases passed!")