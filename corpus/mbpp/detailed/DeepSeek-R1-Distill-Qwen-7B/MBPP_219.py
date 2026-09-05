def extract_min_max(data, k):
    """
    Extracts maximum and minimum k elements from the given tuple.

    Args:
        data (tuple): The input tuple of integers.
        k (int): The number of minimum and maximum elements to extract.

    Returns:
        tuple: A tuple containing 2k elements, first k minima and then k maxima.
    """
    # Handle edge case: empty input or k is 0 or less
    if not data or k <= 0:
        return ()

    # Handle case where k is larger than the length of the input
    if k >= len(data):
        return ()

    # Create a sorted copy of the data to avoid modifying the original
    sorted_data = sorted(data)

    # Extract the first k minima
    min_elements = sorted_data[:k]

    # Extract the last k maxima
    max_elements = sorted_data[-k:]

    # Combine the min and max elements
    result = min_elements + max_elements

    return result