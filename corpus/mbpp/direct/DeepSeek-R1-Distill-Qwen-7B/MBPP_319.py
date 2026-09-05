import re

def find_long_word(s):
    pattern = r'\b\w{5}\b'
    matches = re.findall(pattern, s)
    return matches

# Example usage:
print(find_long_word('Please move back to strem'))  # Output: ['strem']
print(find_long_word('4K Ultra HD streaming player'))  # Output: ['Ultra']
print(find_long_word('Streaming Media Player'))  # Output: ['Media'])