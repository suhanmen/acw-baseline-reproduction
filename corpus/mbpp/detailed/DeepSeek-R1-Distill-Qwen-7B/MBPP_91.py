assert find_substring(["red", "black", "white", "green", "orange"], "ack") == True
# "black" contains "ack"

assert find_substring(["red", "black", "white", "green", "orange"], "abc") == False
# No string contains "abc"

assert find_substring(["red", "black", "white", "green", "orange"], "ange") == True
# "orange" contains "ange"