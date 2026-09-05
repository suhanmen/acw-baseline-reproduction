import re

def is_valid_URL(url: str) -> bool:
    pattern = r'^https?://(www\.)?([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,6}(/\S*)?$'
    return bool(re.match(pattern, url))