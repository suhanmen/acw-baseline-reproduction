def chkList(lst):
    """Check whether all elements in the list are the same."""
    if not lst:  # Handle empty list
        return True
    first = lst[0]
    if all(x == first for x in lst):  # Check if all elements are equal to the first
        return True
    else:
        return False

# Helper function to check if all elements are equal to the first element
def _all_equal(lst, first):
    for x in lst:
        if x != first:
            return False
    return True

# Edge case handling
if not lst:  # Empty list
    print("True")
elif len(lst) == 1:  # Single element
    print("True")
else:
    first = lst[0]
    for x in lst:
        if x != first:
            print("False")
            break
    else:
        print("True")