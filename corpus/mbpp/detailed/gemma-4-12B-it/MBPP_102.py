from typing import List

def snake_to_camel(snake_str: str) -> str:
    """
    Converts a snake_case string to a PascalCase (UpperCamelCase) string.

    Example:
        'python_program' -> 'PythonProgram'

    Args:
        snake_str (str): The string in snake_case format.

    Returns:
        str: The converted string in PascalCase.

    Raises:
        TypeError: If the input is not a string.
        ValueError: If the input string is empty or contains invalid characters.
    """
    # --- Input Validation ---
    if not isinstance(snake_str, str):
        raise TypeError(f"Input must be a string, received {type(snake_str).__name__}")

    # Handle empty string case
    if not snake_str:
        raise ValueError("Input string cannot be empty")

    # --- Processing ---
    # Split the string by underscores to isolate individual words
    # Filter out empty strings in case of double underscores (e.g., 'python__program')
    raw_words: List[str] = snake_str.split('_')

    # Remove empty strings from the list (handling cases like '__leading' or 'trailing__')
    filtered_words: List[str] = []
    for word in raw_words:
        if word:
            filtered_words.append(word)

    # Handle cases where the string is just underscores (e.g., "___")
    if not filtered_words:
        raise ValueError("Input string must contain at least one alphanumeric word")

    # Transform each word into its PascalCase form
    # PascalCase means the first letter is uppercase and the rest are lowercase.
    # We assume standard snake_case is lowercase, but we call .lower() 
    # and .capitalize() to be defensive against mixed cases.
    processed_parts: List[str] = []
    for word in filtered_words:
        # Ensure we handle single characters correctly
        # .capitalize() makes first char upper and the rest lower
        capitalized_word = word.capitalize()
        processed_parts.append(capitalized_word)

    # Join the parts back together
    result_string = "".join(processed_parts)

    return result_string

if __name__ == "__main__":
    # The assertions provided in the prompt:
    # Note: The prompt showed ('PythonLanguage') as a tuple in the second/third 
    # assertions, but the context implies returning a string. 
    # PascalCase generally refers to a string.

    assert snake_to_camel('python_program') == 'PythonProgram'
    assert snake_to_camel('python_language') == 'PythonLanguage'
    assert snake_to_camel('programming_language') == 'ProgrammingLanguage'