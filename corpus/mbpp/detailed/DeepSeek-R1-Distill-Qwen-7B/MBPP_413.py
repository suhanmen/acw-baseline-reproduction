def extract_nth_element(tuples_list, n):
    # Check if the input list is None or empty
    if tuples_list is None or not tuples_list:
        raise ValueError("Input list cannot be None or empty")

    # Check if n is not an integer
    if not isinstance(n, int):
        raise TypeError("n must be an integer")

    # Check if n is negative
    if n < 0:
        raise ValueError("n cannot be negative")

    # Check if any tuple in the list is not a tuple
    for element in tuples_list:
        if not isinstance(element, tuple):
            raise TypeError("All elements in the list must be tuples")

    # Check if any tuple is empty
    for element in tuples_list:
        if len(element) == 0:
            raise ValueError("All tuples must contain at least one element")

    # Get the length of a tuple (assuming all tuples have the same length)
    tuple_length = len(tuples_list[0])

    # Check if n is out of bounds for the tuples
    if n >= tuple_length:
        raise ValueError(f"n ({n}) is out of bounds for the tuples")

    # Collect the nth element from each tuple
    result = []
    for tuple_elem in tuples_list:
        result.append(tuple_elem[n])

    return result