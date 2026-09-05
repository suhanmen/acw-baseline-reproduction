from typing import List

def by_length(arr: List[int]) -> List[str]:
    """
    Given an array of integers, sort the integers that are between 1 and 9 inclusive,
    reverse the resulting array, and then replace each digit by its corresponding name from
    "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine".

    For example:
      arr = [2, 1, 1, 4, 5, 8, 2, 3]   
            -> sort arr -> [1, 1, 2, 2, 3, 4, 5, 8] 
            -> reverse arr -> [8, 5, 4, 3, 2, 2, 1, 1]
      return ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]

      If the array is empty, return an empty array:
      arr = []
      return []

      If the array has any strange number ignore it:
      arr = [1, -1 , 55] 
            -> sort arr -> [-1, 1, 55]
            -> reverse arr -> [55, 1, -1]
      return = ['One']
    """
    # Mapping of integers to their string names
    NUM_TO_NAME = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine"
    }

    # Edge Case: Handle None or non-list input if necessary
    if arr is None:
        return []

    # Edge Case: Handle empty list
    if not arr:
        return []

    # Step 1: Filter the input array to keep only integers between 1 and 9 inclusive.
    # The problem states to "ignore" strange numbers (those not in the range 1-9).
    filtered_list = []
    for item in arr:
        # Ensure item is an integer before range check to avoid TypeError
        if isinstance(item, int):
            if 1 <= item <= 9:
                filtered_list.append(item)

    # Step 2: Sort the resulting list of valid integers.
    # We use sorted() to create a new list, keeping the logic clean.
    sorted_list = sorted(filtered_list)

    # Step 3: Reverse the sorted list.
    # Reversing a sorted ascending list results in a descending list.
    reversed_list = sorted_list[::-1]

    # Step 4: Replace each digit by its corresponding name.
    result = []
    for num in reversed_list:
        name = NUM_TO_NAME.get(num)
        if name is not None:
            result.append(name)

    return result