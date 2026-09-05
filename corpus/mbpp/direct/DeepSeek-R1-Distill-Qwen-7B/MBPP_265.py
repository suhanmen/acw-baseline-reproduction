def list_split(lst, n):
    # Calculate the number of sublists needed
    num_sublists = n
    # Initialize a list to hold the sublists
    sublists = [[] for _ in range(num_sublists)]
    # Iterate over the elements of the list, stepping by n each time
    for i in range(len(lst)):
        # Append the element to the corresponding sublist
        sublists[i % n].append(lst[i])
    # Return the list of sublists
    return sublists