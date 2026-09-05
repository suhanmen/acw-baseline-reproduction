def first_Missing_Positive(nums, n):
    """
    Finds the first missing positive integer in a list.
    The problem implies we are looking for the smallest positive integer (1, 2, 3...)
    that is not present in the input list.
    """
    # Use a set for O(1) average time complexity lookups
    num_set = set(nums)

    # Start checking from the first positive integer
    i = 1
    while True:
        if i not in num_set:
            return i
        i += 1

if __name__ == "__main__":
    # Assertions provided in the problem description
    assert first_Missing_Positive([1,2,3,-1,5],5) == 4
    assert first_Missing_Positive([0,-1,-2,1,5,8],6) == 2
    assert first_Missing_Positive([0,1,2,5,-8],5) == 3