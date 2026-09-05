def sort_mixed_list(elements):
    """Sort a mixed list of integers and strings with integers first, followed by strings."""

    # Helper function to check if an element is an integer
    def is_integer(e):
        return isinstance(e, int)

    # Helper function to check if an element is a string
    def is_string(e):
        return isinstance(e, str)

    # Handle empty input
    if not isinstance(elements, list):
        return None
    if not elements:
        return []

    # Separate integers and strings
    integers = []
    strings = []
    for e in elements:
        if is_integer(e):
            integers.append(e)
        elif is_string(e):
            strings.append(e)

    # Sort integers and strings separately
    integers_sorted = sorted(integers)
    strings_sorted = sorted(strings)

    # Combine the two sorted lists
    sorted_list = integers_sorted + strings_sorted

    return sorted_list