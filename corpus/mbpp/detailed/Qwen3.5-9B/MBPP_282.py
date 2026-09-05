def _validate_input_lists(first_list, second_list):
    """
    Validates that both inputs are lists.
    Raises a TypeError if either input is not a list.
    """
    if not isinstance(first_list, list):
        raise TypeError(f"First argument must be a list, got {type(first_list).__name__}")
    if not isinstance(second_list, list):
        raise TypeError(f"Second argument must be a list, got {type(second_list).__name__}")


def _validate_equal_lengths(first_list, second_list):
    """
    Validates that both input lists have the same length.
    Raises a ValueError if lengths differ.
    """
    length_first = len(first_list)
    length_second = len(second_list)

    if length_first != length_second:
        raise ValueError(
            f"Input lists must have equal lengths. "
            f"First list has {length_first} elements, second has {length_second}."
        )


def sub_list(first_list, second_list):
    """
    Subtracts the second list from the first list element-wise using map and lambda.

    Behavior:
    - Validates inputs are lists.
    - Validates lists are of equal length.
    - Returns a new list where each element is (first[i] - second[i]).
    - Handles empty lists, single elements, all-equal elements, zero, negative numbers, etc.

    Examples:
    sub_list([1, 2, 3], [4, 5, 6]) -> [-3, -3, -3]
    sub_list([1, 2], [3, 4]) -> [-2, -2]
    sub_list([90, 120], [50, 70]) -> [40, 50]
    """

    # Step 1: Validate types
    _validate_input_lists(first_list, second_list)

    # Step 2: Validate lengths
    _validate_equal_lengths(first_list, second_list)

    # Step 3: Create the list comprehension using map and lambda
    # Note: The prompt requires using map and lambda.
    # We define a lambda function that subtracts the second element from the first.
    subtraction_operation = lambda x, y: x - y

    # Step 4: Apply the map function over both lists
    mapped_result = map(subtraction_operation, first_list, second_list)

    # Step 5: Convert the map object to a list of results
    result = list(mapped_result)

    return result