def is_num_keith(number):
    # Handle non-integer inputs
    if not isinstance(number, int):
        return False

    # Extract the digits of the number
    digits = []
    if number == 0:
        digits = [0]
    else:
        temp = abs(number)
        while temp > 0:
            digits.append(temp % 10)
            temp = temp // 10

    # Reverse to get the correct order
    digits = digits[::-1]

    # If the number has only one digit, check if it's 1 or 0
    if len(digits) == 1:
        return number in {0, 1}

    # Initialize the sequence with the digits
    sequence = digits.copy()

    # Generate next terms until we exceed the number or include it
    while True:
        next_term = sum(sequence)
        if next_term == number:
            return True
        elif next_term > number:
            return False
        else:
            sequence.append(next_term)

    # The loop will always return before reaching here
    return False