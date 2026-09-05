def perimeter_pentagon(side_length):
    def validate_input(s):
        try:
            # Check if input is a number
            return isinstance(s, (int, float))
        except TypeError:
            # If input is not a number, raise ValueError
            raise ValueError("Invalid input. Please provide a number.")

    def calculate_perimeter(s):
        return s * 5

    # Validate the input
    if not validate_input(side_length):
        raise ValueError("Side length must be a non-negative number.")

    # Calculate the perimeter
    perimeter = calculate_perimeter(side_length)

    # Return the result
    return perimeter