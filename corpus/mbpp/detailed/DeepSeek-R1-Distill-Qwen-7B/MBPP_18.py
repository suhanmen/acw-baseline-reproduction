def remove_dirty_chars(s1, s2):
    # Handle cases where s2 is empty or s1 is empty
    if not s2:
        return s1
    if not s1:
        return ""

    result = []
    for char in s1:
        if char not in s2:
            result.append(char)
    return ''.join(result)

# Test the function with the provided examples
assert remove_dirty_chars("probasscurve", "pros") == 'bacuve', "Test 1 failed"
assert remove_dirty_chars("digitalindia", "talent") == 'digiidi', "Test 2 failed"
assert remove_dirty_chars("exoticmiles", "toxic") == 'emles', "Test 3 failed"

print("All tests passed!")