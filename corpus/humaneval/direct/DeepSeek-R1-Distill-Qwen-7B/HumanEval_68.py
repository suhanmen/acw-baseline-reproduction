def pluck(arr):
    """
    Given an array representing a branch of a tree that has non-negative integer nodes,
    this function returns the smallest even value and its index. If no even values are found,
    it returns an empty list.

    The output is a list [smallest_value, its_index].
    """
    # Filter out the even values along with their indices
    even_values = [(value, index) for index, value in enumerate(arr) if value % 2 == 0]

    if not even_values:
        return []

    # Sort the even values to find the smallest one and its smallest index
    # Sorting by value first, then by index ensures we get the smallest value first,
    # and in case of ties, the smallest index is chosen.
    even_values.sort(key=lambda x: (x[0], x[1]))

    return [even_values[0][0], even_values[0][1]]