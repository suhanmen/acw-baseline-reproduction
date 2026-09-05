from collections import Counter

def char_frequency(s: str) -> dict:
    return dict(Counter(s))