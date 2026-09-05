from typing import List, Union

Number = Union[int, float]
OptionalNumber = Union[Number, None]

def _validate_input_lists(list_a: List[OptionalNumber], list_b: List[OptionalNumber]) -> None:
    """
    Validates that both input lists are of the same non-negative length
    and contain only numbers (int or float), not None.
    """
    if list_a is None:
        raise ValueError("Input list 'a' cannot be None.")
    if list_b is None:
        raise ValueError("Input list 'b' cannot be None.")

    length_a = len(list_a)
    length_b = len(list_b)

    if length_a < 0 or length_b < 0:
        raise ValueError("Input lists cannot have negative lengths.")

    if length_a != length_b:
        raise ValueError(f"Input lists must have the same length. List 'a' has {length_a}, list 'b' has {length_b}.")

    for index in range(length_a):
        value_a = list_a[index]
        value_b = list_b[index]

        if value_a is None or value_b is None:
            raise ValueError(f"All elements must be numbers. Found None at index {index} in one of the lists.")

        if not isinstance(value_a, (int, float)) or isinstance(value_a, bool):
            raise ValueError(f"All elements must be numbers. Found non-number '{value_a}' at index {index} in list 'a'.")
        if not isinstance(value_b, (int, float)) or isinstance(value_b, bool):
            raise ValueError(f"All elements must be numbers. Found non-number '{value_b}' at index {index} in list 'b'.")


def _validate_k_value(k: int) -> None:
    """
    Validates that the requested number of products 'k' is a positive integer.
    """
    if k is None:
        raise ValueError("The number of products 'k' cannot be None.")
    if not isinstance(k, int) or isinstance(k, bool):
        raise ValueError("The number of products 'k' must be an integer.")
    if k <= 0:
        raise ValueError("The number of products 'k' must be greater than zero.")


def _validate_k_against_list_sizes(k: int, list_length: int) -> None:
    """
    Validates that the requested number of products 'k' does not exceed 
    the total number of possible products (length_a * length_b).
    """
    max_possible_products = list_length * list_length
    if k > max_possible_products:
        raise ValueError(
            f"Requested {k} products, but only {max_possible_products} possible products exist "
            f"based on the input list size ({list_length})."
        )


def _compute_all_products(list_a: List[Number], list_b: List[Number]) -> List[Number]:
    """
    Computes the Cartesian product of the two lists.
    Returns a flat list containing all pairwise products.
    """
    products: List[Number] = []
    count_a = len(list_a)
    count_b = len(list_b)

    for i in range(count_a):
        value_a = list_a[i]
        for j in range(count_b):
            value_b = list_b[j]
            product = value_a * value_b
            products.append(product)

    return products


def _sort_products_descending(products: List[Number]) -> List[Number]:
    """
    Sorts the list of products in descending order.
    """
    products_copy = list(products)
    products_copy.sort(reverse=True)
    return products_copy


def _extract_top_k(products: List[Number], k: int) -> List[Number]:
    """
    Extracts the top k elements from the sorted list.
    """
    if k == 0:
        return []
    if k >= len(products):
        return list(products)

    return products[:k]


def large_product(list_a: List[OptionalNumber], list_b: List[OptionalNumber], k: int) -> List[Number]:
    """
    Finds the specified number of largest products from two given lists.

    This function computes all possible pairwise products of elements from the 
    two input lists, sorts them in descending order, and returns the top 'k' products.

    Parameters:
        list_a (List[OptionalNumber]): The first list of numbers.
        list_b (List[OptionalNumber]): The second list of numbers.
        k (int): The number of largest products to return.

    Returns:
        List[Number]: A list containing the k largest products in descending order.

    Raises:
        ValueError: If inputs are invalid (wrong types, None, mismatched lengths, etc.).
    """
    # Step 1: Validate Input Lists
    _validate_input_lists(list_a, list_b)

    # Step 2: Validate K value
    _validate_k_value(k)

    # Step 3: Validate K against list sizes
    list_length = len(list_a)
    _validate_k_against_list_sizes(k, list_length)

    # Step 4: Compute all pairwise products
    all_products = _compute_all_products(list_a, list_b)

    # Step 5: Sort products in descending order
    sorted_products = _sort_products_descending(all_products)

    # Step 6: Extract top k
    result = _extract_top_k(sorted_products, k)

    return result