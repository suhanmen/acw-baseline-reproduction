def insert_element(main_list, element_to_insert):
    # Input validation
    if not isinstance(main_list, list):
        raise TypeError("The main list must be a list.")
    if not isinstance(element_to_insert, list):
        raise TypeError("The element to insert must be a list.")

    # Handle empty main list
    if not main_list:
        return []

    # Initialize the result list
    result = []

    # Iterate over each element and insert before it
    for element in main_list:
        # Insert element_to_insert before each element
        result.insert(0, element_to_insert)
        result.append(element)

    return result