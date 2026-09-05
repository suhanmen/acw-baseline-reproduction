import re

def snake_to_camel(snake_str):
    # Use regular expression to find all snake_case words
    # Capitalize each word and join them together
    return ''.join([word.capitalize() for word in re.findall(r'\b\w+?', snake_str)])