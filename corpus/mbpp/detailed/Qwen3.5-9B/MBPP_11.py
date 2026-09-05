def remove_Occ(input_string: str, target_char: str) -> str:
    """
    Removes the first and last occurrence of a given character from the string.

    Parameters:
    input_string (str): The string to process.
    target_char (str): The character to remove (must be a single character).

    Returns:
    str: The modified string with the first and last occurrences of target_char removed.

    Raises:
    TypeError: If input_string is not a string or target_char is not a string.
    ValueError: If target_char is not a single character or if there are fewer than 
                two occurrences of target_char in input_string.
    """

    # Validate input_string type
    if not isinstance(input_string, str):
        raise TypeError(f"input_string must be a string, got {type(input_string).__name__}")

    # Validate target_char type
    if not isinstance(target_char, str):
        raise TypeError(f"target_char must be a string, got {type(target_char).__name__}")

    # Validate target_char length
    if len(target_char) != 1:
        raise ValueError("target_char must be a single character")

    target = target_char[0]

    # Find all occurrences of the target character
    indices = []
    current_index = 0

    while current_index < len(input_string):
        if input_string[current_index] == target:
            indices.append(current_index)
        current_index += 1

    # Check if there are fewer than two occurrences
    if len(indices) < 2:
        raise ValueError(f"Must have at least two occurrences of '{target}' to remove first and last")

    # Get the indices to remove
    first_index = indices[0]
    last_index = indices[-1]

    # Construct the result by concatenating slices
    # Part 1: from start to just before the first occurrence
    part_before_first = input_string[:first_index]

    # Part 2: from just after the first occurrence to just before the last occurrence
    # We need to exclude the first occurrence and include everything up to (but not including) the last
    part_middle = input_string[first_index + 1:last_index]

    # Part 3: from just after the last occurrence to the end
    part_after_last = input_string[last_index + 1:]

    # Combine all parts
    result = part_before_first + part_middle + part_after_last

    return result