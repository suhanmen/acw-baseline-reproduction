def vowels_count(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    count = 0
    for i, char in enumerate(s):
        if char.lower() in vowels:
            count += 1
    # Check if 'y' is the last character
    if len(s) > 0 and s[-1].lower() == 'y':
        count += 1
    return count