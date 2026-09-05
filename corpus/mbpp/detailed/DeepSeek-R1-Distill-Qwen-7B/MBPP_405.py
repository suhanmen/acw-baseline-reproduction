def check_tuplex(tuplex, element):
    # Validate the input tuple
    def validate_input(t, e):
        if not isinstance(t, tuple):
            return False
        if not isinstance(e, (int, str, float)):  # Assuming we only check for int, str, float
            return False
        return True

    # Validate the inputs
    if not validate_input(tuplex, element):
        return False

    # Check if the element exists in the tuple
    def check_element(t, e):
        return e in t

    return check_element(tuplex, element)