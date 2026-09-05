from typing import List

def total_match(lst1: List[str], lst2: List[str]) -> List[str]:
    """
    Write a function that accepts two lists of strings and returns the list that has 
    total number of chars in the all strings of the list less than the other list.

    if the two lists have the same number of chars, return the first list.

    Examples
    total_match([], []) ➞ []
    total_match(['hi', 'admin'], ['hI', 'Hi']) ➞ ['hI', 'Hi']
    total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) ➞ ['hi', 'admin']
    total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) ➞ ['hI', 'hi', 'hi']
    total_match(['4'], ['1', '2', '3', '4', '5']) ➞ ['4']
    """

    # Validation: Ensure inputs are actually lists
    if not isinstance(lst1, list) or not isinstance(lst2, list):
        raise TypeError("Both arguments must be of type 'list'.")

    # Validation: Ensure all elements in both lists are strings
    for item in lst1:
        if not isinstance(item, str):
            raise TypeError("All elements in the first list must be strings.")

    for item in lst2:
        if not isinstance(item, str):
            raise TypeError("All elements in the second list must be strings.")

    def calculate_total_length(input_list: List[str]) -> int:
        """
        Helper function to calculate the sum of lengths of all strings 
        in a provided list.
        """
        total_chars = 0
        for string_item in input_list:
            # Use len() to get the character count of the current string
            current_length = len(string_item)
            total_chars += current_length
        return total_chars

    # Calculate total character counts for both lists
    count1 = calculate_total_length(lst1)
    count2 = calculate_total_length(lst2)

    # Logic:
    # 1. If list 2 has fewer characters, return list 2.
    # 2. If list 1 has fewer characters, return list 1.
    # 3. If they are equal, return list 1 (as per requirements).

    if count2 < count1:
        return lst2
    else:
        # This branch handles count1 < count2 AND count1 == count2
        return lst1