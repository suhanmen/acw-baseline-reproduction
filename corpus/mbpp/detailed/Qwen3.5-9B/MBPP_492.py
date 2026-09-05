def binary_search(target: int, sorted_array: list[int]) -> bool:
    """
    Performs a binary search to determine if a target value exists in a sorted array.

    This function assumes the input array is sorted in ascending order.
    If the array is not sorted, the results are undefined.
    It handles edge cases such as empty arrays, single-element arrays,
    arrays with all equal elements, and negative numbers.

    Parameters:
    - target (int): The integer value to search for.
    - sorted_array (list[int]): A list of integers sorted in ascending order.

    Returns:
    - bool: True if the target is found in the array, False otherwise.
    """

    # Helper function to validate the input array
    def _validate_input(array_data: list) -> list:
        # Explicitly check for None
        if array_data is None:
            raise ValueError("The input array cannot be None.")

        # Explicitly check for non-list types
        if not isinstance(array_data, list):
            raise TypeError(f"Expected a list for the array, but got: {type(array_data).__name__}.")

        # Check if all elements are integers
        for i, element in enumerate(array_data):
            if not isinstance(element, int):
                raise TypeError(f"Expected all elements to be integers, but element at index {i} is: {type(element).__name__}.")

        # Check if the array is sorted in ascending order
        for i in range(len(array_data) - 1):
            if array_data[i] > array_data[i + 1]:
                raise ValueError("The input array must be sorted in ascending order.")

        return array_data

    # Validate the input before proceeding
    validated_list = _validate_input(sorted_array)

    # Initialize the search boundaries
    low_index = 0
    high_index = len(validated_list) - 1

    # Iterate while the search space is valid
    while low_index <= high_index:
        # Calculate the middle index explicitly
        # Using integer division to ensure the index remains an integer
        middle_index = (low_index + high_index) // 2

        # Retrieve the value at the middle index
        current_value = validated_list[middle_index]

        # Comparison Step 1: Check if the middle value matches the target
        if current_value == target:
            # Target found
            return True

        # Comparison Step 2: Check if the middle value is less than the target
        if current_value < target:
            # If the middle value is less, the target must be in the right half
            # Move the lower bound to just above the middle index
            low_index = middle_index + 1
            continue

        # Comparison Step 3: Check if the middle value is greater than the target
        if current_value > target:
            # If the middle value is greater, the target must be in the left half
            # Move the upper bound to just below the middle index
            high_index = middle_index - 1
            continue

        # This part is theoretically unreachable due to the if/elif structure above,
        # but included for explicit logic flow visibility.
        # No action needed here as one of the previous conditions must have matched.

    # If the loop completes without returning, the target was not found
    return False