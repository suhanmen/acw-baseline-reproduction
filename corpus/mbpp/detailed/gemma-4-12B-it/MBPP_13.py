from typing import List, Tuple, Dict

def count_common(words: List[str]) -> List[Tuple[str, int]]:
    """
    Counts the occurrences of each word in a list and returns a list of tuples 
    containing the words and their counts, sorted by frequency descending, 
    then alphabetically ascending for ties.

    Args:
        words (List[str]): A list of strings to be counted.

    Returns:
        List[Tuple[str, int]]: A list of (word, count) tuples.
    """
    # 1. Validation: Handle non-list inputs or non-string elements
    if not isinstance(words, list):
        raise ValueError("Input must be a list of strings.")

    if not words:
        return []

    for item in words:
        if not isinstance(item, str):
            raise ValueError(f"All elements in the list must be strings. Found: {type(item)}")

    # 2. Count frequencies using a dictionary
    # We use a manual loop instead of collections.Counter to ensure 
    # maximum explicitness as per the requirements.
    word_counts: Dict[str, int] = {}

    for word in words:
        # Handle potential whitespace issues by stripping if necessary, 
        # but the prompt implies literal string matching.
        current_count = word_counts.get(word, 0)
        word_counts[word] = current_count + 1

    # 3. Prepare the list of results for sorting
    # Convert the dictionary into a list of tuples: (word, count)
    result_list: List[Tuple[str, int]] = []
    for word, count in word_counts.items():
        result_list.append((word, count))

    # 4. Sorting Logic
    # The expected output requires sorting primarily by count (descending).
    # For ties in count, we look at the assertions. 
    # In the first assertion: ('black', 5) and ('white', 5) are both 5.
    # Since 'black' comes before 'white' alphabetically, it implies 
    # alphabetical order for tied counts.

    # To achieve: 
    # Primary key: Count (Descending) -> -count
    # Secondary key: Word (Ascending) -> word

    def sorting_key(item: Tuple[str, int]) -> Tuple[int, str]:
        word_item = item[0]
        count_item = item[1]
        # We negate the count to sort descending while keeping the string ascending
        return (-count_item, word_item)

    sorted_results = sorted(result_list, key=sorting_key)

    # 5. Filter out words with count 0 (though impossible via the logic above)
    # and ensure the list is returned in the correct structure.
    final_output = []
    for entry in sorted_results:
        final_output.append(entry)

    return final_output

if __name__ == "__main__":
    # Assertions provided in the prompt to verify correctness
    assert count_common(['red','green','black','pink','black','white','black','eyes','white','black','orange','pink','pink','red','red','white','orange','white',"black",'pink','green','green','pink','green','pink','white','orange',"orange",'red]) == [('pink', 6), ('black', 5), ('white', 5), ('red', 4)]
    assert count_common(['one', 'two', 'three', 'four', 'five', 'one', 'two', 'one', 'three', 'one']) == [('one', 4), ('two', 2), ('three', 2), ('four', 1)]
    assert count_common(['Facebook', 'Apple', 'Amazon', 'Netflix', 'Google', 'Apple', 'Netflix', 'Amazon']) == [('Apple', 2), ('Amazon', 2), ('Netflix', 2), ('Facebook', 1)]