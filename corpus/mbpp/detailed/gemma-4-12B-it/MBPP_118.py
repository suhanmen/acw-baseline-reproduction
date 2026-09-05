from typing import List


def string_to_list(input_string: str) -> List[str]:
    """
    Converts a space-separated string into a list of strings.

    The function handles whitespace appropriately, ensuring that multiple 
    spaces are treated as a single delimiter and leading/trailing 
    whitespace is removed.

    Args:
        input_string (str): The string to be converted into a list.

    Returns:
        List[str]: A list of individual words/substrings.

    Raises:
        TypeError: If the input is not a string.
    """
    # Step 1: Input Validation
    # Ensure the input is strictly of the string type to prevent runtime errors
    # in methods like .strip() or .split().
    if not isinstance(input_string, str):
        raise TypeError(f"Expected input of type 'str', but received '{type(input_string).__name__}'")

    # Step 2: Handle Empty or Whitespace-only Input
    # If the string is empty or only contains spaces, the result should be 
    # an empty list, not a list containing an empty string.
    stripped_input = input_string.strip()
    if not stripped_input:
        return []

    # Step 3: Split the string
    # We use .split() without arguments. In Python, this specific 
    # behavior handles any whitespace (spaces, tabs, newlines) as 
    # a delimiter and automatically discards empty strings from the result
    # caused by multiple consecutive spaces.
    result_list = stripped_input.split()

    # Step 4: Defensive check for result
    # While .split() on a non-empty stripped string will return a list,
    # we ensure the output is clearly a list of strings.
    if not isinstance(result_list, list):
        # This part is technically unreachable with standard split(),
        # but included for production-grade defensive programming.
        return []

    return result_list


# Assertions to verify the behavior
if __name__ == "__main__":
    # Test cases provided in the requirements
    assert string_to_list("python programming") == ['python', 'programming']
    assert string_to_list("lists tuples strings") == ['lists', 'tuples', 'strings']
    assert string_to_list("write a program") == ['write', 'a', 'program']

    # Additional edge cases for production-grade robustness
    # 1. Empty string
    assert string_to_list("") == []
    # 2. String with only spaces
    assert string_to_list("   ") == []
    # 3. Single word
    assert string_to_list("hello") == ['hello']
    # 4. Multiple spaces between words
    assert string_to_list("hello    world") == ['hello', 'world']
    # 5. Leading and trailing spaces
    assert string_to_list("  leading and trailing  ") == ['leading', 'and', 'trailing']
    # 6. Tabs and newlines
    assert string_to_list("line1\nline2\ttabbed") == ['line1', 'line2', 'tabbed']