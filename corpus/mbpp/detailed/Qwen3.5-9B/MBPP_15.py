import string
from typing import List, Tuple, Union

class InvalidInputError(Exception):
    """Custom exception for invalid input types."""
    pass

def _is_lowercase_char(char: str) -> bool:
    """
    Helper function to check if a character is a lowercase letter.

    Args:
        char: A single character string.

    Returns:
        True if the character is a lowercase letter, False otherwise.
    """
    return char.islower() and char.isalpha()

def _split_at_lowercase_indexed(s: str, current_index: int, split_points: List[int]) -> None:
    """
    Helper function to traverse the string and collect indices of lowercase letters.

    This function iterates through the string once, identifying every character 
    that is lowercase, and records its index.

    Args:
        s: The input string to analyze.
        current_index: The starting index for traversal (should start at 0).
        split_points: A list to append the indices of lowercase letters to.
    """
    # Iterate through the string starting from the given index
    # We use range with a step of 1 to cover all characters
    for i in range(current_index, len(s)):
        # Check the character at the current position
        if _is_lowercase_char(s[i]):
            # If it is a lowercase letter, record its index
            split_points.append(i)

def _construct_segments(s: str, split_indices: List[int]) -> List[str]:
    """
    Helper function to split the string using the collected indices.

    The logic is to create substrings starting after each lowercase letter
    and ending at the start of the next lowercase letter (or the end of the string).

    Logic breakdown:
    1. If the string is empty, return an empty list immediately.
    2. If there are no lowercase letters, the entire string is one segment.
    3. Iterate through the list of split indices.
       - Segment 1 starts at index 0 and ends at the first split index (exclusive).
       - Subsequent segments start immediately after the previous split index
         and end at the current split index (exclusive).
    4. The final segment starts after the last split index and goes to the end of the string.

    Args:
        s: The original string.
        split_indices: Sorted list of indices where lowercase letters occur.

    Returns:
        A list of string segments.
    """
    result_segments: List[str] = []
    segment_count = len(s)
    split_count = len(split_indices)

    # Handle empty string case explicitly
    if segment_count == 0:
        return result_segments

    # Handle case with no lowercase letters
    if split_count == 0:
        return [s]

    # Determine the starting position of the first segment
    # According to the problem logic (e.g., "Python" -> ['y', 't'...]), 
    # the segment starts AFTER the first lowercase letter found.
    # Example: "AbCd" -> 'A' is upper. 'b' is lower (index 1). Segment is "bC".
    # Start of first segment is 0? No, looking at "Python" -> ['y', 't', ...]
    # 'P' is index 0 (upper). 'y' is index 1 (lower). Segment "y".
    # Looking at "AbCd" -> ['bC', 'd']. 'A'(0), 'b'(1). First segment starts at 1? 
    # Wait, let's re-read the assertion carefully.
    # assert split_lowerstring("AbCd")==['bC','d']
    # Indices: A(0), b(1), C(2), d(3).
    # Lowercase at 1 and 3.
    # Output: "bC" (indices 1 to 2? No, 1 to 3 exclusive? "bC" is chars at 1,2).
    # Then "d" (char at 3).
    # So segment 1: from index 1 (first lower) to index 3 (next lower) -> s[1:3] = "bC".
    # Segment 2: from index 3 (next lower) to end -> s[3:4] = "d".
    # 
    # Assertion: assert split_lowerstring("Python")==['y', 't', 'h', 'o', 'n']
    # Indices: P(0), y(1), t(2), h(3), o(4), n(5).
    # Lowercase at 1, 2, 3, 4, 5.
    # Segment 1: from 1 to 2 -> s[1:2] = "y".
    # Segment 2: from 2 to 3 -> s[2:3] = "t".
    # ...
    # Segment 5: from 5 to end -> s[5:6] = "n".
    #
    # Conclusion:
    # We start extracting at the index of the first lowercase letter.
    # For each subsequent lowercase letter at index i, we extract the substring
    # from the start of the previous segment's extraction point up to i.
    # Specifically:
    # Start at first_lower_index.
    # Next split is at next_lower_index.
    # Slice is s[first_lower_index : next_lower_index].
    # Then update first_lower_index to next_lower_index.
    # After the last split, slice from last_split_index to end of string.

    start_index = split_indices[0]

    for i in range(1, split_count):
        current_lower_index = split_indices[i]
        next_lower_index = split_indices[i - 1]

        # Extract segment from previous lower index to current lower index
        # Example: split_indices = [1, 3]
        # i=1, current=3, prev=1. Slice s[1:3] -> "bC"
        segment = s[next_lower_index : current_lower_index]
        result_segments.append(segment)

        # Update start_index for the next iteration (though loop logic handles bounds differently)
        # Actually, we need to set the start for the NEXT potential segment.
        # The loop above handles the segment BETWEEN two lowercase letters.
        # Let's refine the loop to be more direct.
        pass # Logic clarified in loop below

    # Let's restart the loop logic based on the pattern:
    # Pattern: Segment = s[i_lower_prev : i_lower_curr]
    # Except for the very first segment which starts at 0? 
    # No, in "AbCd", segment 1 is "bC". Starts at 1.
    # In "Python", segment 1 is "y". Starts at 1.
    # So the first segment ALWAYS starts at split_indices[0].
    # It ends at split_indices[1].
    # The last segment starts at split_indices[-1] and ends at len(s).

    # Re-implementing the loop cleanly:
    # We know the segments are defined by the gaps between lowercase letters.
    # Gap 1: between split_indices[0] and split_indices[1]
    # Gap 2: between split_indices[1] and split_indices[2]
    # ...
    # Gap Last: from split_indices[-1] to end of string

    # We already established split_indices is sorted because we iterated forward.

    # Segment construction:
    # For k from 0 to split_count - 2:
    #   start = split_indices[k]
    #   end = split_indices[k+1]
    #   segment = s[start:end]
    # For the last segment:
    #   start = split_indices[-1]
    #   end = len(s)
    #   segment = s[start:end]

    current_segment_start = split_indices[0]

    # Iterate through all but the last split index
    for i in range(split_count - 1):
        current_segment_end = split_indices[i + 1]
        segment = s[current_segment_start : current_segment_end]
        result_segments.append(segment)

        current_segment_start = current_segment_end

    # Handle the final segment from the last lowercase letter to the end
    final_segment_start = split_indices[-1]
    final_segment = s[final_segment_start : segment_count]
    result_segments.append(final_segment)

    return result_segments

def split_lowerstring(input_str: str) -> List[str]:
    """
    Splits a string at lowercase letters.

    The function identifies all characters that are lowercase letters.
    It then constructs substrings starting immediately after a lowercase letter
    and ending immediately before the next lowercase letter.

    Based on the provided assertions:
    - "AbCd" -> ['bC', 'd']
    - "Python" -> ['y', 't', 'h', 'o', 'n']
    - "Programming" -> ['r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g']

    Logic interpretation:
    The split occurs such that each resulting segment starts with a lowercase letter
    (if the string starts with one) or continues from the previous lowercase letter.
    Essentially, if lowercase letters are at indices [i1, i2, ..., ik],
    the segments are:
    - s[i1 : i2]
    - s[i2 : i3]
    - ...
    - s[ik : end]

    If no lowercase letters are present, the function returns the original string as a single list item?
    Wait, let's check the constraints and assertions again.
    The assertions only show cases with lowercase letters.
    However, the requirement says "Handle edge cases... all-equal elements, boundary values, zero / negative numbers".
    String context usually implies non-negative length. Empty string is a boundary.
    What about a string with NO lowercase letters? e.g. "ABC"?
    If the logic is "split at lowercase", and there are none, we cannot split.
    Does it return the whole string? Or an empty list? Or raise an error?
    Given "split_lowerstring", returning the whole string seems most logical if no split points exist.
    However, looking at the pattern "Python" -> ['y', 't'...], it seems every lowercase char starts a new chunk.
    If there are no lowercase chars, no chunks are started?
    Let's assume if no lowercase exists, it returns [original_string] as a degenerate split, 
    OR it returns []? 
    Actually, looking at the code logic in _construct_segments:
    if split_count == 0: return [s] -> This handles the "no lowercase" case by returning the whole string.

    Input Validation:
    - Must be a string.
    - Cannot be None.
    - Length must be non-negative (implied by being a string).

    Args:
        input_str: The string to be split.

    Returns:
        A list of strings resulting from the split operation.

    Raises:
        InvalidInputError: If input_str is not a string.
    """

    # Validate input type
    if not isinstance(input_str, str):
        raise InvalidInputError(f"Input must be a string, got {type(input_str).__name__}")

    # Validate for None (technically a check for 'str' covers None, but explicit is good for defensive coding)
    if input_str is None:
        raise InvalidInputError("Input cannot be None")

    s = input_str
    length = len(s)

    # Edge case: Empty string
    if length == 0:
        return []

    split_indices: List[int] = []

    # Collect indices of all lowercase letters
    _split_at_lowercase_indexed(s, 0, split_indices)

    # If no lowercase letters found, return the string as a single element (or empty list?)
    # Re-evaluating based on "split at". If nothing to split at, usually returns [original].
    # However, the prompt doesn't explicitly state behavior for "ABC".
    # But the logic "start at first lower, end at next lower" implies if no lowers, no segments.
    # But standard split behavior usually returns [original] if delimiter not found.
    # Let's stick to the logic derived from _construct_segments which returns [s] if split_count is 0.
    # Wait, looking at the problem description again.
    # If I have "ABC", are there any splits? No.
    # Should I return ["ABC"]?
    # Let's look at the assertion for "Python". P is upper. y is lower.
    # If input was "A", no lower. Output?
    # Let's assume the standard interpretation: if no delimiters, return list containing the string.
    # BUT, looking at the helper logic I wrote: `if split_count == 0: return [s]`.
    # Is this consistent?
    # If input is "ABC", split_indices = []. Returns ["ABC"].
    # If input is "abc", split_indices = [0, 1, 2].
    #   i=0: start=0, end=1 -> s[0:1]="a".
    #   i=1: start=1, end=2 -> s[1:2]="b".
    #   Final: start=2, end=3 -> s[2:3]="c".
    #   Result: ["a", "b", "c"].
    # This matches the pattern.

    if len