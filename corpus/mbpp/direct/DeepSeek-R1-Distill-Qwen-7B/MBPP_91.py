def find_substring(lst, s):
    for word in lst:
        if s in word:
            return True
    return False

assert find_substring(["red", "black", "white", "green", "orange"], "ack") == True
assert find_substring(["red", "black", "white", "green", "orange"], "abc") == False
assert find_substring(["red", "black", "white", "green", "orange"], "ange") == True