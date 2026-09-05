from typing import List


def large_product(list1: List[int], list2: List[int], n: int) -> List[int]:
    """
    Finds the n largest products from two given lists of integers.

    The function takes two lists of integers and an integer n, 
    calculates the product of every possible pair (one from each list), 
    and returns the n largest products in descending order.
    """

    # --- Input Validation ---

    # Check if inputs are actually lists
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise TypeError("Both list1 and list2 must be of type 'list'.")

    # Check if n is an integer
    if not isinstance(n, int):
        raise TypeError("The parameter 'n' must be an integer.")

    # Check if n is non-negative
    if n < 0:
        raise ValueError("The parameter 'n' must be non-negative.")

    # Handle the case where n is 0
    if n == 0:
        return []

    # Check if both lists are empty
    if not list1 or not list2:
        # If either list is empty, no products can be formed.
        # If the user asked for n > 0 products but none exist, 
        # we return an empty list.
        return []

    # Verify that elements in the lists are integers
    for item in list1:
        if not isinstance(item, int):
            raise TypeError("All elements in list1 must be integers.")
    for item in list2:
        if not isinstance(item, int):
            raise TypeError("All elements in list2 must be integers.")

    # --- Logic Implementation ---

    # Step 1: Generate all possible products
    # We use a list to store every combination of products.
    all_products: List[int] = []

    # We iterate through every element in the first list
    for val1 in list1:
        # And every element in the second list
        for val2 in list2:
            # Calculate the product of the current pair
            current_product = val1 * val2
            # Append the product to our collection
            all_products.append(current_product)

    # Step 2: Sort the products
    # To find the largest ones, we sort the list in descending order.
    # We use a stable sort (Python's built-in Timsort).
    all_products.sort(reverse=True)

    # Step 3: Select the top n products
    # We need to handle the case where n is larger than the total number of products available.
    total_available = len(all_products)

    # If n is greater than the number of products we calculated, 
    # we can only return as many as we actually have.
    actual_count_to_return = n
    if n > total_available:
        actual_count_to_return = total_available

    # Slice the sorted list to get the top 'actual_count_to_return' elements
    result = all_products[:actual_count_to_return]

    return result