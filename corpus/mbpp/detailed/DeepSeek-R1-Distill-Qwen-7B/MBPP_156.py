def tuple_int_str(strings):
    # Validate the input
    for string in strings:
        # Check if the string is empty or has non-digit characters
        if len(string) == 0 or not string.isdigit():
            raise ValueError(f"Invalid string format: {string}")

    # Convert each string to an integer
    integers = tuple(int(s) for s in strings)

    return integers