def find_rotation_count(arr):
    """
    Finds the number of rotations in a circularly sorted array.

    A circularly sorted array is one where the array can be rotated some number
    of times to become sorted in ascending order. The number of rotations is
    determined by the index of the point where the next element is smaller than
    the current element.

    Args:
        arr (list): The circularly sorted array to be analyzed.

    Returns:
        int: The number of rotations needed to sort the array.

    Raises:
        ValueError: If the input is not a valid circularly sorted array.
    """
    # Handle empty array case
    if not arr:
        return 0

    # Handle single element or all elements equal
    if len(arr) <= 1 or all(x == arr[0] for x in arr):
        return 0

    rotation_point = -1

    # Iterate through the array to find the rotation point
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            rotation_point = i
            break

    # Check if the array is indeed rotated
    if rotation_point == -1:
        # No rotation point found, array is already sorted
        return 0
    else:
        # Ensure that the next element is smaller than the first element
        if arr[-1] <= arr[0]:
            # Calculate the number of rotations
            return rotation_point + 1
        else:
            # The array is not circularly sorted, raise an error
            raise ValueError("The array is not a circularly sorted array.")