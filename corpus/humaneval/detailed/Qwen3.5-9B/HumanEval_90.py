def next_smallest(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.

    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    """

    # Validate input type
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")

    # Validate input elements
    for item in lst:
        if not isinstance(item, int):
            raise TypeError("All elements must be integers")

    # Check if list has fewer than 2 elements
    if len(lst) < 2:
        return None

    # Check if all elements are equal
    if len(set(lst)) < 2:
        return None

    # Helper function to find the smallest number
    def find_smallest(numbers):
        current_min = numbers[0]
        for i in range(1, len(numbers)):
            if numbers[i] < current_min:
                current_min = numbers[i]
        return current_min

    # Helper function to find the second smallest number
    def find_second_smallest(numbers, smallest):
        second_smallest = float('inf')
        for i in range(len(numbers)):
            if numbers[i] != smallest and numbers[i] < second_smallest:
                second_smallest = numbers[i]
        return second_smallest

    # Get the smallest number
    smallest_value = find_smallest(lst)

    # Get the second smallest number
    second_smallest_value = find_second_smallest(lst, smallest_value)

    return second_smallest_value