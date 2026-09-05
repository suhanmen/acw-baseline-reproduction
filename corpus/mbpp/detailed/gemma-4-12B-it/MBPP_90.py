from typing import List


def len_log(words: List[str]) -> int:
    """
    Calculates the length of the longest word in a list of strings.

    Args:
        words (List[str]): A list of strings to evaluate.

    Returns:
        int: The length of the longest string in the list.
             Returns 0 if the list is empty.

    Raises:
        TypeError: If the input is not a list or contains non-string elements.
    """
    # Step 1: Validate that the input is a list
    if not isinstance(words, list):
        raise TypeError(f"Expected a list of strings, but received {type(words).__name__}")

    # Step 2: Handle the empty list edge case immediately
    if not words:
        return 0

    # Step 3: Initialize the maximum length variable
    # Starting at 0 ensures that even if inputs were empty strings, 
    # the result remains 0.
    max_length = 0

    # Step 4: Iterate through the words to find the maximum length
    for index, word in enumerate(words):
        # Validate that each element in the list is actually a string
        if not isinstance(word, str):
            raise TypeError(
                f"Element at index {index} is not a string: {type(word).__name__}"
            )

        # Calculate the length of the current string
        current_word_length = len(word)

        # Explicit comparison and update logic
        if current_word_length > max_length:
            max_length = current_word_length

    # Step 5: Return the final result
    return max_length


if __name__ == "__main__":
    # The following assertions verify the requirements provided in the prompt.
    assert len_log(["python", "PHP", "bigdata"]) == 7
    assert len_log(["a", "ab", "abc"]) == 3
    assert len_log(["small", "big", "tall"]) == 5

    # Additional defensive edge cases
    assert len_log([]) == 0
    assert len_log([""]) == 0
    assert len_log(["a"]) == 1
    assert len_log(["aaaaa", "bbbbb"]) == 5