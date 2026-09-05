import collections

def freq_element(lst):
    """
    Finds the frequency of each element in a list of lists.

    Args:
        lst (List[List[int]]): A list where each element is a list of integers.

    Returns:
        Dict[int, int]: A dictionary where the keys are the elements and the values are their frequencies.

    Raises:
        ValueError: If the input list is not a list of lists, or if any sublist is not a list.
    """
    # Validate input
    if not isinstance(lst, list):
        raise ValueError("Input must be a list.")
    for sub in lst:
        if not isinstance(sub, list):
            raise ValueError("All sublists must be lists.")

    # Helper function to flatten the list of lists
    def flatten(nested_list):
        """
        Flattens a list of lists into a single list of elements.
        """
        flat_list = []
        for sublist in nested_list:
            flat_list.extend(sublist)
        return flat_list

    # Flatten the list of lists
    flat = flatten(lst)

    # Count frequency using collections.Counter
    freq = collections.Counter(flat)

    return freq

# Test cases
def test_freq_element1():
    input_list = [[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]]
    expected_output = {2: 3, 1: 2, 5: 2, 3: 1, 4: 1, 6: 1, 7: 1, 9: 1}
    assert freq_element(input_list) == expected_output, "Test case 1 failed."

def test_freq_element2():
    input_list = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    expected_output = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1}
    assert freq_element(input_list) == expected_output, "Test case 2 failed."

def test_freq_element3():
    input_list = [[15,20,30,40],[80,90,100,110],[30,30,80,90]]
    expected_output = {30: 3, 80: 2, 90: 2, 15: 1, 20: 1, 40: 1, 100: 1, 110: 1}
    assert freq_element(input_list) == expected_output, "Test case 3 failed."

# Run all test cases
if __name__ == "__main__":
    test_freq_element1()
    test_freq_element2()
    test_freq_element3()
    print("All test cases passed.")