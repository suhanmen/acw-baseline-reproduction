def remove_Occ(s, char):
    # Find the first occurrence of the character
    first = s.find(char)
    # If the character is not found, return the original string
    if first == -1:
        return s
    # Remove the first occurrence
    modified = s[:first] + s[first+1:]
    # Find the last occurrence of the character in the modified string
    last = modified.rfind(char)
    # If the character is not found in the modified string, return the modified string
    if last == -1:
        return modified
    # Remove the last occurrence
    return modified[:last] + modified[last+1:]

# Test the function with the given examples
assert remove_Occ("hello","l") == "heo"
assert remove_Occ("abcda","a") == "bcd"
assert remove_Occ("PHP","P") == "H"