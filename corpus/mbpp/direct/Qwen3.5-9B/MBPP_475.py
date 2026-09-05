from collections import Counter

def sort_counter(c: dict) -> list:
    """Sort a dictionary by its values in descending order and return a list of (key, value) tuples."""
    return sorted(c.items(), key=lambda item: item[1], reverse=True)