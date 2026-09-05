def find_max(records):
    """
    Find the maximum element from a list of two-element tuples.

    Args:
        records (list): A list of tuples, each containing exactly two elements.

    Returns:
        The maximum element found among all tuples.

    Raises:
        ValueError: If the input is invalid.
    """
    # Step 1: Validate the input
    if not isinstance(records, list):
        raise ValueError("Invalid input: records must be a list of tuples.")

    for record in records:
        # Check if each record is a tuple and has exactly two elements
        if not isinstance(record, tuple) or len(record) != 2:
            raise ValueError("Invalid input: each element must be a tuple with exactly two elements.")

    # Step 2: Extract all elements into a single list
    elements = []
    for num in records:
        elements.append(num[0])
        elements.append(num[1])

    # Step 3: Find the maximum element
    try:
        maximum = max(elements)
    except ValueError:
        # This exception occurs if the elements list is empty
        raise ValueError("The input list is empty.")

    # Step 4: Return the maximum element
    return maximum