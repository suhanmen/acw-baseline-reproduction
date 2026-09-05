def remove_empty(lst):
    """
    Removes all empty lists from a given list of lists/items.

    Args:
        lst (list): A list containing various elements, including some empty lists.

    Returns:
        list: A list containing all elements except the empty lists.
    """
    return [item for item in lst if not (isinstance(item, list) and len(item) == 0)]

if __name__ == "__main__":
    assert remove_empty([[], [], [], 'Red', 'Green', [1,2], 'Blue', [], []])==['Red', 'Green', [1, 2], 'Blue']
    assert remove_empty([[], [], [],[],[], 'Green', [1,2], 'Blue', [], []])==[ 'Green', [1, 2], 'Blue']
    assert remove_empty([[], [], [], 'Python',[],[], 'programming', 'language',[],[],[], [], []])==['Python', 'programming', 'language']