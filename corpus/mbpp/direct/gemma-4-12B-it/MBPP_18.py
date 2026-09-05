def remove_dirty_chars(first_string: str, second_string: str) -> str:
    """
    Removes characters from the first string that are present in the second string.
    Maintains the original order of characters in the first string.
    """
    dirty_chars = set(second_string)
    return "".join(char for char in first_string if char not in dirty_chars)

if __name__ == "__main__":
    assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'
    assert remove_dirty_chars("digitalindia", "talent") == 'digiidi'
    assert remove_dirty_chars("exoticmiles", "toxic") == 'emles'