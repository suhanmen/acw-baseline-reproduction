import re

def find_char(text):
    # The regex \b\w{3,5}\b matches words (alphanumeric sequences) 
    # that are between 3 and 5 characters long inclusive, 
    # ensuring they are bounded by word boundaries.
    # Note: \w matches letters, digits, and underscores.
    # Based on the assertions, it treats uppercase/lowercase and 
    # mixed characters as words.
    pattern = r'\b\w{3,5}\b'
    return re.findall(pattern, text)

if __name__ == "__main__":
    assert find_char('For the four consumer complaints contact manager AKR reddy') == ['For', 'the', 'four', 'AKR', 'reddy']
    assert find_char('Certain service are subject to change MSR') == ['are', 'MSR']
    assert find_char('Third party legal desclaimers') == ['Third', 'party', 'legal']