def index_on_inner_list(data_list, sort_index):
    """
    Sorts a list of lists by the value at a given index within each inner list.

    The sorting is performed in ascending order. If two items have the same value
    at the specified index, their relative order in the original list is preserved
    (stable sort).

    Parameters:
    data_list (list): A list containing inner lists or tuples. Each inner list/tuple
                      must have at least (sort_index + 1) elements.
    sort_index (int): The index of the element within the inner lists/tuples to use
                      for sorting.

    Returns:
    list: A new list containing the original elements sorted based on the value at 
          sort_index.

    Raises:
    ValueError: If the data_list is not a list or if sort_index is not an integer.
    IndexError: If any inner list/tuple is shorter than sort_index + 1, or if sort_index 
                is negative.
    TypeError: If any element in data_list is not a list or tuple.
    """

    # Step 1: Validate that the input data_list is actually a list.
    if not isinstance(data_list, list):
        raise ValueError(
            f"Expected the first argument to be a list, but got {type(data_list).__name__}."
        )

    # Step 2: Validate that the sort_index is an integer.
    # Note: We must explicitly check for bool because bool is a subclass of int in Python.
    if not isinstance(sort_index, int) or isinstance(sort_index, bool):
        raise ValueError(
            f"Expected the second argument 'sort_index' to be an integer, "
            f"but got {type(sort_index).__name__}."
        )

    # Step 3: Validate that sort_index is non-negative.
    # The problem implies indexing into inner lists, so negative indices would 
    # be ambiguous unless specified, and typically "index" implies 0, 1, 2...
    # However, standard list indexing allows negatives. Given the problem context
    # and typical interpretation of "index of the inner list" for sorting data,
    # we will enforce non-negative to prevent accessing "last" elements which
    # might not be the intended semantics of a positive integer index.
    # If negative indices were intended, the problem usually specifies "index from end".
    if sort_index < 0:
        raise IndexError(
            f"Expected a non-negative sort_index for forward indexing, "
            f"but got {sort_index}."
        )

    # Step 4: Iterate through the data_list to validate structure and check for IndexError.
    # We do this separately before sorting to provide a clear error message 
    # and ensure all constraints are met upfront.
    validated_index_value = None
    num_items = 0

    for current_item in data_list:
        # Step 4a: Validate that each item in the list is a list or a tuple.
        if not isinstance(current_item, (list, tuple)):
            raise TypeError(
                f"All items in data_list must be lists or tuples, "
                f"but found {type(current_item).__name__} at index {num_items}."
            )

        # Step 4b: Check the length of the current item to ensure the index exists.
        current_length = len(current_item)

        if current_length <= sort_index:
            raise IndexError(
                f"The inner list/tuple at index {num_items} has length {current_length}, "
                f"but sort_index is {sort_index}. The index does not exist."
            )

    # Step 5: Perform the actual sorting.
    # We use the standard sorted() function which is stable (preserves order of equal keys).
    # We use a lambda function to extract the key (the value at sort_index) for each item.
    sorted_data = sorted(data_list, key=lambda x: x[sort_index])

    return sorted_data