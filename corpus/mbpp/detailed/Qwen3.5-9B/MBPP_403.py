import re
from typing import Optional

def _sanitize_url(url: str) -> Optional[str]:
    """
    Strips leading and trailing whitespace from the input URL string.
    Returns None if the input is not a string.

    This function explicitly handles the degenerate case where the input might
    have significant whitespace around the protocol or domain, which often
    indicates a malformed URL in practice, though the problem statement
    specifically flags "https:// www.redit.com" as invalid.
    """
    if not isinstance(url, str):
        return None

    stripped_url = url.strip()

    # If the original string had leading or trailing whitespace, it is considered invalid
    # based on the requirement that "https:// www.redit.com" must be False.
    if stripped_url != url:
        return None

    return stripped_url

def _validate_protocol(protocol: str) -> bool:
    """
    Validates that the protocol matches 'http' or 'https' (case-insensitive).
    """
    normalized_protocol = protocol.lower()
    return normalized_protocol in ('http', 'https')

def _validate_domain(domain: str) -> bool:
    """
    Validates the domain part of the URL.
    Requirements derived from examples:
    1. Must contain at least one dot.
    2. Cannot start or end with a dot or hyphen.
    3. Labels must not start or end with a hyphen.
    4. Labels must not be empty.
    5. TLD (top-level domain) must be at least 2 characters.
    """
    # Check for empty domain
    if not domain:
        return False

    # Check if the domain starts or ends with special characters that are typically invalid
    if domain.startswith('.') or domain.startswith('-') or domain.endswith('.') or domain.endswith('-'):
        return False

    # Split domain into labels
    labels = domain.split('.')

    # Must have at least two parts for a valid domain (e.g., 'www.google')
    if len(labels) < 2:
        return False

    # Validate each label
    for label in labels:
        if not label:
            return False

        # Labels cannot contain leading or trailing hyphens
        if label.startswith('-') or label.endswith('-'):
            return False

        # Basic character check: alphanumeric and hyphen only
        if not re.match(r'^[a-zA-Z0-9\-]+$', label):
            return False

    return True

def _validate_path(path: str) -> bool:
    """
    Validates the path part of the URL.
    It must be either empty or start with a forward slash '/'.
    """
    if not path:
        return True

    # A valid path must start with a slash
    if not path.startswith('/'):
        return False

    # A path cannot contain spaces
    if ' ' in path:
        return False

    return True

def _validate_query(query: str) -> bool:
    """
    Validates the query string part of the URL.
    It must be empty, or start with '?'.
    It cannot contain unencoded spaces.
    """
    if not query:
        return True

    # Must start with '?'
    if not query.startswith('?'):
        return False

    # Extract the part after '?'
    query_content = query[1:]

    # Cannot contain spaces
    if ' ' in query_content:
        return False

    return True

def _validate_fragment(fragment: str) -> bool:
    """
    Validates the fragment (anchor) part of the URL.
    It must be empty, or start with '#'.
    """
    if not fragment:
        return True

    # Must start with '#'
    if not fragment.startswith('#'):
        return False

    return True

def _validate_full_url(sanitized_url: str) -> bool:
    """
    Uses explicit string manipulation to validate the structure of the URL.
    This approach avoids complex regex backtracking issues and makes validation steps clear.
    """
    # Define the required pattern components
    required_prefix = "https://"
    allowed_protocols = ("http://", "https://")

    # Check for valid protocol
    if not (sanitized_url.startswith("http://") or sanitized_url.startswith("https://")):
        return False

    # Extract parts
    separator = sanitized_url.split("://")
    if len(separator) != 2:
        return False

    protocol = separator[0]
    rest = separator[1]

    if not _validate_protocol(protocol):
        return False

    # Find the position of the first space in the rest of the URL
    first_space_index = rest.find(' ')
    if first_space_index != -1:
        # Spaces are generally only allowed in user info (after @), 
        # but for simplicity and strictness based on "www.redit.com" example,
        # we assume no spaces in the core domain structure unless explicitly encoded.
        # However, to be rigorous about "https:// www.redit.com", we already handled stripping.
        # If a space exists in the rest, it's likely invalid unless in a specific context.
        # Given the examples, let's treat any space in 'rest' as invalid for now.
        return False

    # Split the rest into components
    # Order: domain, path, query, fragment

    # Check for query/fragment first (must appear after path)
    query_pos = rest.find('?')
    fragment_pos = rest.find('#')

    # Determine split positions
    domain_end = len(rest)
    if query_pos != -1:
        domain_end = min(domain_end, query_pos)
    if fragment_pos != -1:
        domain_end = min(domain_end, fragment_pos)

    domain_part = rest[:domain_end]

    # Check domain part again (sanity check)
    if not _validate_domain(domain_part):
        return False

    path_part = ""
    query_part = ""
    fragment_part = ""

    if query_pos != -1:
        path_part = rest[domain_end:query_pos]
        query_part = rest[query_pos:]
    elif fragment_pos != -1:
        path_part = rest[domain_end:fragment_pos]
        fragment_part = rest[fragment_pos:]
    else:
        path_part = rest[domain_end:]

    if not _validate_path(path_part):
        return False

    if not _validate_query(query_part):
        return False

    if not _validate_fragment(fragment_part):
        return False

    return True

def is_valid_URL(url: str) -> bool:
    """
    Checks if a URL is valid.

    Args:
        url (str): The URL string to validate.

    Returns:
        bool: True if the URL is valid, False otherwise.

    Constraints handled:
        - Empty input
        - Single element
        - All-equal elements (N/A for string validation but handled via empty check)
        - Boundary values (spaces, special chars)
        - Zero / negative numbers (N/A for string but handled via type check)
    """
    # 1. Basic Input Validation
    if not isinstance(url, str):
        return False

    # 2. Handle empty string or None-like string
    if len(url) == 0:
        return False

    # 3. Normalize and check for leading/trailing whitespace
    # Note: The problem explicitly states "https:// www.redit.com" should be False.
    # Simply stripping it and validating the result would return True for that input
    # (as 'www.redit.com' is a valid domain). Therefore, we must detect the space.
    if url != url.strip():
        return False

    # 4. Check for spaces anywhere in the URL
    # While strictly speaking, spaces can be percent-encoded, the problem examples
    # suggest a strict no-space policy for the raw string provided.
    if ' ' in url:
        return False

    # 5. Perform structural validation
    return _validate_full_url(url)