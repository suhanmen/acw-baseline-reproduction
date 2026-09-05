def sum_of_digits(data):
    """
    Computes the sum of digits of each number in a given list.
    Handles nested lists and ignores non-numeric types.
    """
    total_sum = 0

    def process_item(item):
        nonlocal total_sum
        if isinstance(item, list):
            for sub_item in item:
                process_item(sub_item)
        elif isinstance(item, int):
            # Use absolute value to handle negative numbers
            # and sum the digits of the integer
            total_sum += sum(int(digit) for digit in str(abs(item)))

    process_item(data)
    return total_sum

if __name__ == "__main__":
    assert sum_of_digits([10, 2, 56]) == 14
    assert sum_of_digits([[10, 20, 4, 5, 'b', 70, 'a']]) == 19
    assert sum_of_digits([10, 20, -4, 5, -70]) == 19