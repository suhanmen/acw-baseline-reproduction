def even_bit_toggle_number(n):
    # Create a mask with 1s at all odd bit positions
    mask = 0xAAAAAAAA  # Binary: 1010101010101010...
    # Toggle all odd bits by XOR
    return n ^ mask