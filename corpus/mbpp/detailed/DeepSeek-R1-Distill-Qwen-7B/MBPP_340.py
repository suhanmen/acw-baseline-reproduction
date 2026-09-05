def sum_three_smallest_nums(numbers):
    def is_list valid(list):
        if not isinstance(list, list):
            return False
        if len(list) < 3:
            return False
        positives = [num for num in list if num > 0]
        if len(positives) < 3:
            return False
        return True

    def get_positive_numbers(lst):
        return [num for num in lst if num > 0]

    def sort_and Take_first_three(lst):
        lst.sort()
        return sum(lst[:3])

    if not is_list_valid(numbers):
        return None

    positives = get_positive_numbers(numbers)
    sum_positives = sort_and_take_first_three(positives)
    return sum_positives

# Test cases
print(sum_three_smallest_nums([10,20,30,40,50,60,7]))  # Expected output: 37
print(sum_three_smallest_nums([1,2,3,4,5]))          # Expected output: 6
print(sum_three_smallest_nums([0,1,2,3,4,5]))        # Expected output: 6
print(sum_three_smallest_nums([1, -2, 3, -4, 5]))    # Expected output: 9
print(sum_three_smallest_nums([1, 2]))               # Expected output: None
print(sum_three_smallest_nums([-1, -2, -3]))          # Expected output: None
print(sum_three_smallest_nums([5]))                  # Expected output: None