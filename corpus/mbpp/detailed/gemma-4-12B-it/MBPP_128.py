from typing import List


def long_words(n: int, text: str) -> List[str]:
    """
    Shortlists words from a given string that have a length strictly greater than n.

    Args:
        n (int): The minimum length threshold (exclusive).
        text (str): The input string containing words.

    Returns:
        List[str]: A list of words longer than n.

    Raises:
        ValueError: If n is negative.
        TypeError: If n is not an integer or text is not a string.
    """
    # --- Input Validation ---
    if not isinstance(n, int):
        raise TypeError(f"Parameter 'n' must be an integer, got {type(n).__name__}.")

    if not isinstance(text, str):
        raise TypeError(f"Parameter 'text' must be a string, got {type(text).__name__}.")

    if n < 0:
        raise ValueError(f"Threshold 'n' must be a non-negative integer, got {n}.")

    # --- Handle Edge Cases ---
    # If text is empty or only whitespace, return an empty list
    if not text or text.isspace():
        return []

    # --- Processing Steps ---

    # 1. Split the input string into individual words.
    # .split() without arguments handles multiple spaces and newlines automatically.
    raw_words: List[str] = text.split()

    # 2. Clean and filter words.
    # We iterate through words and keep only those whose length > n.
    # Note: The problem examples show that punctuation is not explicitly
    # stripped, but standard words are kept as they appear in the string.
    result_list: List[str] = []

    for word in raw_words:
        word_length: int = len(word)

        if word_length > n:
            result_list.append(word)

    return result_list


# The following section contains the assertions provided in the prompt.
if __name__ == "__main__":
    # Validation of requirements
    assert long_words(3, "python is a programming language") == ['python', 'programming', 'language']
    assert long_words(2, "writing a program") == ['writing', 'program']
    assert long_words(5, "sorting list") == ['sorting']