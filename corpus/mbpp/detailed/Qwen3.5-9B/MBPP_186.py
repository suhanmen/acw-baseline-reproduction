import re
from typing import List, Union

def _validate_search_patterns(patterns: List[str]) -> None:
    """
    Validates that the provided list of search patterns is well-formed.

    Rules:
    1. The list must not be None.
    2. Every element in the list must be a string.
    3. Every element must not be an empty string.

    Raises:
        TypeError: If the input is not a list or contains non-string elements.
        ValueError: If the list is empty or contains empty strings.
    """
    if patterns is None:
        raise TypeError("The list of patterns cannot be None.")

    if not isinstance(patterns, list):
        raise TypeError("The input must be a list of strings.")

    if len(patterns) == 0:
        raise ValueError("The list of patterns cannot be empty.")

    for index, pattern in enumerate(patterns):
        if not isinstance(pattern, str):
            raise TypeError(f"Pattern at index {index} is not a string.")
        if len(pattern) == 0:
            raise ValueError(f"Pattern at index {index} cannot be an empty string.")

def _compile_patterns(patterns: List[str]) -> List[re.Pattern]:
    """
    Compiles each string pattern into a compiled regex pattern object.

    This step ensures that invalid regex syntax will be caught and raised
    as an error during compilation, rather than at runtime during search.

    Args:
        patterns: A list of valid string patterns to compile.

    Returns:
        A list of compiled regex pattern objects.

    Raises:
        re.error: If any pattern contains invalid regex syntax.
    """
    compiled_list = []
    for index, pattern_string in enumerate(patterns):
        try:
            compiled_pattern = re.compile(pattern_string)
        except re.error as regex_error:
            raise re.error(
                f"Invalid regular expression syntax at index {index}: {regex_error.msg}"
            ) from regex_error
        compiled_list.append(compiled_pattern)
    return compiled_list

def _search_all_patterns(text: str, compiled_patterns: List[re.Pattern]) -> bool:
    """
    Iterates through the compiled patterns and checks if ANY of them match the text.

    The search returns True immediately upon finding the first match to ensure
    efficiency. It checks for a match anywhere within the text string.

    Args:
        text: The target string to search within.
        compiled_patterns: A list of pre-compiled regex patterns.

    Returns:
        True if at least one pattern matches, False otherwise.
    """
    for pattern in compiled_patterns:
        if pattern.search(text) is not None:
            return True
    return False

def _determine_result_string(match_found: bool) -> str:
    """
    Returns the specific result string based on whether a match was found.

    Args:
        match_found: Boolean indicating if a pattern matched the text.

    Returns:
        "Matched!" if match_found is True, "Not Matched!" otherwise.
    """
    if match_found:
        return "Matched!"
    return "Not Matched!"

def check_literals(text: str, patterns: List[str]) -> str:
    """
    Searches for any of the provided literal strings within a given text using regex.

    This function performs defensive programming by validating inputs, compiling
    patterns safely, and explicitly handling the logic flow to ensure correctness
    across all edge cases (empty text, no matches, multiple matches, etc.).

    Args:
        text: The main string in which to search for patterns.
        patterns: A list of string patterns to search for within 'text'.

    Returns:
        "Matched!" if any pattern in the list is found within 'text'.
        "Not Matched!" if none of the patterns are found.

    Raises:
        TypeError: If 'patterns' is None, not a list, or contains non-string elements.
        ValueError: If 'patterns' is empty or contains empty strings.
        re.error: If any pattern contains invalid regular expression syntax.
    """

    # Step 1: Explicitly handle the case where the input text is None or not a string.
    # While the problem implies valid text, robust code handles degenerate cases.
    if not isinstance(text, str):
        raise TypeError("The 'text' argument must be a string.")

    # Step 2: Validate the patterns list to ensure safety before processing.
    _validate_search_patterns(patterns)

    # Step 3: Compile all regex patterns. This moves syntax checking to initialization.
    compiled_patterns = _compile_patterns(patterns)

    # Step 4: Perform the search logic.
    match_found = _search_all_patterns(text, compiled_patterns)

    # Step 5: Determine and return the final result string.
    return _determine_result_string(match_found)