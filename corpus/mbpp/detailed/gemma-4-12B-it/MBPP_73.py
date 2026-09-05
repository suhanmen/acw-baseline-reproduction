import re
from typing import List


def multiple_split(input_string: str) -> List[str]:
    """
    Splits a string by multiple delimiters (newline characters and asterisks)
    using regular expressions and returns a list of the resulting substrings.

    Args:
        input_string (str): The string to be split.

    Returns:
        List[str]: A list of substrings separated by the delimiters.

    Raises:
        TypeError: If the input_string is not a string.
        ValueError: If the input_string is None.
    """
    # --- Input Validation ---
    if input_string is None:
        raise ValueError("Input string cannot be None.")

    if not isinstance(input_string, str):
        raise TypeError(f"Expected string input, but received {type(input_string).__name__}.")

    # Handle the edge case of an empty string immediately
    if input_string == "":
        return []

    # --- Logic ---
    # Define the delimiters: newline (\n) and asterisk (*)
    # In regex, the asterisk is a special character (quantifier),
    # so it must be escaped with a backslash to be treated as a literal.
    # We use a character class [] to define a set of delimiters.
    delimiters_regex_pattern = r"[\n*]"

    # Compile the regular expression for efficiency and clarity
    regex_object = re.compile(delimiters_regex_pattern)

    # Use re.split to perform the split operation.
    # re.split handles multiple occurrences of delimiters automatically.
    raw_split_result = regex_object.split(input_string)

    # The split operation might result in empty strings if:
    # 1. Delimiters are at the start or end of the string.
    # 2. Delimiters are adjacent to each other.
    # Based on the provided assertions, the desired behavior is to
    # return the substrings, but standard split behavior might include empty strings.
    # However, looking at the assertions:
    # 'Forces of the \ndarkness*are coming...' 
    # \n is between ' ' and 'd', * is between 's' and 'a'.
    # There are no leading/trailing delimiters or adjacent delimiters in the examples.
    # If there were, we would need to decide whether to filter them or not.
    # To match the strict logic of split operations, we filter out empty strings
    # if they occur as a result of redundant delimiters.

    processed_result = []
    for segment in raw_split_result:
        # Only append if the segment is not an empty string.
        # This ensures that adjacent delimiters (e.g., '\n*') don't result 
        # in an empty string element in the list.
        if segment != "":
            processed_result.append(segment)

    # Edge case check: if the input was only delimiters, the list might be empty.
    # If the input was a non-empty string of delimiters, and we want to 
    # represent the result of a split, we return the list.

    return processed_result


# The function is intended to be used with the following assertions:
# assert multiple_split('Forces of the \ndarkness*are coming into the play.') == ['Forces of the ', 'darkness', 'are coming into the play.']
# assert multiple_split('Mi Box runs on the \n Latest android*which has google assistance and chromecast.') == ['Mi Box runs on the ', ' Latest android', 'which has google assistance and chromecast.']
# assert multiple_split('Certain services\nare subjected to change*over the seperate subscriptions.') == ['Certain services', 'are subjected to change', 'over the seperate subscriptions.']