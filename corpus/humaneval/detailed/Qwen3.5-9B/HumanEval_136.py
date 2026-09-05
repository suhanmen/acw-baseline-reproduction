def largest_smallest_integers(lst):
    """
    Create a function that returns a tuple (a, b), where 'a' is
    the largest of negative integers, and 'b' is the smallest
    of positive integers in a list.
    If there is no negative or positive integers, return them as None.

    Examples:
    largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    largest_smallest_integers([]) == (None, None)
    largest_smallest_integers([0]) == (None, None)
    """
    # Validate that the input is indeed a list (or list-like sequence)
    if not isinstance(lst, list):
        raise TypeError(f"Expected a list, but got {type(lst).__name__}")

    # Helper function to find the largest negative integer
    def find_largest_negative(numbers):
        """
        Scans the provided list for negative integers.
        Returns the largest (closest to zero) negative integer found,
        or None if no negative integers exist.
        """
        largest_neg = None
        for num in numbers:
            # Ensure the number is an integer (defensive check against floats like 2.5)
            if not isinstance(num, int):
                continue

            if num < 0:
                # If we haven't found a negative yet, this is the first one (and thus largest)
                if largest_neg is None:
                    largest_neg = num
                else:
                    # Update if the current number is larger (closer to 0) than the stored one
                    if num > largest_neg:
                        largest_neg = num

        return largest_neg

    # Helper function to find the smallest positive integer
    def find_smallest_positive(numbers):
        """
        Scans the provided list for positive integers.
        Returns the smallest positive integer found,
        or None if no positive integers exist.
        """
        smallest_pos = None
        for num in numbers:
            # Ensure the number is an integer (defensive check against floats like 2.5)
            if not isinstance(num, int):
                continue

            if num > 0:
                # If we haven't found a positive yet, this is the first one (and thus smallest)
                if smallest_pos is None:
                    smallest_pos = num
                else:
                    # Update if the current number is smaller than the stored one
                    if num < smallest_pos:
                        smallest_pos = num

        return smallest_pos

    # Helper function to validate contents (optional strictness)
    def validate_elements_are_numbers(data):
        """
        Checks if all elements in the list are either int or float.
        Raises a ValueError if non-numeric types are found.
        """
        for i, item in enumerate(data):
            if not isinstance(item, (int, float)):
                raise ValueError(f"Invalid element at index {i}: expected a number, got {type(item).__name__}")

    # Step 1: Validate that all elements are numbers (handling potential edge cases with non-numeric lists)
    validate_elements_are_numbers(lst)

    # Step 2: Initialize result variables with defaults
    result_negative = None
    result_positive = None

    # Step 3: Execute the helper functions on the validated list
    # We call them separately to maintain clear separation of concerns as requested
    result_negative = find_largest_negative(lst)
    result_positive = find_smallest_positive(lst)

    # Step 4: Return the tuple containing the results
    return (result_negative, result_positive)