def by_length(arr):
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
    # Filter the array to include only integers between 1 and 9
    valid_numbers = [num for num in arr if isinstance(num, int) and 1 <= num <= 9]

    if not valid_numbers:
        return []

    # Sort the valid numbers in ascending order
    sorted_numbers = sorted(valid_numbers)

    # Reverse the sorted array
    reversed_numbers = sorted_numbers[::-1]

    # Mapping of numbers to their corresponding words
    number_to_word = {
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

    # Convert each number to its corresponding word
    words = [number_to_word[num] for num in reversed_numbers]

    return words