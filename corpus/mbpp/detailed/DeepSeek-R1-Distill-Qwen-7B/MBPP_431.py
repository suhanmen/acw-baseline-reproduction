def common_element(list_a, list_b):
    # Handle the case where either list is empty
    if not list_a or not list_b:
        return False

    # Convert both lists to sets for efficient membership checking
    set_a = set(list_a)
    set_b = set(list_b)

    # Check if there's any intersection between the two sets
    common = set_a.intersection(set_b)

    # Return True if there is at least one common element, else False
    return len(common) > 0