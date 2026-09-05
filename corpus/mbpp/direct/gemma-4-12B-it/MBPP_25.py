from typing import List

def find_Product(arr: List[int], n: int) -> int:
    """
    Finds the product of non-repeated elements in a given array.
    An element is considered non-repeated if it appears exactly once in the array.
    """
    counts = {}
    for x in arr:
        counts[x] = counts.get(x, 0) + 1

    product = 1
    has_non_repeated = False

    for x in arr:
        if counts[x] == 1:
            product *= x
            has_non_repeated = True

    return product if has_non_repeated else 0