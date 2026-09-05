def sort_array(arr):
    """
    In this Kata, you have to sort an array of non-negative integers according to
    number of ones in their binary representation in ascending order.
    For similar number of ones, sort based on decimal value.

    It must be implemented like this:
    >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4]) [0, 1, 2, 3, 4]
    """

    def _validate_element(element):
        """
        Validates that a single element is a non-negative integer.
        Raises a TypeError if the element is not an int or if it is negative.
        """
        if not isinstance(element, int):
            raise TypeError(f"All elements must be integers, but got {type(element).__name__}: {element}")
        if element < 0:
            raise ValueError(f"All elements must be non-negative integers, but got {element}")

    def _count_ones_in_binary(element):
        """
        Counts the number of set bits (ones) in the binary representation of the element.
        Since the input is guaranteed to be non-negative by validation, we can use bin().

        Args:
            element (int): A non-negative integer.

        Returns:
            int: The count of ones in the binary representation.
        """
        binary_representation = bin(element)
        # bin() returns a string like '0b101'. We slice off the '0b' prefix and count '1's.
        binary_string_part = binary_representation[2:]
        ones_count = binary_string_part.count('1')
        return ones_count

    def _sort_key(item):
        """
        Generates a sort key tuple for a given integer.

        The primary sort criterion is the count of ones in the binary representation (ascending).
        The secondary sort criterion is the decimal value itself (ascending),
        used when the number of ones is identical.

        Returns:
            tuple: (ones_count, decimal_value)
        """
        ones_count = _count_ones_in_binary(item)
        decimal_value = item
        return (ones_count, decimal_value)

    # Step 1: Input Validation and Sanity Checks

    # Check for None input
    if arr is None:
        raise TypeError("Input must be a list or tuple, not None")

    # Check type of input container
    if not isinstance(arr, (list, tuple)):
        raise TypeError(f"Input must be a list or tuple, but got {type(arr).__name__}")

    # Check if the container is empty (edge case, though valid to return empty)
    is_empty = len(arr) == 0

    # Validate every element in the array
    for index, element in enumerate(arr):
        _validate_element(element)

    # Step 2: Transformation

    # We will create a list of tuples to perform the sort.
    # Each tuple will be: (sort_key_primary, sort_key_secondary, original_value)
    # This makes the sort logic explicit rather than relying on Python's default tuple sorting 
    # of a lambda function result, ensuring clarity and strict adherence to requirements.
    transformation_list = []

    for index, element in enumerate(arr):
        ones_count = _count_ones_in_binary(element)
        decimal_value = element
        sort_key = (ones_count, decimal_value)

        transformation_list.append({
            'original_value': element,
            'sort_key': sort_key
        })

    # Step 3: Sorting

    # Sort the transformed list based on the 'sort_key'
    # Python's sort is stable, but our secondary key (decimal_value) makes explicit stability less critical for correctness,
    # though it preserves order for equal keys if they were originally in a specific sequence.
    # We sort explicitly by the two criteria defined in _sort_key.
    sorted_transformation_list = sorted(
        transformation_list,
        key=lambda item: item['sort_key']
    )

    # Step 4: Extraction

    # Extract the original integer values from the sorted transformation list
    sorted_result = []
    for item in sorted_transformation_list:
        sorted_result.append(item['original_value'])

    # Step 5: Return
    return sorted_result