from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Define the ordering and mapping of the number words to integers.
    # This allows us to sort based on numeric value while preserving the word for output.
    number_map = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }

    # Handle empty input or whitespace-only input gracefully.
    if not numbers or numbers.strip() == "":
        return ""

    # Split the string into individual words by whitespace.
    # .split() without arguments handles multiple spaces and leading/trailing spaces.
    raw_words = numbers.split()

    # Validate and clean the words list.
    # We want to ensure that we only process words that are present in our map.
    valid_words = []
    for word in raw_words:
        # Normalize input (lowercase) to be case-insensitive if needed,
        # though the prompt implies lowercase. Let's stick to strict map check.
        normalized_word = word.strip().lower()
        if normalized_word in number_map:
            valid_words.append(normalized_word)
        else:
            # In a production environment, we could raise a ValueError here.
            # For this task, we skip invalid words or treat them as non-existent.
            pass

    # If no valid words were found after filtering, return an empty string.
    if not valid_words:
        return ""

    # Sorting logic:
    # We need to sort the words based on the integer value they represent.
    # We use a stable sort to maintain relative order of equal elements if necessary.
    # The key function extracts the integer value from our mapping.
    sorted_words = sorted(
        valid_words, 
        key=lambda word: number_map[word]
    )

    # Join the sorted words back into a space-delimited string.
    result = " ".join(sorted_words)

    return result