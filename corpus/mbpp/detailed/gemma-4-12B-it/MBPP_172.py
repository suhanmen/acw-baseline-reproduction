def count_occurance(input_string: str) -> int:
    """
    Counts the number of occurrences of the substring 'std' within a given string.

    This function handles various edge cases such as empty strings, null values,
    non-string inputs, and overlapping scenarios (though 'std' cannot overlap 
    with itself in a way that shares characters).

    Args:
        input_string (str): The string to search within.

    Returns:
        int: The count of occurrences of 'std'.

    Raises:
        TypeError: If the input is not a string.
    """
    # 1. Input Validation
    # Ensure the input is actually a string to prevent runtime crashes on non-string types.
    if not isinstance(input_string, str):
        raise TypeError(f"Expected input_string to be of type str, but got {type(input_string).__name__}")

    # 2. Handle Edge Cases
    # If the string is empty or shorter than the target substring, the count is zero.
    target_substring = "std"
    target_length = len(target_substring)

    if not input_string or len(input_string) < target_length:
        return 0

    # 3. Implementation Logic
    # We iterate through the string and check if the slice starting at each index 
    # matches the target substring. This is a defensive, explicit approach.
    occurrence_count = 0
    string_length = len(input_string)

    # We only need to loop up to the point where the remaining string 
    # is at least as long as the target substring.
    for index in range(string_length - target_length + 1):
        # Extract the current window of characters
        current_slice = input_string[index : index + target_length]

        # Check if the current window matches our target
        if current_slice == target_substring:
            occurrence_count += 1

    return occurrence_count

if __name__ == "__main__":
    # Testing the requirements provided in the prompt
    assert count_occurance("letstdlenstdporstd") == 3
    assert count_occurance("truststdsolensporsd") == 1
    assert count_occurance("makestdsostdworthit") == 2

    # Additional defensive checks
    assert count_occurance("") == 0
    assert count_occurance("st") == 0
    assert count_occurance("stdstdstd") == 3
    assert count_occurance("no_match_here") == 0
    assert count_occurance("STD") == 0  # Case sensitivity check