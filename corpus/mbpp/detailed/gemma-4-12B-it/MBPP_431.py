from typing import List, Any, Optional

def common_element(list1: List[Any], list2: List[Any]) -> Optional[bool]:
    """
    Determines if two lists share at least one common element.

    Returns:
        True if there is at least one common element.
        None if there are no common elements.

    Args:
        list1: The first list to compare.
        list2: The second list to compare.

    Raises:
        TypeError: If inputs are not list types.
    """
    # Validate that inputs are actually lists
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise TypeError("Both inputs must be of type 'list'.")

    # Handle the case where one or both lists are empty.
    # An empty list cannot share an element with any other list.
    if len(list1) == 0 or len(list2) == 0:
        return None

    # To optimize the search for common elements, we convert the first list
    # into a set. This provides O(1) average-time complexity for lookups.
    # Using a set also handles duplicates naturally.
    set_of_elements1 = set()
    for item in list1:
        set_of_elements1.add(item)

    # We iterate through the second list and check if any element 
    # exists in the first set.
    found_common = False

    for item in list2:
        # Check if the item exists in our set of first-list elements.
        if item in set_of_elements1:
            found_common = True
            # Once one common element is found, we can stop searching.
            break

    # The problem specification requires returning True for a match,
    # and specifically None for no match (as indicated by the assertions).
    if found_common:
        return True
    else:
        return None

# The provided assertions are satisfied as follows:
# assert common_element([1,2,3,4,5], [5,6,7,8,9]) == True
# assert common_element([1,2,3,4,5], [6,7,8,9]) == None
# assert common_element(['a','b','c'], ['d','b','e']) == True