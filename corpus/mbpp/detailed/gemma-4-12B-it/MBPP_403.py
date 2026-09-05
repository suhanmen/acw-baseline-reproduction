import re
from typing import Optional


def is_valid_URL(url: str) -> bool:
    """
    Validates a URL based on a set of production-grade criteria using regular expressions.

    A valid URL in this context must:
    1. Start with a valid scheme (http, https, ftp).
    2. Follow the scheme with '://'.
    3. Contain a domain name (alphanumeric, hyphens, dots).
    4. Contain a TLD (Top Level Domain).
    5. Not contain whitespaces.
    6. Not have consecutive slashes in the protocol separator or protocol-less parts
       that would invalidate the structure.

    Args:
        url (str): The string to be validated as a URL.

    Returns:
        bool: True if the URL is valid according to the rules, False otherwise.

    Raises:
        TypeError: If the input provided is not a string.
    """
    # Step 1: Input Validation
    # Ensure the input is actually a string type before proceeding.
    if not isinstance(url, str):
        raise TypeError(f"Input must be a string, but received {type(url).__name__}")

    # Step 2: Handle Edge Cases
    # An empty string or a string of only whitespace is immediately invalid.
    if not url or url.isspace():
        return False

    # Step 3: Check for whitespaces
    # A URL should never contain spaces. "https:// www.google.com" is invalid.
    if " " in url:
        return False

    # Step 4: Define the Regex Pattern
    # Explanation of the regex components:
    # ^                          : Start of string
    # (https?|ftp)               : Match 'http', 'https', or 'ftp'
    # ://                        : Match the literal characters '://'
    # (?:[a-zA-Z0-9-]+\.)+       : Match one or more domain labels followed by a dot
    # [a-zA-Z]{2,}               : Match a TLD (at least 2 characters long)
    # (?:[/?#][^\s]*)?           : Optionally match a path, query string, or fragment
    # $                          : End of string

    # Note: We use a specific regex to enforce the '://' and domain structure 
    # strictly as required by the test cases.
    url_pattern = (
        r"^(?:https?|ftp)://"           # Scheme and protocol separator
        r"(?:[a-zA-Z0-9-]+\.)+"         # Domain name parts
        r"[a-zA-Z]{2,}"                  # Top-level domain
        r"(?:/[^ \s]*)?$"                # Optional path (no spaces)
    )

    # Step 5: Perform the Regex Match
    # We use re.fullmatch to ensure the entire string conforms to the pattern.
    try:
        match_result = re.fullmatch(url_pattern, url)

        if match_result is not None:
            return True
        else:
            return False

    except re.error:
        # This handles potential issues with the regex engine itself.
        # In production, this should be logged.
        return False


if __name__ == "__main__":
    # The following assertions verify the requirements provided in the prompt.
    assert is_valid_URL("https://www.google.com") == True
    assert is_valid_URL("https:/www.gmail.com") == False
    assert is_valid_URL("https:// www.redit.com") == False