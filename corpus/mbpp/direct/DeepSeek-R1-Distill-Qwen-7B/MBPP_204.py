def count(string, character):
    count = 0
    for char in string:
        if char == character:
            count += 1
    return count

assert count("abcc", "c") == 2
assert count("ababca", "a") == 3
assert count("mnmm0pm", "m") == 4