def validate(number):
    digits = str(number)
    frequency = {}
    for d in digits:
        frequency[d] = frequency.get(d, 0) + 1
    for d in digits:
        if frequency[d] > int(d):
            return False
    return True

# Test cases
assert validate(1234) == True
assert validate(51241) == False
assert validate(321) == True