def insert_element(lst, element):
    """
    Inserts a given element before each element of a list.

    Args:
        lst (list): The original list of elements.
        element: The element to insert before each list item.

    Returns:
        list: A new list with the element inserted before each original item.
    """
    result = []
    for item in lst:
        result.append(element)
        result.append(item)
    return result

if __name__ == "__main__":
    assert insert_element(['Red', 'Green', 'Black'] ,'c') == ['c', 'Red', 'c', 'Green', 'c', 'Black'] 
    assert insert_element(['python', 'java'] ,'program') == ['program', 'python', 'program', 'java'] 
    assert insert_element(['happy', 'sad'] ,'laugh') == ['laugh', 'happy', 'laugh', 'sad']