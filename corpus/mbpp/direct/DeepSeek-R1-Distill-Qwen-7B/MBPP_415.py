def max_Product(arr):
    max_prod = (-float('inf'), -float('inf'))
    max_pair = (None, None)

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            current = (arr[i], arr[j])
            product = arr[i] * arr[j]
            if product > max_prod[0]:
                max_prod = (product, current)
            elif product == max_prod[0]:
                if max_prod[1] is None or product > max_prod[1][0] * max_prod[1][1]:
                    max_prod = (product, current)

    if max_pair[0] is not None and max_pair[1] is not None:
        return max_pair[1]
    else:
        return max_pair