def first_Digit(number):
    # Handle single-digit numbers
    if 0 <= number <= 9:
        return number
    # Convert number to string to access individual digits
    number_str = str(number)
    # Return the first character as an integer
    return int(number_str[0])