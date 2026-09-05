def sum_of_alternates(sequence):
    # Validate input
    if not isinstance(sequence, tuple):
        raise ValueError("Input must be a tuple")

    odd_elements = []
    even_elements = []

    # Iterate through the sequence
    for i, num in enumerate(sequence):
        if i % 2 == 0:
            even_elements.append(num)
        else:
            odd_elements.append(num)

    # Calculate sums
    sum_odd = sum(odd_elements)
    sum_even = sum(even_elements)

    # Return the result
    return (sum_odd, sum_even)