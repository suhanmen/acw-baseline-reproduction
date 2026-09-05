import string
import re

def text_match_word(text: str) -> str:
    """
    Matches if the word 'python' appears at the end of the input string,
    optionally followed by punctuation.

    Args:
        text (str): The input string to check.

    Returns:
        str: 'Found a match!' if the criteria are met, 'Not matched!' otherwise.
    """
    # Step 1: Basic input validation
    if not isinstance(text, str):
        # In a production environment, we might raise a TypeError,
        # but for this logic flow, we treat invalid types as non-matches.
        return "Not matched!"

    # Step 2: Handle empty string or whitespace-only strings
    # We trim whitespace to handle cases like "python.  "
    stripped_text = text.strip()
    if not stripped_text:
        return "Not matched!"

    # Step 3: Define the target word
    target_word = "python"

    # Step 4: Identify punctuation
    # We want to allow trailing punctuation, but ensure 'python' is the core word.
    # We use a regex approach to ensure the word is at the very end.

    # Regex Explanation:
    # \bpython   -> Match the word 'python' at a word boundary.
    # [.,!?!\s]* -> Followed by zero or more punctuation marks or spaces.
    # $           -> Ensure this happens at the end of the string.
    # Using \b ensures we don't match "cython" or "pythonic".

    # We define a pattern that looks for 'python' followed by 
    # only punctuation characters at the end of the string.
    # \w* is ignored because we want the word to be 'python' specifically.

    # pattern:
    # ^.*          -> Match anything from the start
    # \bpython     -> Match the exact word 'python'
    # [.,!?;:]*    -> Match optional trailing punctuation
    # \s*          -> Match optional trailing whitespace
    # $             -> End of string

    pattern = r"\bpython[.,!?;:]*\s*$"

    # We check if the pattern matches the end of the input string.
    # We use re.search because we don't care what comes before 'python'.
    match = re.search(pattern, text)

    if match:
        return "Found a match!"
    else:
        return "Not matched!"

# The logic is strictly defined to pass the provided assertions:
# "python." -> Found a match! (Ends with python + .)
# "  lang  ." -> Not matched! (Ends with lang, not python)