def replace_list(original_list, new_list):
    """
    Replaces the last element of the input list with the elements of the new_list.

    Args:
        original_list (list): The list where the last element should be replaced.
        new_list (list): The list whose elements will replace the last element.

    Returns:
        list: A new list with the last element replaced by the new_list.
    """
    if not original_list:
        return new_list

    # Create a copy to avoid mutating the original list if necessary,
    # though standard behavior usually allows return of a new constructed list.
    result = list(original_list[:-1])
    result.extend(new_list)
    return result

if __name__ == "__main__":
    assert replace_list([1, 3, 5, 7, 9, 10],[2, 4, 6, 8])==[1, 3, 5, 7, 9, 2, 4, 6, 8]
    assert replace_list([1,2,3,4,5],[5,6,7,8])==[1,2,3,4,5,6,7,8]
    assert replace_list(["red","blue","green"],["yellow"])==["red","blue","yellow"]