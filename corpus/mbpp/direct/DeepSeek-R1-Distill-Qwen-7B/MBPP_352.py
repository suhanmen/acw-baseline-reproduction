def unique_Characters(s):
    return len(s) == len(set(s))

# Explanation:
# This function works by converting the string into a set, which automatically removes duplicates.
# If the length of the set (which contains unique characters) is equal to the length of the original string,
# it means all characters were unique. Otherwise, there were duplicates.