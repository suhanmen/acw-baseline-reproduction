def position_max(lst):
    max_value = max(lst)
    max_indices = [i for i, val in enumerate(lst) if val == max_value]
    return max_indices

# Example usage:
print(position_max([12,33,23,10,67,89,45,667,23,12,11,10,54]))  # Output: [7]
print(position_max([1,2,2,2,4,4,4,5,5,5,5]))  # Output: [7,8,9,10]
print(position_max([2,1,5,6,8,3,4,9,10,11,8,12]))  # Output: [11]