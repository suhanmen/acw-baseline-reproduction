import re

def is_valid_URL(url):
    """
    Check if the given URL is valid using regex.
    """
    # Handle empty input
    if not url:
        return False

    # Split the URL into scheme and domain part
    try:
        scheme, rest = url.split('://')
    except ValueError:
        # Invalid URL format
        return False

    # Check if scheme is valid
    valid_schemes = {'http', 'https', 'ftp', 'ftps', 'data'}
    if scheme not in valid_schemes:
        return False

    # Split the domain part into local part and path
    try:
        local_part, path = rest.split('/')
    except ValueError:
        # No path part in URL
        return False

    # Regex pattern for domain part
    domain_pattern = r'^[a-zA-Z0-9-._%!?]*\.'  # Subdomain and TLD

    # Split into subdomain and top-level domain
    subdomains = local_part.split('.')

    # Check the number of subdomains
    if len(subdomains) < 2:
        return False

    # Check each subdomain and TLD
    for subdomain in subdomains[:-1]:
        if not re.match(r'^[a-zA-Z0-9-._%!?]*$', subdomain):
            return False

    # Check TLD
    tld = subdomains[-1]
    if not re.match(r'^[a-zA-Z]{2,}$', tld):
        return False

    # Regex pattern for path part
    path_pattern = r'^(/.*$)|^(/?[?#]*$)|^(/[-=_#&:\/%?\\?*;:’“”\'"]*)$'

    if not re.match(path_pattern, path):
        return False

    return True

# Test cases
assert is_valid_URL("https://www.google.com") == True
assert is_valid_URL("https:/www.gmail.com") == False
assert is_valid_URL("https:// www.redit.com") == False