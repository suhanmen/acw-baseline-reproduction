def concatenate_elements(elements):
    """
    Concatenates all elements of the given list into a string with a space separator.

    Args:
        elements (list): A list of strings to be concatenated.

    Returns:
        str: A single string with all elements concatenated with spaces.

    Raises:
        TypeError: If elements is not a list.
        ValueError: If any element in the list is not a string.
    """
    # Validate input
    if not isinstance(elements, list):
        raise TypeError("elements must be a list")

    # Check if all elements are strings
    if not all(isinstance(e, str) for e in elements):
        raise ValueError("All elements must be strings")

    # Handle empty list case
    if not elements:
        return ""

    # Join the elements with a space separator
    result = ' '.join(elements)

    return result