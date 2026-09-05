import re
from typing import List

def snake_to_camel(snake_str: str) -> str:
    """
    Converts a snake_case string to a PascalCase (UpperCamelCase) string
    using regular expressions.

    The function handles:
    - Standard snake_case (e.g., 'android_tv' -> 'AndroidTv')
    - Leading/trailing underscores
    - Multiple consecutive underscores
    - Empty strings
    - Non-alphanumeric characters (ignored/preserved as per logic)
    """

    # 1. Input Validation
    if not isinstance(snake_str, str):
        raise TypeError(f"Input must be a string, got {type(snake_str).__name__}")

    # Handle empty string case explicitly
    if not snake_str:
        return ""

    # 2. Pre-processing
    # Strip leading and trailing underscores as they don't contribute 
    # to the word structure in standard conversion.
    trimmed_str = snake_str.strip('_')

    if not trimmed_str:
        return ""

    # 3. Regex Identification
    # We look for words separated by underscores. 
    # [a-zA-Z0-9]+ matches sequences of alphanumeric characters.
    # The regex logic essentially finds the parts of the string separated by '_'
    words: List[str] = re.split(r'_+', trimmed_str)

    # Filter out any empty strings that might result from leading/trailing 
    # underscores or multiple consecutive underscores (e.g. 'a__b')
    filtered_words: List[str] = []
    for word in words:
        if word:
            filtered_words.append(word)

    # 4. Transformation
    # We iterate through the filtered words and capitalize each one.
    # capitalize() in Python converts the first character to upper 
    # and the rest to lower. If we want to preserve existing casing 
    # within words (like 'xml_HTTP'), we would use word[0].upper() + word[1:].
    # Based on the assertions ('android_tv' -> 'AndroidTv'), 
    # standard capitalization is the intended behavior.

    camel_parts: List[str] = []
    for word in filtered_words:
        # Ensure we don't crash on single-character words
        if len(word) > 0:
            transformed_word = word.capitalize()
            camel_parts.append(transformed_word)

    # 5. Final Construction
    result_string = "".join(camel_parts)

    return result_string

# Verification logic
if __name__ == "__main__":
    # These match the requirements exactly
    assert snake_to_camel('android_tv') == 'AndroidTv'
    assert snake_to_camel('google_pixel') == 'GooglePixel'
    assert snake_to_camel('apple_watch') == 'AppleWatch'

    # Edge cases
    assert snake_to_camel('') == ''
    assert snake_to_camel('single') == 'Single'
    assert snake_to_camel('multiple__underscores') == 'MultipleUnderscores'
    assert snake_to_camel('_leading_and_trailing_') == 'LeadingAndTrailing'
    assert snake_to_camel('123_numbers') == '123Numbers'