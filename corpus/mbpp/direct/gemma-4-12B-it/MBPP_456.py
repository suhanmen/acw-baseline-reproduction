def reverse_string_list(strings: list[str]) -> list[str]:
    """
    Reverses each string in a given list of strings.

    Args:
        strings: A list of strings to be reversed.

    Returns:
        A new list where each string from the input list is reversed.
    """
    return [s[::-1] for s in strings]

if __name__ == "__main__":
    assert reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black']) == ['deR', 'neerG', 'eulB', 'etihW', 'kcalB']
    assert reverse_string_list(['john','amal','joel','george']) == ['nhoj','lama','leoj','egroeg']
    assert reverse_string_list(['jack','john','mary']) == ['kcaj','nhoj','yram']