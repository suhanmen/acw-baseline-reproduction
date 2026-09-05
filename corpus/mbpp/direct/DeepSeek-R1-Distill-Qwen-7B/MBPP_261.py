def division_elements(dividend, divisor):
    # Calculate element-wise division of the two tuples
    return tuple(d // e for d, e in zip(dividend, divisor))