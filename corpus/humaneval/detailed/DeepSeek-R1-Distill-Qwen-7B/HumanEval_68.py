def pluck(arr):
    """
    Given an array representing a branch of a tree that has non-negative integer nodes,
    this function plucks one of the nodes and returns it.
    The plucked node should be the node with the smallest even value.
    If multiple nodes with the same smallest even value are found, return the node with the smallest index.

    The result is returned as a list [smallest_value, its_index].
    If there are no even values or the array is empty, return an empty list.

    Parameters:
    arr (list): The input list of non-negative integers.

    Returns:
    list: A list containing the smallest even value and its index, or an empty list if no even values exist or the array is empty.
    """
    # Initialize variables to keep track of the smallest even value and its index
    smallest_even = None
    smallest_index = -1

    # Iterate through each element in the array along with its index
    for index, value in enumerate(arr):
        # Check if the current value is even
        if value % 2 == 0:
            # If it's the first even value encountered, initialize the variables
            if smallest_even is None:
                smallest_even = value
                smallest_index = index
            else:
                # Compare with the current smallest even value
                if value < smallest_even:
                    smallest_even = value
                    smallest_index = index
                elif value == smallest_even:
                    # If the current value is equal, choose the one with the smaller index
                    if index < smallest_index:
                        smallest_index = index

    # Return the result based on whether we found any even value
    if smallest_even is not None:
        return [smallest_even, smallest_index]
    else:
        return []