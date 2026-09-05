from typing import List

def all_prefixes(string: str) -> List[str]:
    """Return list of all prefixes from shortest to longest of the input string."""

    # Validate the input
    if not isinstance(string, str):
        raise ValueError("Input must be a string.")

    # Handle empty string case
    if not string:
        return []

    prefixes = []
    # Generate each prefix by taking the string up to each position
    for i in range(1, len(string) + 1):
        prefixes.append(string[:i])

    return prefixes