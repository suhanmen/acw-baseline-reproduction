def reverse_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    vowel_indices = []
    for i, c in enumerate(s):
        if c in vowels:
            vowel_indices.append(i)
    reversed_vowels = [s[i] for i in vowel_indices][::-1]
    reversed_indices = vowel_indices[::-1]
    result = list(s)
    for i, c in enumerate(result):
        if i in reversed_indices:
            result[i] = reversed_vowels[i]
    return ''.join(result)

# Test the function with provided examples
assert reverse_vowels("Python") == "Python"
assert reverse_vowels("USA") == "ASU"
assert reverse_vowels("ab") == "ab"