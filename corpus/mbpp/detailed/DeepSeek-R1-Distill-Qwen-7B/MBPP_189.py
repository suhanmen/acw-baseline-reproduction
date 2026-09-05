def first_Missing_Positive(nums):
    """
    Finds the first missing positive integer in the given list.

    Args:
        nums (list): A list of integers.

    Returns:
        int: The first missing positive integer.

    Raises:
        TypeError: If the input is not a list.
    """
    if not isinstance(nums, list):
        raise TypeError("Input must be a list of integers.")

    # Handle the case where the list is empty
    if not nums:
        return 1

    # Create a set of positive integers for O(1) lookups
    positive_ints = set()
    for num in nums:
        if isinstance(num, int) and num > 0:
            positive_ints.add(num)

    # Find the smallest positive integer not in the set
    missing = 1
    while missing in positive_ints:
        missing += 1

    return missing

# Example usage:
# print(first_Missing_Positive([1,2,3,-1,5],5))  # Output: 4
# print(first_Missing_Positive([0,-1,-2,1,5,8],6))  # Output: 2
# print(first_Missing_Positive([0,1,2,5,-8],5))  # Output: 3