def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    '''

    # Validate input type: ensure the input is a list
    if not isinstance(lst, list):
        raise TypeError("Input must be a list of integers.")

    # Validate input content: ensure all elements are integers
    for index, element in enumerate(lst):
        if not isinstance(element, int):
            raise TypeError(f"All elements in the list must be integers. Found element at index {index} of type {type(element).__name__}.")

    # Handle the empty list case explicitly
    if len(lst) == 0:
        return []

    # Handle the single element case explicitly
    if len(lst) == 1:
        return lst.copy()

    # Create a sorted copy of the original list to serve as our pool of available numbers
    sorted_numbers = sorted(lst)

    # Prepare the result list to hold the strangely sorted integers
    result = []

    # Create a copy of the sorted numbers to track which ones have been used
    # We will slice this list to remove used elements as we progress
    available_numbers = sorted_numbers.copy()

    # Define a flag to alternate between picking the minimum and the maximum
    pick_minimum = True

    # Iterate until there are no more numbers available in our pool
    while len(available_numbers) > 0:
        if pick_minimum:
            # Pick the minimum value from the current available numbers
            # Since available_numbers is kept sorted, the minimum is always at index 0
            current_value = available_numbers[0]

            # Remove the minimum value from the available numbers
            available_numbers.pop(0)

        else:
            # Pick the maximum value from the current available numbers
            # Since available_numbers is kept sorted, the maximum is always at the last index
            current_value = available_numbers[-1]

            # Remove the maximum value from the available numbers
            available_numbers.pop(-1)

        # Append the selected value to the result list
        result.append(current_value)

        # Toggle the flag for the next iteration
        pick_minimum = not pick_minimum

    return result