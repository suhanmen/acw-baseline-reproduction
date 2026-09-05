def diff_consecutivenums(lst):
    """
    Calculate the difference between each pair of consecutive numbers in a given list.

    Parameters:
    lst (list): A list of numbers.

    Returns:
    list: A list containing the differences between consecutive elements.
    """
    # Handle edge case: empty list or single-element list
    if len(lst) < 2:
        return []

    # Initialize the result list
    differences = []

    # Helper function to calculate the difference between two consecutive numbers
    def calculate_difference(a, b):
        return b - a

    # Iterate through the list, starting from the second element
    for i in range(1, len(lst)):
        diff = calculate_difference(lst[i-1], lst[i])
        differences.append(diff)

    return differences

# Test cases
print(diff_consecutivenums([1, 1, 3, 4, 4, 5, 6, 7]))  # Output: [0, 2, 1, 0, 1, 1, 1]
print(diff_consecutivenums([4, 5, 8, 9, 6, 10]))     # Output: [1, 3, 1, -3, 4])
print(diff_consecutivenums([0, 1, 2, 3, 4, 4, 4, 4, 5, 7]))  # Output: [1, 1, 1, 1, 0, 0, 0, 1, 2])