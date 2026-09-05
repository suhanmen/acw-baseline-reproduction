def concatenate_strings(tup1, tup2):
    # Handle the case where either tuple is empty
    if not tup1 or not tup2:
        return ()

    # Determine the length of the longer tuple
    max_length = max(len(tup1), len(tup2))

    # Create a list to store the resulting concatenated tuples
    result = []

    # Iterate through each index up to the maximum length
    for i in range(max_length):
        # Concatenate corresponding elements from each tuple
        # If an element doesn't exist, use an empty string
        part1 = tup1[i] if i < len(tup1) else ''
        part2 = tup2[i] if i < len(tup2) else ''

        # Combine the parts and add to the result
        result.append(part1 + part2)

    # Convert the result list to a tuple and return
    return tuple(result)

# Test the function with provided examples
assert concatenate_strings(("Manjeet", "Nikhil", "Akshat"), (" Singh", " Meherwal", " Garg")) == ('Manjeet Singh', 'Nikhil Meherwal', 'Akshat Garg')
assert concatenate_strings(("Shaik", "Ayesha", "Sanya"), ("Dawood", "Begum", "Singh")) == ('ShaikDawood', 'AyeshaBegum', 'SanyaSingh')
assert concatenate_strings(("Harpreet", "Priyanka", "Muskan"), ("Kour", "Agarwal", "Sethi")) == ('HarpreetKour', 'PriyankaAgarwal', 'MuskanSethi')

print("All tests passed successfully")