def remove_tuples(input_list: list, k: int) -> list:
    """
    Removes all tuples from the input list that have a length equal to k.

    Parameters:
        input_list (list): A list containing tuples.
        k (int): The target length of tuples to remove.

    Returns:
        list: A new list with tuples of length k removed.

    Raises:
        TypeError: If input_list is not a list or k is not an integer.
        ValueError: If k is negative.
    """

    # Validate input_list type
    if not isinstance(input_list, list):
        raise TypeError(f"Expected 'input_list' to be a list, but got {type(input_list).__name__}")

    # Validate k type
    if not isinstance(k, int):
        raise TypeError(f"Expected 'k' to be an integer, but got {type(k).__name__}")

    # Validate k value
    if k < 0:
        raise ValueError(f"Expected 'k' to be non-negative, but got {k}")

    result_list = []

    # Iterate through each element in the input list
    for current_element in input_list:
        # Check if the current element is a tuple
        if not isinstance(current_element, tuple):
            raise TypeError(f"Expected all elements in 'input_list' to be tuples, but got {type(current_element).__name__} for element {current_element}")

        # Get the length of the current tuple
        current_length = len(current_element)

        # Check if the current tuple's length is NOT equal to k
        if current_length != k:
            result_list.append(current_element)

    return result_list