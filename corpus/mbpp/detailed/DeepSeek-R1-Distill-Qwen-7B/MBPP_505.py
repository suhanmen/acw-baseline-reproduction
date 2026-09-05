def re_order(arr):
    """
    Moves all zeroes to the end of the given array while maintaining the order of non-zero elements.
    Handles all edge cases, including empty arrays, single elements, arrays with all zeroes,
    and arrays with negative numbers.

    Args:
        arr: The input list of integers, which may contain zeroes.

    Returns:
        A new list with all zeroes moved to the end.

    Raises:
        TypeError: If the input is not a list.
    """
    # Check if the input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")

    # Split the array into non-zero elements and zero elements
    non_zero = []
    zero_count = 0
    for num in arr:
        if num == 0:
            zero_count += 1
        else:
            non_zero.append(num)

    # Combine non-zero elements with zero elements at the end
    result = non_zero + [0] * zero_count

    # Handle the case where the input array is empty
    if not arr:
        return result

    return result