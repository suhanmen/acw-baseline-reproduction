def frequency_Of_Smallest(arr):
    """
    Find the frequency of the smallest value in a given array.

    Steps:
    1. Validate Input: Check if the input is a non-empty list.
    2. Find the smallest value in the array.
    3. Count the frequency of this smallest value.
    4. Return the count.
    """
    # Validate input: Check if the input is a list
    if not isinstance(arr, list):
        raise ValueError("Input must be a list.")

    # Check if the list is empty
    if not arr:
        return 0

    # Find the smallest value in the array
    smallest_val = min(arr)

    # Count the frequency of the smallest value
    frequency = arr.count(smallest_val)

    return frequency