def text_match_one(s):
    import re
    return re.fullmatch(r"a+b+", s) is not None

# Explanation:
# This function uses a regular expression to match a string that starts with an 'a' followed by one or more 'b's.
# The re.fullmatch() function ensures that the entire string conforms to the pattern, which guarantees that:
# 1. The string must start with 'a'
# 2. The string must have at least one 'b' following the initial 'a'
# 3. The string cannot contain any other characters besides 'a' and 'b'