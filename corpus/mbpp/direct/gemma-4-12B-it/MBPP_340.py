def sum_three_smallest_nums(numbers):
    """
    Finds the sum of the three lowest positive numbers from a given list.
    Positive numbers are defined as numbers strictly greater than 0.
    """
    # Filter the list to keep only positive numbers
    positive_nums = [num for num in numbers if num > 0]

    # If there are fewer than 3 positive numbers, sum all of them
    # (Though the problem implies at least 3 will exist based on assertions)
    positive_nums.sort()

    return sum(positive_nums[:3])