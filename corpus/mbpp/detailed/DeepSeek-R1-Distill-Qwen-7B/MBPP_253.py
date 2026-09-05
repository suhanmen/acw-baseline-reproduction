def count_integer(lst):
    def is_int(element):
        return type(element) == int

    def is_integer_float(element):
        return isinstance(element, float) and element.is_integer()

    count = 0
    for element in lst:
        if is_int(element) or is_integer_float(element):
            count += 1
    return count

# Test cases
assert count_integer([1,2,'abc',1.2]) == 2
assert count_integer([1,2,3]) == 3
assert count_integer([1,1.2,4,5.1]) == 2