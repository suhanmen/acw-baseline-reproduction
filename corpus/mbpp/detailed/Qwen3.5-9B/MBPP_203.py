def _validate_inputs(value_a, value_b):
    """
    Validates that both inputs are integers and handles the case where they are not.
    Raises a ValueError if either input is invalid.

    :param value_a: The first integer value to compare.
    :param value_b: The second integer value to compare.
    :raises: ValueError if inputs are not integers.
    """
    if not isinstance(value_a, int):
        raise ValueError(f"The first argument must be an integer, got {type(value_a).__name__}.")
    if not isinstance(value_b, int):
        raise ValueError(f"The second argument must be an integer, got {type(value_b).__name__}.")

def _convert_to_binary_representation(number):
    """
    Converts a non-negative integer to a list of its binary digits (bits).

    Logic:
    1. Handle the zero case explicitly.
    2. Repeatedly take modulo 2 to get the current bit.
    3. Divide by 2 to move to the next bit.
    4. Store bits in a list (will be reversed at the end).

    :param number: A non-negative integer.
    :return: A list of integers (0s and 1s) representing the binary form.
    """
    if number == 0:
        return [0]

    bits = []
    temp_number = number

    while temp_number > 0:
        current_bit = temp_number % 2
        bits.append(current_bit)
        temp_number = temp_number // 2

    # The bits are collected in reverse order (LSB first), so we reverse them back
    bits.reverse()

    return bits

def _align_binary_lists(bits_a, bits_b):
    """
    Aligns two binary lists to the same length by padding the shorter one 
    with zeros on the left (most significant side).

    This ensures that bits are compared at the correct positions.

    :param bits_a: First list of binary digits.
    :param bits_b: Second list of binary digits.
    :return: Two lists of equal length representing the aligned binary numbers.
    """
    length_a = len(bits_a)
    length_b = len(bits_b)

    target_length = max(length_a, length_b)

    padded_a = bits_a
    padded_b = bits_b

    if length_a < target_length:
        padding_count = target_length - length_a
        # Create a list of zeros for padding
        padding_zeros = [0] * padding_count
        # Prepend padding to the original list
        padded_a = padding_zeros + bits_a

    if length_b < target_length:
        padding_count = target_length - length_b
        # Create a list of zeros for padding
        padding_zeros = [0] * padding_count
        # Prepend padding to the original list
        padded_b = padding_zeros + bits_b

    return padded_a, padded_b

def _calculate_hamming_distance_aligned(aligned_bits_a, aligned_bits_b):
    """
    Calculates the Hamming distance between two aligned binary lists.

    The Hamming distance is the number of positions at which the corresponding
    bits are different.

    :param aligned_bits_a: First aligned list of binary digits.
    :param aligned_bits_b: Second aligned list of binary digits.
    :return: An integer representing the Hamming distance.
    """
    distance = 0
    length = len(aligned_bits_a)

    for index in range(length):
        bit_a = aligned_bits_a[index]
        bit_b = aligned_bits_b[index]

        if bit_a != bit_b:
            distance = distance + 1

    return distance

def hamming_Distance(value_a, value_b):
    """
    Calculates the Hamming distance between two integers.

    The Hamming distance is the number of positions at which the corresponding
    bits are different.

    Steps:
    1. Validate inputs to ensure they are integers.
    2. Convert both integers to binary representations.
    3. Align the binary representations to the same length.
    4. Compare bits at each position and count differences.
    5. Return the count of differences.

    :param value_a: The first integer.
    :param value_b: The second integer.
    :return: The Hamming distance between the two integers.
    :raises: ValueError if inputs are not integers.
    """
    # Step 1: Validate inputs
    _validate_inputs(value_a, value_b)

    # Step 2: Convert integers to binary lists
    bits_a = _convert_to_binary_representation(value_a)
    bits_b = _convert_to_binary_representation(value_b)

    # Step 3: Align the binary lists
    aligned_a, aligned_b = _align_binary_lists(bits_a, bits_b)

    # Step 4: Calculate the distance
    distance = _calculate_hamming_distance_aligned(aligned_a, aligned_b)

    # Step 5: Return the result
    return distance