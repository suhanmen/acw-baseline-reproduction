import re

def snake_to_camel(snake_case: str) -> str:
    return re.sub(r'_(\w)', lambda m: m.group(1).upper(), snake_case).capitalize()