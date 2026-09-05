def find_Product(arr):
    # Check if the input is a list of integers
    if not isinstance(arr, list):
        raise ValueError("Input must be a list of integers")
    for element in arr:
        if not isinstance(element, int):
            raise ValueError("All elements in the array must be integers")

    # Count the occurrences of each element
    counts = {}
    for element in arr:
        if element in counts:
            counts[element] += 1
        else:
            counts[element] = 1

    # Identify elements that appear exactly once
    non_repeated_elements = [element for element, count in counts.items() if count == 1]

    # Calculate the product of non-repeated elements
    product = 1
    for element in non_repeated_elements:
        product *= element

    return product