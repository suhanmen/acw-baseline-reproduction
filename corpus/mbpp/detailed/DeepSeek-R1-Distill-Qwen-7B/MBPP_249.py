def intersection_array(arr1, arr2):
    if not arr1 or not arr2:
        return []

    set1 = set(arr1)
    set2 = set(arr2)

    common_elements = set1.intersection(set2)

    return sorted(common_elements)

# Example usage:
# print(intersection_array([1, 2, 3, 5, 7, 8, 9, 10], [1, 2, 4, 8, 9]))  # Output: [1, 2, 8, 9]
# print(intersection_array([1, 2, 3, 5, 7, 8, 9, 10], [3, 5, 7, 9]))  # Output: [3, 5, 7, 9]
# print(intersection_array([1, 2, 3, 5, 7, 8, 9, 10], [10, 20, 30, 40]))  # Output: [10]