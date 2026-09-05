def index_minimum(tuples_list):
    if not tuples_list:
        return None
    min_name = tuples_list[0][0]
    min_value = tuples_list[0][1]
    for name, value in tuples_list:
        if value < min_value:
            min_value = value
            min_name = name
    return min_name

# Test cases
assert index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]) == 'Varsha', "Test case 1 failed"
assert index_minimum([('Yash', 185), ('Dawood', 125), ('Sanya', 175)]) == 'Dawood', "Test case 2 failed"
assert index_minimum([('Sai', 345), ('Salman', 145), ('Ayesha', 96)]) == 'Ayesha', "Test case 3 failed"