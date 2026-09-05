def index_multiplication(tuple1, tuple2):
    result = []
    for i in range(len(tuple1)):
        t1 = tuple1[i]
        t2 = tuple2[i]
        product_tuple = tuple(a * b for a, b in zip(t1, t2))
        result.append(product_tuple)
    return tuple(result)