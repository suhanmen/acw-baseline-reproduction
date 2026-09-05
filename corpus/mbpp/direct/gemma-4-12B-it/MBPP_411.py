import re

def snake_to_camel(snake_str: str) -> str:
    """
    Converts a snake_case string to PascalCase (UpperCamelCase) 
    using regular expressions.
    """
    # Find all words separated by underscores
    words = re.split(r'_', snake_str)
    # Capitalize the first letter of each word and join them
    return "".join(word.capitalize() for word in words if word)