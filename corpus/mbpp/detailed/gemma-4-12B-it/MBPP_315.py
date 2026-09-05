from typing import List

def find_Max_Len_Even(input_string: str) -> str:
    """
    Finds the first occurrence of the longest even-length word in a given string.

    Criteria:
    1. A word is defined as a sequence of characters separated by whitespace.
    2. A word is "even" if its length is an even number (length % 2 == 0).
    3. If multiple words have the same maximum even length, the first one encountered is returned.
    4. If no even-length words are found, or the input is empty, return "-1".

    Args:
        input_string (str): The string to search within.

    Returns:
        str: The longest even-length word or "-1" if none exists.
    """
    # Handle the case where input is not a string or is empty
    if not isinstance(input_string, str):
        return "-1"

    if not input_string.strip():
        return "-1"

    # Split the input string into individual words by whitespace
    # This handles multiple spaces, tabs, and newlines
    words: List[str] = input_string.split()

    # Variables to track the best candidate found so far
    max_even_word: str = ""
    max_even_length: int = -1

    for word in words:
        # Clean the word (optional, but good for production code 
        # to handle punctuation if implied, though standard split is usually sufficient)
        # For the sake of the specific test cases, standard split is used.
        current_length = len(word)

        # Check if the word has an even length
        is_even = (current_length % 2 == 0)

        if is_even:
            # If this word is strictly longer than the previous max, update
            # We use strictly greater (>) to ensure we keep the 'first' occurrence
            if current_length > max_even_length:
                max_even_length = current_length
                max_even_word = word

    # Final determination of return value
    if max_even_length == -1:
        # No even length words were found
        return "-1"
    else:
        # Return the longest even word found
        return max_even_word

# Test cases to verify functionality
if __name__ == "__main__":
    # Assertion 1: "language" is length 8, "python" is 6. "language" is longer.
    assert find_Max_Len_Even("python language") == "language"

    # Assertion 2: "maximum" (7), "even" (4), "length" (6). "length" is longest even.
    assert find_Max_Len_Even("maximum even length") == "length"

    # Assertion 3: "eve" is length 3 (odd). No even words.
    assert find_Max_Len_Even("eve") == "-1"