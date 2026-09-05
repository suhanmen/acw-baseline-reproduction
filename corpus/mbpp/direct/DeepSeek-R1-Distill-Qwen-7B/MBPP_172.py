def count_occurance(s):
    count = 0
    for i in range(len(s) - 2):
        if s[i] == 's' and s[i+1] == 't' and s[i+2] == 'd':
            count += 1
    return count

# Example usage
print(count_occurance("letstdlenstdporstd"))  # Output: 3
print(count_occurance("truststdsolensporsd"))  # Output: 1
print(count_occurance("makestdsostdworthit"))  # Output: 2