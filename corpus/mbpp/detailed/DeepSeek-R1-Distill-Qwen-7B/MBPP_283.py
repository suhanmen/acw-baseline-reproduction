def validate(number):
    # Handle negative numbers
    if not isinstance(number, int) or number < 0:
        return False
    # Handle zero case
    if number == 0:
        return True

    # Convert number to string to process each digit
    digits = str(number)

    # Count the frequency of each digit
    frequency = {}
    for d in digits:
        if d in frequency:
            frequency[d] += 1
        else:
            frequency[d] = 1

    # Check each digit's frequency
    for digit, count in frequency.items():
        if int(digit) < count:
            return False
    return True