def remove_elements(original_list, list_to_remove):
    """
    Removes all elements from the original_list that are present in list_to_remove.
    Preserves the original order of elements.
    """
    # Using a set for O(1) average time complexity lookup
    to_remove = set(list_to_remove)
    return [item for item in original_list if item not in to_remove]

if __name__ == "__main__":
    assert remove_elements([1,2,3,4,5,6,7,8,9,10],[2,4,6,8])==[1, 3, 5, 7, 9, 10]
    assert remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],[1, 3, 5, 7])==[2, 4, 6, 8, 9, 10]
    assert remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],[5,7])==[1, 2, 3, 4, 6, 8, 9, 10]