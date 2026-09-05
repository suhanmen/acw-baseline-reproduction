def first(arr, element, default=None):
    """
    Find the first position of an element in a sorted array.

    Args:
        arr: The sorted array to search.
        element: The element to find in the array.
        default: The value to return if the element is not found. Defaults to None.

    Returns:
        The index of the first occurrence of the element, or the default value if not found.

    Raises:
        TypeError: If the array is not an instance of list or the element is not comparable.
    """
    # Validate inputs
    if not isinstance(arr, list):
        raise TypeError("The first argument must be a list.")

    # Handle the case where the array is empty
    if not arr:
        return default

    # Initialize the index variable
    index = 0

    # Iterate through the array to find the first occurrence of the element
    for i in range(len(arr)):
        if arr[i] == element:
            return i  # Return the first occurrence index
        elif arr[i] > element:
            # If any element is greater than the target, check if all subsequent elements are greater
            if all(a > element for a in arr[i:]):
                return default
            else:
                # Continue searching in the left part of the array
                index = i
    # If loop completes without returning, return the default value
    return default