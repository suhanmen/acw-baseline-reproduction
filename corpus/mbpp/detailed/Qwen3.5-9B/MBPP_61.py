def count_substrings(input_string: str) -> int:
    """
    Counts the number of substrings where the sum of the digits equals the length of the substring.

    Parameters:
    input_string (str): The input string containing numeric characters.

    Returns:
    int: The count of substrings meeting the criteria.

    Raises:
    TypeError: If the input is not a string.
    ValueError: If the input string is empty or contains non-digit characters.
    """
    # Input validation
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string.")

    if len(input_string) == 0:
        return 0

    if not input_string.isdigit():
        raise ValueError("Input string must contain only digit characters.")

    # Convert the entire input string into a list of integer digits immediately
    # to avoid repeated conversion overhead and keep logic clean.
    digits = [int(char) for char in input_string]

    n = len(digits)
    valid_count = 0

    # We will iterate through all possible substrings.
    # A substring is defined by its start index (i) and end index (j) inclusive.
    # Range for start index i: from 0 to n-1
    # Range for end index j: from i to n-1

    for start_index in range(n):
        current_sum = 0

        # Iterate through end indices for the current start index
        # We maintain 'current_sum' to accumulate digits as we extend the substring to the right
        for end_index in range(start_index, n):
            digit_value = digits[end_index]
            current_sum += digit_value

            # Calculate the length of the current substring (inclusive of start and end)
            current_length = end_index - start_index + 1

            # Check the condition: sum of digits equals length of substring
            if current_sum == current_length:
                valid_count += 1

    return valid_count