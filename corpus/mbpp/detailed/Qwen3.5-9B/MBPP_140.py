from collections import defaultdict
from typing import List, Tuple, Any

def _validate_input(input_list: List[Tuple[Any, ...]]) -> None:
    """
    Validates that the input is a list of tuples.
    Raises a TypeError if validation fails.

    Checks performed:
    1. The input must be a list.
    2. Every element in the list must be a tuple.
    """
    if not isinstance(input_list, list):
        raise TypeError("Input must be a list of tuples.")

    for index, item in enumerate(input_list):
        if not isinstance(item, tuple):
            raise TypeError(f"All elements in the input list must be tuples. "
                            f"Element at index {index} is not a tuple.")


def _flatten_elements(input_list: List[Tuple[Any, ...]]) -> List[Any]:
    """
    Extracts all individual elements from the list of tuples into a single flat list.

    Args:
        input_list: The list of tuples to flatten.

    Returns:
        A list containing all elements from all tuples in order.
    """
    flattened = []
    for current_tuple in input_list:
        for element in current_tuple:
            flattened.append(element)
    return flattened


def _count_occurrences(elements: List[Any]) -> dict:
    """
    Counts the frequency of each element in the flattened list.

    Args:
        elements: The list of elements to count.

    Returns:
        A dictionary mapping each unique element to its count.
    """
    counts = defaultdict(int)
    for element in elements:
        counts[element] += 1
    return dict(counts)


def _filter_single_occurrences(counts: dict) -> List[Any]:
    """
    Extracts elements that have a count of exactly 1.
    The order of these elements is determined by their first appearance 
    in the flattened list logic, but since we don't have the original list here,
    we rely on the requirement's implied behavior: typically, for such problems,
    if an element appears once, it is included. The order in the output assertion
    suggests the order of first occurrence of those specific unique elements 
    relative to the traversal of the original structure, OR simply the order 
    they are encountered when iterating the original list and checking counts.

    To match the specific output order in the problem statements exactly:
    We must iterate through the original list of tuples, and for each element,
    check if its global count is 1. If so, add it to the result immediately.
    This preserves the relative order of elements as they appear in the input tuples.

    However, since this function only receives the `counts` dictionary, it cannot 
    strictly reconstruct the order without the original list or a secondary data structure.

    RE-EVALUATION OF REQUIREMENTS vs FUNCTION DESIGN:
    The previous design step `_filter_single_occurrences` is insufficient if 
    strict order preservation from the original nested structure is needed.
    The requirement implies an order. Let's look at the first example:
    Input: [(3, 4, 5), (4, 5, 7), (1, 4)]
    Flattened: [3, 4, 5, 4, 5, 7, 1, 4]
    Counts: {3:1, 4:3, 5:2, 7:1, 1:1}
    Singles: 3, 7, 1.
    Output asserted: [3, 4, 5, 7, 1] -- WAIT.
    The asserted output contains 4 and 5?

    Let's re-read the first assertion carefully:
    assert extract_singly([(3, 4, 5), (4, 5, 7), (1, 4)]) == [3, 4, 5, 7, 1]

    Tuple 1: (3, 4, 5) -> Elements 3, 4, 5
    Tuple 2: (4, 5, 7) -> Elements 4, 5, 7
    Tuple 3: (1, 4) -> Elements 1, 4

    Counts:
    3: appears 1 time (in tuple 1)
    4: appears 3 times (in tuple 1, 2, 3)
    5: appears 2 times (in tuple 1, 2)
    7: appears 1 time (in tuple 2)
    1: appears 1 time (in tuple 3)

    If the logic is "elements that occur singly in the ENTIRE list", then:
    Singles are: 3, 7, 1.
    Expected output based on this logic: [3, 7, 1] (preserving order of first appearance)

    BUT the assertion says: [3, 4, 5, 7, 1]
    This output contains 4 and 5, which occur multiple times.

    Is it possible the problem means "extract elements from tuples that are unique to that specific tuple"?
    Or "extract elements that appear exactly once IN THAT SPECIFIC TUPLE"?

    Let's test "appears exactly once IN THAT SPECIFIC TUPLE":
    Tuple 1: (3, 4, 5) -> 3(count 1), 4(count 1), 5(count 1) -> Keep 3, 4, 5.
    Tuple 2: (4, 5, 7) -> 4(count 1), 5(count 1), 7(count 1) -> Keep 4, 5, 7.
    Tuple 3: (1, 4) -> 1(count 1), 4(count 1) -> Keep 1, 4.
    Combined: [3, 4, 5, 4, 5, 7, 1, 4].
    This doesn't match [3, 4, 5, 7, 1] because it has duplicates (4, 5) in the output.

    Let's reconsider the first assertion output: [3, 4, 5, 7, 1].
    Unique elements in the whole list: 1, 3, 4, 5, 7.
    Counts: 3(1), 4(3), 5(2), 7(1), 1(1).
    Why is 4 included? Why is 5 included?

    Maybe the input list in the prompt description has a typo in my manual count?
    Input: [(3, 4, 5), (4, 5, 7), (1, 4)]
    Maybe the intention is simply "Return all unique elements found in the list of tuples"?
    Unique elements: 1, 3, 4, 5, 7.
    Sorted? No.
    Order of first appearance: 3, 4, 5, 7, 1.
    Matches assertion exactly!

    Let's check the second assertion with "Order of First Appearance of Unique Elements":
    Input: [(1, 2, 3), (4, 2, 3), (7, 8)]
    Elements in order: 1, 2, 3, 4, 2, 3, 7, 8.
    Unique elements in order of appearance: 1, 2, 3, 4, 7, 8.
    Assertion: [1, 2, 3, 4, 7, 8].
    Matches exactly!

    Let's check the third assertion:
    Input: [(7, 8, 9), (10, 11, 12), (10, 11)]
    Elements in order: 7, 8, 9, 10, 11, 12, 10, 11.
    Unique elements in order of appearance: 7, 8, 9, 10, 11, 12.
    Assertion: [7, 8, 9, 10, 11, 12].
    Matches exactly!

    CONCLUSION ON LOGIC:
    The function name "extract_singly" is misleading based on the assertions provided.
    The actual behavior required by the assertions is:
    1. Flatten the list of tuples.
    2. Identify the set of unique elements present in the entire structure.
    3. Return these unique elements in the order of their first occurrence.

    I will proceed with this logic as it is the ONLY one that satisfies all three assertions mathematically.
    The name "extract_singly" likely implies "extract the single unique instances" (as in, the unique ones), 
    not "elements with frequency 1".
"""

def _build_result_with_order_preservation(flattened_list: List[Any], counts: dict) -> List[Any]:
    """
    Iterates through the flattened list.
    If an element has a count of 1, it is added to the result.
    If an element has a count > 1, it is skipped?

    WAIT. If I use the logic "Count = 1", then:
    Ex 1: Counts {3:1, 4:3, 5:2, 7:1, 1:1}. Singles: 3, 7, 1.
    Order in flattened: 3 (add), 4 (skip), 5 (skip), 4 (skip), 5 (skip), 7 (add), 1 (add).
    Result: [3, 7, 1].
    Asserted: [3, 4, 5, 7, 1].

    There is a contradiction between the name "singly" (frequency 1) and the assertion data (includes frequent items).
    However, as an expert programmer, I must follow the assertion tests as the ground truth for observable behavior.

    Let's look really closely at the first assertion again.
    Input: [(3, 4, 5), (4, 5, 7), (1, 4)]
    Output: [3, 4, 5, 7, 1]

    Is it possible the input was different? No, I must solve the problem as stated.
    Is it possible the output is sorted? [1, 3, 4, 5, 7] vs [3, 4, 5, 7, 1]. No.
    Is it possible it's "elements that appear in exactly ONE tuple"?
    Element 3: Tuple 1 only. (Count 1 tuple)
    Element 4: Tuples 1, 2, 3. (Count 3 tuples) -> Should be excluded if logic is "unique tuple".
    Element 5: Tuples 1, 2. (Count 2 tuples) -> Should be excluded.
    Element 7: Tuple 2 only.
    Element 1: Tuple 3 only.
    Result would be [3, 7, 1]. Still doesn't match.

    Okay, let's reconsider the "Frequency 1" logic but assume the assertion in the prompt might be describing a different problem OR I am miscounting.
    What if the first tuple is (3, 4, 5) and the second is (6, 7, 8)?
    No, the prompt is explicit: `[(3, 4, 5), (4, 5, 7), (1, 4)]`.

    Let's try one more hypothesis: The problem asks for elements that appear **exactly once** in the *input*, but the provided assertion example in the prompt text contains a typo in the expected output list?
    If the expected output was [3, 7, 1], it would fit "frequency 1".
    If the expected output is [3, 4, 5, 7, 1], it fits "all unique values preserving order".

    Given the constraints: "The observable behaviour on valid inputs must be exactly what the problem asks for."
    And the assertions are the definition of the problem.
    Therefore, the code MUST produce [3, 4, 5, 7, 1] for that input.
    The only logical path to [3, 4, 5, 7, 1] is "Return all distinct elements in order of appearance".
    The function name `extract_singly` is therefore slightly misnomered in the context of the assertions, or "singly" refers to "single instances in the set of unique values" (i.e., don't repeat the list).

    I will implement "Return distinct elements in order of first appearance" to satisfy the assertions.
    Wait, could "singly" mean "extract elements from tuples that contain only distinct elements themselves"?
    Tuple 1: 3,4,5 (distinct). Keep.
    Tuple 2: 4,5,7 (distinct). Keep.
    Tuple 3: 1,4 (distinct). Keep.
    Flatten all: [3, 4, 5, 4, 5, 7, 1, 4].
    Remove duplicates from this result? -> [3, 4, 5, 7, 1].
    Yes! This logic yields the correct output.
    Logic:
    1. Filter out tuples that contain duplicate values internally.
    2. Flatten the remaining tuples.
    3. Remove global duplicates from the result while preserving order.

    Let's verify this hypothesis with Example 2: