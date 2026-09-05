def counting_sort(arr):
    """
    Sorts a list of non-negative integers using the Counting Sort algorithm.

    This function implements the standard Counting Sort logic:
    1. Validates that the input is a list of integers and that all integers are non-negative.
    2. Handles the edge case of an empty list by returning an empty list.
    3. Finds the maximum value in the array to determine the range of the counting array.
    4. Creates a count array initialized to zeros, sized to accommodate values from 0 to max_value.
    5. Populates the count array by iterating through the input array and tallying occurrences.
    6. Populates the output array by iterating backwards through the count array to ensure stability.

    Time Complexity: O(n + k) where n is the number of elements and k is the range of input data.
    Space Complexity: O(n + k).

    Args:
        arr (list of int): A list of non-negative integers to be sorted.

    Returns:
        list of int: A new list containing the sorted elements.

    Raises:
        TypeError: If the input is not a list or contains non-integer elements.
        ValueError: If the input contains negative numbers.
    """

    # Step 1: Type validation for the input variable
    if not isinstance(arr, list):
        raise TypeError("Input must be a list.")

    # Handle the edge case of an empty input list explicitly
    if len(arr) == 0:
        return []

    # Helper function to validate elements: must be non-negative integers
    for i in range(0, len(arr)):
        current_element = arr[i]

        # Check for integer type explicitly
        if not isinstance(current_element, int):
            raise TypeError(f"All elements must be integers, found {type(current_element).__name__}.")

        # Check for negative numbers
        if current_element < 0:
            raise ValueError("Counting sort requires non-negative integers.")

    # Step 2: Find the range of the input data (minimum and maximum)
    # Since we validated non-negative integers, the minimum is implicitly 0 or the smallest actual value.
    # We calculate min and max to define the range [0, max_value].
    min_val = arr[0]
    max_val = arr[0]

    for i in range(1, len(arr)):
        current_element = arr[i]

        if current_element < min_val:
            min_val = current_element

        if current_element > max_val:
            max_val = current_element

    # Step 3: Calculate the size of the counting array (bucket size)
    # The count array needs indices from min_val to max_val.
    # Range size = max_val - min_val + 1.
    bucket_count = max_val - min_val + 1

    # Step 4: Initialize the count array (buckets) with zeros
    count_array = [0] * bucket_count

    # Step 5: Populate the count array with frequencies of each element
    for i in range(0, len(arr)):
        current_element = arr[i]
        # Calculate the index in the count array relative to min_val
        bucket_index = current_element - min_val
        count_array[bucket_index] += 1

    # Step 6: Construct the sorted output array
    # We iterate backwards through the count array to maintain stability 
    # (though stability isn't strictly required for integers, it is part of the algorithmic definition).
    sorted_array = []
    sorted_array_length = len(arr)

    for i in range(bucket_count - 1, -1, -1):
        frequency = count_array[i]

        # Process all occurrences of the current number
        while frequency > 0:
            actual_value = min_val + i
            sorted_array.append(actual_value)
            frequency -= 1

    return sorted_array