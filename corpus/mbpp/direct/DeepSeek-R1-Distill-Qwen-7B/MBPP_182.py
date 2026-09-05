import re

def find_character(s):
    uppercase = []
    lowercase = []
    special = []
    numeric = []

    for char in s:
        if char.isupper():
            uppercase.append(char)
        elif char.islower():
            lowercase.append(char)
        elif char.isdigit():
            numeric.append(char)
        elif not char.isalnum():
            special.append(char)

    return (uppercase, lowercase, special, numeric)

# Test the function with the given examples
assert find_character("ThisIsGeeksforGeeks") == (['T', 'I', 'G', 'G'], ['h', 'i', 's', 's', 'e', 'e', 'k', 's', 'f', 'o', 'r', 'e', 'e', 'k', 's'], [], [])
assert find_character("Hithere2") == (['H'], ['i', 't', 'h', 'e', 'r', 'e'], ['2'], [])
assert find_character("HeyFolks32") == (['H', 'F'], ['e', 'y', 'o', 'l', 'k', 's'], ['3', '2'], [])