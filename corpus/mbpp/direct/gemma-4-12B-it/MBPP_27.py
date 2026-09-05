def remove(strings):
    """
    Removes all digits from a list of strings.
    """
    result = []
    for s in strings:
        # Join characters that are not digits
        cleaned = "".join(char for char in s if not char.isdigit())
        result.append(cleaned)
    return result

if __name__ == "__main__":
    assert remove(['4words', '3letters', '4digits']) == ['words', 'letters', 'digits']
    assert remove(['28Jan','12Jan','11Jan']) == ['Jan','Jan','Jan']
    assert remove(['wonder1','wonder2','wonder3']) == ['wonder','wonder','wonder']