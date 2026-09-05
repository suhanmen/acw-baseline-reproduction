def common_in_nested_lists(nested_lists):
    """
    Find common elements in given nested lists.

    Args:
        nested_lists: A list of lists where each sublist contains integers.

    Returns:
        A list of integers that are present in all sublists.

    Raises:
        ValueError: If any sublist is empty.
    """
    # Validate input: check that all sublists are non-empty
    for sublist in nested_lists:
        if not sublist:
            raise ValueError("All sublists must contain at least one element.")

    # Determine the frequency of each element in the first sublist
    from collections import defaultdict
    freq_first = defaultdict(int)
    for elem in nested_lists[0]:
        freq_first[elem] += 1

    # Helper function to count frequency of elements in a sublist
    def count_in_sublist(sublist, freq_dict):
        count = defaultdict(int)
        for elem in sublist:
            count[elem] += 1
            # Early exit if any element's count exceeds the frequency in the first sublist
            if count[elem] > freq_dict[elem]:
                return None
        return count

    # Calculate the frequency of each element in all sublists
    all_freq = count_in_sublist(nested_lists[0], freq_first)
    if all_freq is None:
        return []

    # Helper function to find intersection of frequency dictionaries
    def intersection(freq1, freq2):
        result = defaultdict(int)
        for elem, count in freq1.items():
            if elem in freq2 and freq2[elem] >= count:
                result[elem] = count
        return result

    # Find common elements across all sublists
    common = intersection(freq_first, all_freq)
    if not common:
        return []

    # Extract elements from the frequency dictionary
    result = []
    for elem, count in common.items():
        if count >= 1:
            result.append(elem)

    # Remove duplicates while preserving order
    seen = set()
    unique_result = []
    for elem in reversed(result):
        if elem not in seen:
            seen.add(elem)
            unique_result.append(elem)
    unique_result.reverse()

    return unique_result

# Test the function with the provided examples
def test_common_in_nested_lists():
    assert common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]) == [18, 12]
    assert common_in_nested_lists([[12, 5, 23, 25, 45], [7, 11, 5, 23, 28], [1, 5, 8, 18, 23, 16]]) == [5, 23]
    assert common_in_nested_lists([[2, 3, 4, 1], [4, 5], [6, 4, 8], [4, 5], [6, 8, 4]]) == [4]

# Run the tests
test_common_in_nested_lists()