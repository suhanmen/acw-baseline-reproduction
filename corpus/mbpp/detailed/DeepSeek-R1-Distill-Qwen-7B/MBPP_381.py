def index_on_inner_list(list_of_lists, index):
    # Validate the input
    if not list_of_lists:
        return []

    # Check if all inner lists have the same length
    inner_list_length = len(list_of_lists[0])
    if any(len(inner_list) != inner_list_length for inner_list in list_of_lists):
        raise ValueError("All inner lists must have the same length")

    # Check if the index is within bounds for all inner lists
    if index < 0 or index >= inner_list_length:
        raise ValueError("Index out of bounds for all inner lists")

    # Function to extract the sort key for each element
    def get_key(element):
        return element[index]

    # Sort the list of lists based on the key
    sorted_list = sorted(list_of_lists, key=get_key)

    return sorted_list

# Test the function with the provided assertions
assert index_on_inner_list([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)], 0) == [ ('Beau Turnbull', 94, 98), ('Brady Kent', 97, 96), ('Greyson Fulton', 98, 99), ('Wyatt Knott', 91, 94) ]
assert index_on_inner_list([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)], 1) == [ ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98), ('Brady Kent', 97, 96), ('Greyson Fulton', 98, 99) ]
assert index_on_inner_list([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)], 2) == [ ('Wyatt Knott', 91, 94), ('Brady Kent', 97, 96), ('Beau Turnbull', 94, 98), ('Greyson Fulton', 98, 99) ]