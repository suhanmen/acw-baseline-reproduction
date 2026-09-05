def _validate_search_terms(search_terms):
    """
    Validates the 'search_terms' argument.

    Rules:
    1. It must not be None.
    2. It must be a list or a tuple.
    3. Every element within the list/tuple must be a string.

    Raises:
        TypeError: If the container is invalid or contains non-string elements.
    """
    if search_terms is None:
        raise TypeError("search_terms cannot be None.")

    # Accept list or tuple, reject other iterables like sets or generators
    if not isinstance(search_terms, (list, tuple)):
        raise TypeError(
            f"search_terms must be a list or tuple, but got '{type(search_terms).__name__}'."
        )

    # Check each element inside
    for index, term in enumerate(search_terms):
        if not isinstance(term, str):
            raise TypeError(
                f"All search terms must be strings. Found non-string at index {index}: "
                f"'{term}' (type: {type(term).__name__})."
            )


def _validate_search_text(search_text):
    """
    Validates the 'search_text' argument.

    Rules:
    1. It must not be None.
    2. It must be a string.

    Raises:
        TypeError: If the text is invalid.
    """
    if search_text is None:
        raise TypeError("search_text cannot be None.")

    if not isinstance(search_text, str):
        raise TypeError(
            f"search_text must be a string, but got '{type(search_text).__name__}'."
        )


def _find_literal_in_text(literal, text):
    """
    Checks if a specific 'literal' exists within the 'text'.

    This function uses a case-sensitive substring search.
    It returns True if found, False otherwise.

    Args:
        literal (str): The string to search for.
        text (str): The text within which to search.

    Returns:
        bool: True if 'literal' is found in 'text', False otherwise.
    """
    # Explicit check for empty literal string
    # An empty string is technically a substring of any string,
    # but in the context of "searching for literals", it usually implies
    # we are looking for a non-empty token. However, standard string methods
    # treat '' as present. Based on standard library behavior (''.find('') == 0),
    # we return True if the literal is empty, as it technically exists in the text.
    if literal == "":
        return True

    # Standard substring search
    # Python's 'in' operator returns True if 'literal' is a substring of 'text'.
    return literal in text


def string_literals(search_terms, search_text):
    """
    Searches for specific literal strings within a target text.

    The function iterates through the provided list of search terms.
    If ANY of the search terms are found within the target text, 
    it returns the string "Matched!".
    If NONE of the search terms are found, it returns the string "Not Matched!".

    Note: The function does not return the specific term that was matched,
    nor does it distinguish between matches and non-matches beyond the 
    binary "Matched!" vs "Not Matched!" output.

    Args:
        search_terms (list or tuple): A collection of string literals to search for.
        search_text (str): The text in which to perform the search.

    Returns:
        str: "Matched!" if any term is found, "Not Matched!" otherwise.

    Raises:
        TypeError: If input arguments are invalid types or contain invalid data.
    """
    # Step 1: Validate inputs strictly before processing
    _validate_search_terms(search_terms)
    _validate_search_text(search_text)

    # Step 2: Iterate through each search term explicitly
    # We use a flag to track if any match is found. This avoids short-circuiting
    # logic that might hide the state of other variables in more complex scenarios.
    any_match_found = False

    # Initialize a list to hold the results of individual searches for clarity
    individual_matches = []

    for term in search_terms:
        # Perform the lookup for the current term
        is_present = _find_literal_in_text(term, search_text)

        # Record the result of this specific search
        individual_matches.append({
            "term": term,
            "found": is_present
        })

        # Update the global match flag if this term was found
        if is_present:
            any_match_found = True

            # Optional: We could break here for efficiency, but the requirements
            # ask for explicit steps and defensive coding. Breaking is a valid 
            # explicit control flow decision for optimization. 
            # Here, we will NOT break to fully inspect the data structure logic
            # as per the "spell out steps" requirement, though in production
            # a break would likely be preferred. We proceed to the next term.

    # Step 3: Determine the final outcome string based on the flag
    if any_match_found:
        result_message = "Matched!"
    else:
        result_message = "Not Matched!"

    # Step 4: Return the final result
    return result_message


# The following block demonstrates that the code is complete and runnable
# by verifying the exact assertions provided in the problem statement.
if __name__ == "__main__":
    # Assertion 1
    try:
        result1 = string_literals(['language'], 'python language')
        expected1 = ('Matched!',)
        if result1 != expected1[0]:
            raise AssertionError(f"Test 1 Failed: Expected {expected1[0]}, got {result1}")
        print(f"Test 1 PASSED: {result1}")
    except Exception as e:
        print(f"Test 1 Exception: {e}")

    # Assertion 2
    try:
        result2 = string_literals(['program'], 'python language')
        expected2 = ('Not Matched!',)
        if result2 != expected2[0]:
            raise AssertionError(f"Test 2 Failed: Expected {expected2[0]}, got {result2}")
        print(f"Test 2 PASSED: {result2}")
    except Exception as e:
        print(f"Test 2 Exception: {e}")

    # Assertion 3
    try:
        result3 = string_literals(['python'], 'programming language')
        expected3 = ('Not Matched!',)
        if result3 != expected3[0]:
            raise AssertionError(f"Test 3 Failed: Expected {expected3[0]}, got {result3}")
        print(f"Test 3 PASSED: {result3}")
    except Exception as e:
        print(f"Test 3 Exception: {e}")