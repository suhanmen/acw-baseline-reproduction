import re

def is_valid_URL(url: str) -> bool:
    """
    Checks if a URL is valid using a regular expression.
    The regex ensures the scheme (http/https) is followed by ://,
    then a domain/hostname without whitespace, and a valid TLD.
    """
    # Regex breakdown:
    # ^https?://        - Starts with http or https followed by ://
    # [^\s/$.?#]        - First char of domain cannot be whitespace or special chars
    # [^\s]*            - Followed by non-whitespace characters
    # \.                - A literal dot
    # [a-zA-Z]{2,}      - A TLD of at least 2 alphabetic characters
    # (\.[a-zA-Z]{2,})? - Optional additional subdomains/TLDs
    # $                 - End of string
    # Note: We specifically ensure no spaces are allowed anywhere in the string.

    pattern = r'^https?://[^\s/$.?#].[^\s]*\.[a-zA-Z]{2,}$'

    # Additional check: Ensure there are no spaces anywhere in the string
    if ' ' in url:
        return False

    return bool(re.match(pattern, url))

if __name__ == "__main__":
    assert is_valid_URL("https://www.google.com") == True
    assert is_valid_URL("https:/www.gmail.com") == False
    assert is_valid_URL("https:// www.redit.com") == False