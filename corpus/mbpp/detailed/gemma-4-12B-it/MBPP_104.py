from typing import List

def sort_sublists(nested_list: List[List[str]]) -> List[List[str]]:
    """
    Sorts each sublist of strings within a given list of lists.
    Sorting is performed lexicographically based on the string values.

    Args:
        nested_list (List[List[str]]): A list containing sublists of strings.

    Returns:
        List[List[str]]: A new list where each sublist has been sorted.

    Raises:
        TypeError: If the input is not a list of lists of strings.
        ValueError: If any element within the sublists is not a string.
    """
    # Validate that the input is a list
    if not isinstance(nested_list, list):
        raise TypeError("Input must be a list of lists.")

    # This will hold our resulting list of sorted sublists
    sorted_nested_list: List[List[str]] = []

    for index, sublist in enumerate(nested_list):
        # Validate that each element in the outer list is a list
        if not isinstance(sublist, list):
            raise TypeError(f"Element at index {index} is not a list.")

        # Validate that every element inside the sublist is a string
        for item in sublist:
            if not isinstance(item, str):
                raise ValueError(f"Found non-string element '{item}' at index {index}.")

        # Handle the edge case of an empty sublist
        if len(sublist) == 0:
            sorted_nested_list.append([])
            continue

        # Use a lambda function as the sorting key to perform a standard 
        # lexicographical sort on the strings in the sublist.
        # We create a copy of the sublist to avoid mutating the original input.
        sublist_copy = list(sublist)

        # The problem specifically asks to use a lambda function for sorting.
        # The lambda here acts as the key. A standard sort() uses the identity
        # or a custom key. Here we define the key as the string itself.
        sublist_copy.sort(key=lambda x: x)

        # Append the sorted copy to our result list
        sorted_nested_list.append(sublist_copy)

    return sorted_nested_list

if __name__ == "__main__":
    # Test Case 1
    input1 = [["green", "orange"], ["black", "white"], ["white", "black", "orange"]]
    expected1 = [['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
    assert sort_sublists(input1) == expected1

    # Test Case 2
    input2 = [[" red ","green" ],["blue "," black"],[" orange","brown"]]
    expected2 = [[' red ', 'green'], [' black', 'blue '], [' orange', 'brown']]
    assert sort_sublists(input2) == expected2

    # Test Case 3
    input3 = [["zilver","gold"], ["magnesium","aluminium"], ["steel", "bronze"]]
    expected3 = [['gold', 'zilver'],['aluminium', 'magnesium'], ['bronze', 'steel']]
    assert sort_sublists(input3) == expected3