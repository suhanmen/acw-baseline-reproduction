def firstRepeatedChar(s):
    char_counts = {}
    for char in s:
        if char in char_counts:
            return char
        char_counts[char] = 1
    return None

# Test the function with the examples
print(firstRepeatedChar("Google"))  # Should return "o"
print(firstRepeatedChar("data"))   # Should return "a"
print(firstRepeatedChar("python")) # Should return None