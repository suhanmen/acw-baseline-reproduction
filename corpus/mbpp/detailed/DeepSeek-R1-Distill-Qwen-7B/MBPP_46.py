def test_distinct(numbers):
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")

    if not numbers:
        return False  # An empty list has no distinct elements

    # Check if all elements are distinct using a set
    unique_elements = set(numbers)
    return len(unique_elements) == len(numbers)