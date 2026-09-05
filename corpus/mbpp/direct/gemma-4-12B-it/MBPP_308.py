import heapq

def large_product(list1, list2, n):
    """
    Finds the specified number of largest products from two given lists.

    Args:
        list1: A list of integers.
        list2: A list of integers.
        n: The number of largest products to return.

    Returns:
        A list of the n largest products in descending order.
    """
    products = []
    for x in list1:
        for y in list2:
            products.append(x * y)

    # Using nlargest is more efficient than sorting the entire list
    # if n is small relative to the total number of products.
    return heapq.nlargest(n, products)