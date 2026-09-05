import re
from typing import List

def match(input_string: str) -> str:
    """
    Identifies if the given string contains at least one sequence consisting 
    of exactly one uppercase letter followed by one or more lowercase letters.

    Args:
        input_string (str): The string to search.

    Returns:
        str: 'Yes' if a match is found, 'No' otherwise.
    """
    # 1. Validate the input type
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string.")

    # 2. Handle empty input explicitly
    if not input_string:
        return "No"

    # 3. Define the regex pattern.
    # [A-Z] matches exactly one uppercase letter.
    # [a-z]+ matches one or more lowercase letters.
    # We use a raw string for the regex to handle potential escape sequences correctly.
    pattern_string = r"[A-Z][a-z]+"

    try:
        # 4. Compile the regex pattern.
        # Compiling provides a slight performance boost and allows for better error checking.
        pattern_object = re.compile(pattern_string)

        # 5. Perform the search.
        # re.search looks for the pattern anywhere in the string.
        # findall is also an option, but search is more efficient for a "Yes/No" check.
        match_result = pattern_object.search(input_string)

        # 6. Evaluate the result.
        if match_result is not None:
            # A match was found (e.g., 'G' followed by 'eeks' in 'Geeks')
            return "Yes"
        else:
            # No sequence of Uppercase + lowercase(s) was found.
            return "No"

    except re.error as e:
        # Handle potential regex compilation errors (though unlikely with a static pattern)
        print(f"Regex Error: {e}")
        return "No"

if __name__ == "__main__":
    # Assertions provided in the problem description
    assert match("Geeks") == 'Yes'
    assert match("geeksforGeeks") == 'Yes'
    assert match("geeks") == 'No'

    # Additional edge cases for defensive programming:
    assert match("A") == 'No'            # Only one uppercase, no lowercase
    assert match("aA") == 'No'           # Lowercase then Uppercase
    assert match("ABC") == 'No'          # All Uppercase
    assert match("abc") == 'No'          # All Lowercase
    assert match("A123") == 'No'         # Uppercase followed by numbers
    assert match("A_b") == 'No'          # Uppercase followed by underscore then lowercase
    assert match("123Geeks") == 'Yes'    # Match preceded by numbers
    assert match("MultipleWords") == 'Yes' # Multiple matches