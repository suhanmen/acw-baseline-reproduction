def count_substring_with_equal_ends(text: str) -> int:
    """
    Counts all substrings of the input string that start and end with the same character.

    A substring is defined as a contiguous sequence of characters within the string.
    We are looking for substrings where the first character equals the last character.
    This includes single-character substrings (where start and end are the same index).

    Examples:
    - "abc": 
      - "a" (index 0 to 0)
      - "b" (index 1 to 1)
      - "c" (index 2 to 2)
      Total: 3

    - "abcda":
      - Single chars: "a", "b", "c", "d", "a" (5 substrings)
      - "abcda" (starts and ends with 'a')
      Total: 6

    Args:
        text (str): The input string to analyze.

    Returns:
        int: The count of substrings that start and end with the same character.

    Raises:
        TypeError: If the input is not a string.
        ValueError: If the input string is None.
    """

    # Validate input type
    if not isinstance(text, str):
        raise TypeError(
            f"Input must be a string, got {type(text).__name__} instead."
        )

    # Handle None case explicitly
    if text is None:
        raise ValueError("Input string cannot be None.")

    # Handle empty string case
    if len(text) == 0:
        return 0

    # Handle single character case
    if len(text) == 1:
        return 1

    # Initialize the count variable
    total_count = 0

    # Get the length of the string for use in loops
    n = len(text)

    # Iterate through all possible starting positions
    for start_index in range(n):
        start_character = text[start_index]

        # Iterate through all possible ending positions starting from the current start index
        for end_index in range(start_index, n):
            end_character = text[end_index]

            # Check if the starting and ending characters match
            if start_character == end_character:
                total_count += 1

    return total_count