import re

def find_char(text):
    pattern = r'\b\w{3,5}\b'
    matches = re.findall(pattern, text)
    return matches

# Example usage:
# print(find_char('For the four consumer complaints contact manager AKR reddy'))  # Output: ['For', 'the', 'four', 'AKR', 'reddy']
# print(find_char('Certain service are subject to change MSR'))  # Output: ['are', 'MSR']
# print(find_char('Third party legal desclaimers'))  # Output: ['Third', 'party', 'legal']