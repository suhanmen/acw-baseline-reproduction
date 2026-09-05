from typing import List


def split_lowerstring(input_string: str) -> List[str]:
    """
    Splits a string into a list of substrings based on lowercase letters.
    The logic follows the behavior established in the assertions:
    - Every lowercase letter is treated as a delimiter.
    - The substrings between these delimiters (or between a delimiter and a boundary)
      are collected.
    - If a delimiter is followed immediately by another delimiter, an empty 
      string logic might apply, but the examples suggest we are extracting 
      the non-lowercase segments separated by lowercase characters.

    Looking at the examples:
    1. "AbCd" -> ['bC', 'd'] ?? 
       Wait, let's re-examine the provided assertions carefully:
       "AbCd" -> ['bC', 'd']
       "Python" -> ['y', 't', 'h', 'o', 'n']
       "Programming" -> ['r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g']

    Re-evaluating the pattern:
    Example 1: "AbCd"
    'A' (Upper), 'b' (Lower), 'C' (Upper), 'd' (Lower)
    If 'b' and 'd' are delimiters, the segments are:
    Before 'b': "A"
    Between 'b' and 'd': "C"
    After 'd': ""
    Result: ['A', 'C', ''] -> This doesn't match ['bC', 'd'].

    Let's look at the logic again. 
    "Python": 'P' (U), 'y' (L), 't' (L), 'h' (L), 'o' (L), 'n' (L)
    If lowercase letters are the ONLY things we keep? 
    "Python" -> ['y', 't', 'h', 'o', 'n'] (Correct)
    "Programming" -> ['r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g'] (Correct)
    "AbCd" -> ['b', 'd'] ? No, the assertion says ['bC', 'd'].

    Wait, look at "AbCd" again. 
    'b' is lowercase. 'C' is uppercase. 'd' is lowercase.
    The result is ['bC', 'd'].

    Let's re-read: "split a string at lowercase letters".
    In "AbCd":
    The first lowercase letter is 'b'. 
    If we "split" at 'b', we get "A" and "Cd".
    If we "split" at 'd' in "Cd", we get "C" and "".

    Let's try a different interpretation:
    Maybe it means: find every lowercase letter. The string is split into 
    parts. But the parts returned are the substrings starting FROM a lowercase letter 
    UNTIL the next lowercase letter?

    Example 1: "AbCd"
    Lowercases are at indices: 1 ('b') and 3 ('d').
    Substring from index 1 to 3: "bC"
    Substring from index 3 to end: "d"
    Result: ['bC', 'd'] -> MATCHES!

    Example 2: "Python"
    Lowercases at indices: 1 ('y'), 2 ('t'), 3 ('h'), 4 ('o'), 5 ('n').
    Substring from 1 to 2: "y"
    Substring from 2 to 3: "t"
    Substring from 3 to 4: "h"
    Substring from 4 to 5: "o"
    Substring from 5 to end: "n"
    Result: ['y', 't', 'h', 'o', 'n'] -> MATCHES!

    Example 3: "Programming"
    Lowercases are all letters except 'P'.
    Indices: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11.
    Each substring is just the letter itself because they are adjacent.
    Result: ['r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g'] -> MATCHES!

    Logic:
    1. Find all indices of lowercase letters in the string.
    2. For each index i in the list of indices:
       a. Determine the end of this segment.
       b. The end is the next index in the list, or the end of the string.
       c. Slice the string from current index i to that end index.
       d. Add to result list.
    """

    # Input Validation
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string.")

    # Handle empty string case
    if not input_string:
        return []

    # Step 1: Identify all indices of lowercase letters
    lowercase_indices = []
    for index, character in enumerate(input_string):
        if character.islower():
            lowercase_indices.append(index)

    # Handle case where no lowercase letters exist
    if not lowercase_indices:
        return []

    # Step 2: Build the result list by slicing
    # We iterate through the indices and take segments from 
    # current_index to next_index.
    result_segments = []
    num_lower_indices = len(lowercase_indices)

    for i in range(num_lower_indices):
        start_index = lowercase_indices[i]

        # Determine the end index for the current segment
        if i + 1 < num_lower_indices:
            # The segment ends just before the next lowercase letter
            end_index = lowercase_indices[i + 1]
        else:
            # The last segment goes to the end of the string
            end_index = len(input_string)

        # Extract the substring
        segment = input_string[start_index:end_index]

        # Append to our list
        result_segments.append(segment)

    return result_segments