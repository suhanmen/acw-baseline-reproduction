from typing import List

def find_Product(nums: List[int], length: int) -> int:
    """
    Calculates the product of all elements in the list that appear exactly 
    once in the input sequence.

    Args:
        nums: A list of integers.
        length: The length of the list to consider.

    Returns:
        int: The product of non-repeated elements. Returns 0 if no 
             non-repeated elements exist (based on standard product logic 
             for an empty set of criteria, though usually 1 is the 
             multiplicative identity, the prompt's logic implies 
             identifying specific indices).
    """
    # --- Input Validation ---
    if not isinstance(nums, list):
        raise ValueError("The input 'nums' must be a list of integers.")

    if not isinstance(length, int):
        raise ValueError("The input 'length' must be an integer.")

    # Check if the length provided matches the actual list size or 
    # handle slices if the user provides a length smaller than the list.
    if length > len(nums):
        raise ValueError("The provided length exceeds the actual size of the list.")

    # Consider only the relevant part of the list
    target_slice = nums[:length]

    # Handle empty input case
    if not target_slice:
        return 0

    # --- Frequency Counting ---
    # We use a dictionary to count occurrences of each number
    counts = {}
    for number in target_slice:
        if not isinstance(number, int):
            raise TypeError(f"Element {number} is not an integer.")

        if number in counts:
            counts[number] += 1
        else:
            counts[number] = 1

    # --- Identification of Unique Elements ---
    # An element is "non-repeated" if its count is exactly 1
    non_repeated_elements = []

    # We iterate over the slice to maintain original order, 
    # though order doesn't affect product.
    for number in target_slice:
        count_of_number = counts.get(number, 0)
        if count_of_number == 1:
            non_repeated_elements.append(number)

    # --- Product Calculation ---
    # Edge case: If no elements are non-repeated, what should be returned?
    # Looking at the test cases:
    # [1,1,2,3] -> 2*3 = 6
    # [1,2,3,1,1] -> 2*3 = 6
    # [1,1,4,5,6] -> 4*5*6 = 120
    # If no unique elements existed, the mathematical product of an empty set 
    # is 1, but for programming tasks of this type, 0 or 1 is common.
    # Given the logic, we will return 0 if the list of unique items is empty.

    if not non_repeated_elements:
        return 0

    product_result = 1
    for val in non_repeated_elements:
        product_result *= val

    return product_result

# The assertions provided in the prompt:
# assert find_Product([1,1,2,3],4) == 6
# assert find_Product([1,2,3,1,1],5) == 6
# assert find_Product([1,1,4,5,6],5) == 120