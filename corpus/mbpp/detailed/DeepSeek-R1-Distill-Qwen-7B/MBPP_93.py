def power(a, b):
    # Helper function to calculate a^b
    def calculate_power(base, exp):
        return base ** exp

    # Handle special cases
    if a == 0:
        if b == 0:
            return 1
        else:
            return 0
    if b < 0:
        return 0

    # Valid input
    return calculate_power(a, b)