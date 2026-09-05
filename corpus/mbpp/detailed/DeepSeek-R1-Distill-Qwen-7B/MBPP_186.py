import re

def check_literals(text, literals):
    # Validate input
    if not literals or not text or not all(isinstance(lit, str) for lit in literals):
        raise ValueError("Invalid input")

    # Escape literals for regex and create pattern
    escaped_literals = [re.escape(lit) for lit in literals]
    pattern = re.join('|', escaped_literals)

    # Search for pattern in text
    match = re.search(pattern, text)

    # Return result based on match
    return 'Matched!' if match else 'Not Matched!'