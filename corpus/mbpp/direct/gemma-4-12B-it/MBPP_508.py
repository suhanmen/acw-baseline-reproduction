from typing import List

def same_order(list1: List[str], list2: List[str]) -> bool:
    """
    Checks if the common elements between two lists appear in the same relative order.
    """
    # Find elements common to both lists
    common_elements = set(list1).intersection(set(list2))

    # Extract elements in the order they appear in list1
    order1 = [item for item in list1 if item in common_elements]

    # Extract elements in the order they appear in list2
    order2 = [item for item in list2 if item in common_elements]

    # If the ordered common elements are identical, they are in the same relative order
    return order1 == order2

if __name__ == "__main__":
    assert same_order(["red","green","black","orange"],["red","pink","green","white","black"]) == True
    assert same_order(["red","pink","green","white","black"],["white","orange","pink","black"]) == False
    assert same_order(["red","green","black","orange"],["red","pink","green","white","black"]) == True