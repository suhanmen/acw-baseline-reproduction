def max_product_tuple(pairs):
    max_prod = None
    for a, b in pairs:
        prod = a * b
        if max_prod is None or prod > max_prod:
            max_prod = prod
    return max_prod