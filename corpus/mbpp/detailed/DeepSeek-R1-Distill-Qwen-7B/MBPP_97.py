def frequency_lists(list_of_lists):
    """
    Calculate the frequency count of each integer in a list of lists.

    Args:
        list_of_lists (list of list of int): A list where each element is a list of integers.

    Returns:
        dict: A dictionary where keys are integers and values are their counts.

    Raises:
        ValueError: If the input is not a list of lists, or if any sublist contains non-integer elements.
    """
    # Step 1: Validate the input
    if not isinstance(list_of_lists, list):
        raise ValueError("Input must be a list of lists.")
    for sublist in list_of_lists:
        if not isinstance(sublist, list):
            raise ValueError("All elements of the input must be lists.")
        for element in sublist:
            if not isinstance(element, int):
                raise ValueError(f"Sublist contains non-integer element: {element}")

    # Step 2: Flatten the list of lists
    flattened = []
    for sublist in list_of_lists:
        flattened.extend(sublist)

    # Step 3: Count the occurrences
    frequency = {}
    for num in flattened:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    # Step 4: Return the frequency dictionary
    return frequency