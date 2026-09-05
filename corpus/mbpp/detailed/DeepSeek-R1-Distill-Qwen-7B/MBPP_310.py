assert string_to_tuple("python 3.0") == ('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0')
# This should return the tuple with each character, including the space and special characters

assert string_to_tuple("item1") == ('i', 't', 'e', 'm', '1')
# This should return the tuple with each character of the string

assert string_to_tuple("15.10") == ('1', '5', '.', '1', '0')
# This should return the tuple with each character, including digits and special characters