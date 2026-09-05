import typing

def anti_shuffle(s: str) -> str:
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'
    """
    # Defensive Programming: Validate that the input is actually a string
    if not isinstance(s, str):
        raise TypeError(f"Expected input of type str, but got {type(s).__name__}")

    # Handle empty string edge case
    if len(s) == 0:
        return ""

    def sort_word_characters(word: str) -> str:
        """
        Helper function to sort characters of a word by ASCII value.
        """
        # Convert string to a list of characters
        char_list = list(word)

        # Sort the list in ascending order based on ASCII values
        char_list.sort()

        # Join the characters back into a string
        sorted_word = "".join(char_list)
        return sorted_word

    # The requirement is to keep the order of words and blank spaces.
    # Words are defined as segments separated by spaces.
    # We need to split the string while preserving the spaces.

    # Approach: Iterate through the string and identify contiguous blocks 
    # of non-space characters (words) and preserve spaces as they are.

    result_parts = []
    current_word_buffer = []

    for char in s:
        if char == " ":
            # If we hit a space, it means the preceding buffer was a word.
            # Process the word if the buffer is not empty.
            if current_word_buffer:
                word_to_sort = "".join(current_word_buffer)
                sorted_word = sort_word_characters(word_to_sort)
                result_parts.append(sorted_word)
                current_word_buffer = []

            # Append the space to the results
            result_parts.append(" ")
        else:
            # Accumulate characters for the current word
            current_word_buffer.append(char)

    # Handle the final word if the string did not end with a space
    if current_word_buffer:
        word_to_sort = "".join(current_word_buffer)
        sorted_word = sort_word_characters(word_to_sort)
        result_parts.append(sorted_word)

    # Combine all parts back into a single string
    final_string = "".join(result_parts)

    return final_string