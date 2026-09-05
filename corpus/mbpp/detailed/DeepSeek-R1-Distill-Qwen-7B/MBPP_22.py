def find_first_duplicate(arr):
    # Check if the input is a list
    if not isinstance(arr, list):
        return -1
    # Check if the list is empty
    if len(arr) == 0:
        return -1

    # Create a dictionary to track the occurrence of each element
    occurrence = {}

    # Iterate through each element in the array
    for num in arr:
        # If the element is already in the dictionary, return it as the first duplicate
        if num in occurrence:
            return num
        # Otherwise, add the element to the dictionary
        occurrence[num] = True

    # If no duplicates are found, return -1
    return -1