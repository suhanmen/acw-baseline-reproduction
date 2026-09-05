assert is_valid_URL("https://www.google.com") == True
assert is_valid_URL("https:/www.gmail.com") == False
assert is_valid_URL("https:// www.redit.com") == False