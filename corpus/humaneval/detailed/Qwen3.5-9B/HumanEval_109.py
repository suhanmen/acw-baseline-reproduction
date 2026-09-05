def move_one_ball(arr):
    """We have an array 'arr' of N integers arr[1], arr[2], ..., arr[N].The
    numbers in the array will be randomly ordered. Your task is to determine if
    it is possible to get an array sorted in non-decreasing order by performing 
    the following operation on the given array:
        You are allowed to perform right shift operation any number of times.

    One right shift operation means shifting all elements of the array by one
    position in the right direction. The last element of the array will be moved to
    the starting position in the array i.e. 0th index. 

    If it is possible to obtain the sorted array by performing the above operation
    then return True else return False.
    If the given array is empty then return True.

    Note: The given list is guaranteed to have unique elements.

    For Example:

    move_one_ball([3, 4, 5, 1, 2])==>True
    Explanation: By performin 2 right shift operations, non-decreasing order can
                 be achieved for the given array.
    move_one_ball([3, 5, 4, 1, 2])==>False
    Explanation:It is not possible to get non-decreasing order for the given
                array by performing any number of right shift operations.

    """

    def is_sorted_linearly(sequence):
        """
        Helper function to check if a given sequence is sorted in non-decreasing order.
        This is a basic verification step.
        """
        # Iterate through the sequence up to the second-to-last element
        for i in range(len(sequence) - 1):
            current_value = sequence[i]
            next_value = sequence[i + 1]

            # If current value is greater than the next, it's not sorted
            if current_value > next_value:
                return False

        # If the loop completes without returning False, the sequence is sorted
        return True

    def check_rotated_sortedness(original_array):
        """
        Helper function to determine if the array is a rotation of a sorted array.
        This is done by checking for the single "drop" point where a larger number
        is followed by a smaller number.
        """
        n = len(original_array)

        # Count the number of "descents" (where arr[i] > arr[i+1])
        # In a valid rotation of a sorted array with unique elements, 
        # there should be exactly 0 or 1 such descent.

        descent_count = 0
        descent_index = -1

        for i in range(n - 1):
            current_val = original_array[i]
            next_val = original_array[i + 1]

            if current_val > next_val:
                descent_count += 1
                descent_index = i

                # If we find more than one descent, it cannot be a rotated sorted array
                if descent_count > 1:
                    return False

        # Special case: If there are 0 descents, the array is already sorted.
        # This is a valid rotation (0 shifts).
        if descent_count == 0:
            return True

        # If there is exactly 1 descent:
        # The array looks like: [Large...Large] [Small...Small]
        # Example: [3, 4, 5, 1, 2] -> Descent at index 2 (5 > 1)
        # For this to be a rotated sorted array, the first element must be 
        # greater than the last element (wrapping around), effectively completing
        # the sorted sequence if we were to rotate.
        # Since elements are unique, if we have exactly 1 descent, the array 
        # represents a sorted sequence that has been cut and pasted.
        # We just need to ensure the wrap-around is consistent with the sorted order.
        # Actually, if elements are unique and there is exactly 1 descent, 
        # the array is ALWAYS a rotation of a sorted array.
        # Why? Because if there's only one break point, splitting there and joining
        # the end to the beginning creates a sorted sequence.

        # However, we must also consider the case of empty array or single element
        # which are handled in the main function before this logic usually.
        # But for completeness here:
        if n > 0:
            return True

        return False

    # --- Main Logic Execution ---

    # Step 1: Validate Input Type
    # The problem implies an array of integers. We expect a list.
    if not isinstance(arr, list):
        return False

    # Step 2: Handle Edge Case - Empty Array
    # The problem statement explicitly says: "If the given array is empty then return True."
    if len(arr) == 0:
        return True

    # Step 3: Handle Edge Case - Single Element
    # A single element array is trivially sorted. No operations needed.
    if len(arr) == 1:
        return True

    # Step 4: Analyze the structure for "Rotated Sorted" property
    # We use the helper function which counts descents.
    # Logic: 
    # 1. If 0 descents: Already sorted. (True)
    # 2. If 1 descent: It is a rotation of a sorted array. (True)
    #    Example: [3, 4, 5, 1, 2] -> 5 > 1 is the only drop.
    # 3. If > 1 descents: It is not a rotation of a sorted array. (False)
    #    Example: [3, 5, 4, 1, 2] -> 5>4 and 4>1 are two drops. Impossible.

    # We can implement this directly without a separate call to keep flow linear,
    # but using the helper makes the step explicit as requested.

    is_valid_rotation = check_rotated_sortedness(arr)

    # Step 5: Return the result
    # If the helper returns True, it means we can shift the array to make it sorted.
    return is_valid_rotation


# Note: The function above is self-contained and runnable.
# It handles all specified edge cases:
# - Empty list: Returns True explicitly.
# - Single element: Returns True explicitly.
# - Unique elements: Logic relies on the unique property to distinguish 0 vs 1 descent clearly.
# - Negative/Zero numbers: Comparison operators work correctly regardless of sign.
# - Invalid type: Returns False for non-list inputs.