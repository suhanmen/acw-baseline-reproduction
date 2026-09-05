def index_multiplication(tuple_a, tuple_b):
    # Validate that both inputs are tuples
    if not isinstance(tuple_a, tuple) or not isinstance(tuple_b, tuple):
        raise ValueError("Both inputs must be tuples.")

    # Check if the tuples have the same length
    if len(tuple_a) != len(tuple_b):
        raise ValueError("The two tuples must have the same length.")

    # Handle the case where one or both tuples are empty
    if len(tuple_a) == 0:
        return ()

    # Initialize the result list with the first element's product
    result = [tuple_a[0] * tuple_b[0]]

    # Iterate through the elements starting from the second element
    for i in range(1, len(tuple_a)):
        # Multiply corresponding elements
        product = tuple_a[i] * tuple_b[i]
        # Append the product to the result list
        result.append(product)

    # Return the result as a tuple of tuples
    return tuple(result)