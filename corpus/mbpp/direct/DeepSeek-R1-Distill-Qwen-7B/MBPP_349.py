assert check("01010101010") == "Yes"  # Returns "Yes" because it's a binary string.
assert check("name0") == "No"       # Returns "No" because it contains non-binary characters.
assert check("101") == "Yes"        # Returns "Yes" because it's a binary string.