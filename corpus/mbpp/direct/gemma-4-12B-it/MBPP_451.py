import re

def remove_whitespaces(text: str) -> str:
    """
    Removes all whitespaces from the given string using regex.
    """
    return re.sub(r'\s+', '', text)

if __name__ == "__main__":
    assert remove_whitespaces(' Google    Flutter ') == 'GoogleFlutter'
    assert remove_whitespaces(' Google    Dart ') == 'GoogleDart'
    assert remove_whitespaces(' iOS    Swift ') == 'iOSSwift'