def remove_dirty_chars(s: str, chars_to_remove: str) -> str:
    remove_set = set(chars_to_remove)
    return ''.join(c for c in s if c not in remove_set)