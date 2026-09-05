from collections import Counter

def find_Product(arr: list, n: int) -> int:
    """
    Returns the product of non-repeated elements in the given array.
    Non-repeated means elements that appear exactly once.
    The second argument 'n' is ignored in this implementation as it is
    just a positional parameter to match the required signature.
    """
    if not arr:
        return 1  # Product of an empty set is 1

    counts = Counter(arr)
    product = 1
    for num in arr:
        if counts[num] == 1:
            product *= num
    return product