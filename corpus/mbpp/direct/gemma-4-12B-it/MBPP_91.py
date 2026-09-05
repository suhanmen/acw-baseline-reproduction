def find_substring(string_list, substring):
    """
    Checks if a given substring exists within any of the strings in a list.

    Args:
        string_list (list of str): A list containing string values.
        substring (str): The substring to search for.

    Returns:
        bool: True if the substring is found in any element of the list, False otherwise.
    """
    for item in string_list:
        if substring in item:
            return True
    return False

if __name__ == "__main__":
    assert find_substring(["red", "black", "white", "green", "orange"], "ack") == True
    assert find_substring(["red", "black", "white", "green", "orange"], "abc") == False
    assert find_substring(["red", "black", "white", "green", "orange"], "ange") == True