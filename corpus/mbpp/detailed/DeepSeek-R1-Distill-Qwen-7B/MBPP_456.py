def reverse_string_list(strings):
    """
    Reverses each string in a given list of strings and returns the modified list.

    Args:
        strings: A list of strings to be processed.

    Returns:
        A list containing the reversed strings.

    Raises:
        ValueError: If any element in the input is not a string.
    """
    # Validate input: check if all elements are strings
    if not all(isinstance(s, str) for s in strings):
        raise ValueError("All elements in the input must be strings.")

    # Reverse each string and collect the results
    reversed_strings = []
    for s in strings:
        reversed_string = s[::-1]
        reversed_strings.append(reversed_string)

    return reversed_strings

# Example usage:
# reversed_list = reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black'])
# print(reversed_list)  # Output: ['deR', 'neerG', 'eulB', 'etihW', 'kcalB']