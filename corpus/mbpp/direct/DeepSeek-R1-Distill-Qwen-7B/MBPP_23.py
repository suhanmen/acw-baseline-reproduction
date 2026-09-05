def maximum_Sum(lst):
    max_sum = -float('inf')
    for sublist in lst:
        current_sum = sum(sublist)
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum

# Test cases
assert maximum_Sum([[1,2,3],[4,5,6],[10,11,12],[7,8,9]]) == 33
assert maximum_Sum([[0,1,1],[1,1,2],[3,2,1]]) == 6
assert maximum_Sum([[0,1,3],[1,2,1],[9,8,2],[0,1,0],[6,4,8]]) == 19