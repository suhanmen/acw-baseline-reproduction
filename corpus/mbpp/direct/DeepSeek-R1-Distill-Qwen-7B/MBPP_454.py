def text_match_wordz(text):
    import re
    pattern = r"\b(z)\b"
    match = re.search(pattern, text)
    if match:
        return ('Found a match!')
    else:
        return ('Not matched!')