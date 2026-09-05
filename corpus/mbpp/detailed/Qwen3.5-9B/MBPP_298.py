from typing import List, Any, Union

def _create_empty_list_of_lists() -> List[List[Any]]:
    """
    Creates and returns an empty list of lists.
    This serves as the accumulator for the result.
    """
    return []

def _convert_inner_list_to_set(inner_list: List[Any]) -> set:
    """
    Converts a list of elements into a set for O(1) lookup efficiency.

    Args:
        inner_list: The list to be converted.

    Returns:
        A set containing the unique elements of the input list.
    """
    return set(inner_list)

def _find_intersection_elements(list_one: List[Any], list_two: List[Any]) -> List[Any]:
    """
    Finds elements present in both provided lists.

    Logic:
    1. Convert the second list to a set for fast lookup.
    2. Iterate through the first list.
    3. If an element exists in the set from step 1, include it in the result list.

    Args:
        list_one: The primary list to iterate over.
        list_two: The list to convert to a set and check against.

    Returns:
        A list of elements found in both input lists, maintaining the order 
        from list_one.
    """
    set_two = _convert_inner_list_to_set(list_two)
    intersection_result = _create_empty_list_of_lists()

    for current_element in list_one:
        if current_element in set_two:
            intersection_result.append(current_element)

    return intersection_result

def _process_single_nested_element(nested_element: List[Any], 
                                   common_elements: List[Any]) -> List[Any]:
    """
    Processes a single nested list against the list of common elements.

    Logic:
    1. Check if the nested element is a list.
    2. If it is a list, find the intersection of its elements with common_elements.
    3. If it is not a list, treat it as a container with a single element 
       (conceptually similar to a single-element list) and check membership.

    Args:
        nested_element: The nested list (or element) to process.
        common_elements: The list of elements common to both input outer lists.

    Returns:
        A new list containing the matching elements found within nested_element.
        If nested_element is not a list, returns a list containing the element 
        if it exists in common_elements.
    """
    result_container = _create_empty_list_of_lists()

    # Explicit check to determine if the element is a list
    if isinstance(nested_element, list):
        # Case: It is a list. We need to find which elements inside it 
        # are present in common_elements.
        for item_in_nested in nested_element:
            if item_in_nested in common_elements:
                result_container.append(item_in_nested)
    else:
        # Case: It is not a list (based on the problem examples, inputs are lists,
        # but this handles the degenerate case where a non-list 'element' might appear).
        # In the context of the problem, the second argument contains lists, 
        # but this branch handles the logic if a single element were passed.
        if nested_element in common_elements:
            result_container.append(nested_element)

    return result_container

def intersection_nested_lists(list_one: List[Any], list_two: List[Any]) -> List[List[Any]]:
    """
    Finds the nested list elements which are present in another list.

    Specifically, for every nested list (or element) in list_one, 
    this function checks which of its elements are also present in list_two.
    It returns a new list where each entry corresponds to the matched elements 
    from the corresponding nested list in list_one.

    Example Logic based on problem:
    Input 1: ['john','amal', ...], Input 2: [['john'], ['jack','john', ...], ...]
    For 'john' in Input 1: Check against Input 2.
    However, the problem description and examples imply a specific mapping logic:
    The function seems to compare the i-th element of list_one against the i-th 
    element of list_two if both are lists, OR it compares elements of list_one 
    against the elements of list_two to find matches.

    Re-evaluating based on Example 1:
    L1: [1..14], L2: [[12..], [7..], [1..]]
    Result: [[12], [7, 11], [1, 5, 8]]
    Observation: 
      - Index 0 of L2 [12, 18...] shares 12 with L1. Result index 0 is [12].
      - Index 1 of L2 [7, 11...] shares 7, 11 with L1. Result index 1 is [7, 11].
      - Index 2 of L2 [1, 5...] shares 1, 5, 8 with L1. Result index 2 is [1, 5, 8].
      - Index 3 of L2 is not in L1? Or L1 is exhausted? L1 has 14 items, L2 has 3 lists.
      The result has 3 lists. It seems the function iterates over L2, 
      checks intersection with L1, and returns those intersections.
      BUT, Example 3 contradicts this simple "iterate L2" hypothesis because 
      the output length matches the length of L1 (4 elements), not L2 (4 lists).

    Re-evaluating based on Example 3:
    L1: ['john', 'amal', 'joel', 'george']
    L2: [['john'], ['jack','john','mary'], ['howard','john'], ['jude']]
    Result: [['john'], ['john'], ['john'], []]
    Observation:
      - Output index 0: 'john' (from L1[0]) matches elements in L2[0]? 
        L2[0] is ['john']. Intersection of {'john'} and {'john'} is {'john'}.
      - Output index 1: 'amal' (from L1[1]). L2[1] is ['jack','john','mary'].
        Does 'amal' exist in L2[1]? No. Result is ['john']? 
        Wait, the result is [['john'], ['john'], ['john'], []].
        If the logic was "intersection of L1[i] and L2[i]", then:
        i=0: L1[0]='john', L2[0]=['john']. Intersection? 'john' in ['john'] -> ['john'].
        i=1: L1[1]='amal', L2[1]=['jack','john','mary']. 'amal' not in L2[1]. -> [].
        But the expected result for index 1 is ['john']. This is confusing.

    Let's look closer at Example 3 result: [['john'], ['john'], ['john'], []]
    L1 has 4 items. L2 has 4 lists.
    L1 items: 'john', 'amal', 'joel', 'george'.
    L2 lists:
      0: ['john']
      1: ['jack', 'john', 'mary']
      2: ['howard', 'john']
      3: ['jude']

    Hypothesis A: For each item in L1, find how many times it appears in the corresponding 
    list in L2?
    'john' in L2[0] ('john') -> 1 time? -> ['john']
    'amal' in L2[1] -> 0 times? -> Should be [], but expected ['john'].

    Hypothesis B: The problem statement says "nested list elements which are present in another list".
    Maybe it means: For every list in L2, find what from L1 is in it.
    But Example 3 output length is 4 (length of L1).

    Let's reconsider Example 1 with Hypothesis B:
    L1: [1..14]
    L2: [ListA, ListB, ListC]
    Result: [ResultA, ResultB, ResultC]
    ResultA = [12] -> Intersection of L1 and ListA. Correct.
    ResultB = [7, 11] -> Intersection of L1 and ListB. Correct.
    ResultC = [1, 5, 8] -> Intersection of L1 and ListC. Correct.

    Now Example 3 with Hypothesis B:
    L1: ['john', 'amal', 'joel', 'george']
    L2: [List0, List1, List2, List3]
    Result: [R0, R1, R2, R3]
    R0 = Intersection(L1, List0) -> Intersection({'john','amal','joel','george'}, {'john'}) -> ['john'].
    R1 = Intersection(L1, List1) -> Intersection(..., {'jack','john','mary'}) -> ['john']. (Because 'john' is in L1).
    R2 = Intersection(L1, List2) -> Intersection(..., {'howard','john'}) -> ['john'].
    R3 = Intersection(L1, List3) -> Intersection(..., {'jude'}) -> [].
    Result: [['john'], ['john'], ['john'], []].

    This matches the expected output perfectly!

    Conclusion on Logic:
    The function iterates over the second list (list_two).
    For each element in list_two:
      1. Determine if the element is a list.
      2. If it is a list, compute the intersection of its elements with list_one.
      3. If it is NOT a list (unlikely given "nested list" prompt, but handled for robustness),
         treat it as a container with that single element and compute intersection with list_one.
      4. Append the resulting intersection list to the final result.

    Wait, what about Example 2?
    L1: [[2, 3, 1], [4, 5], [6, 8]]
    L2: [[4, 5], [6, 8]]
    Result: [[], []]

    Applying Logic:
    Iteration 1: Element of L2 is [4, 5].
       Intersection of L1 ([[2,3,1], [4,5], [6,8]]) and [4, 5].
       Does [4, 5] exist in L1? No, the elements of L1 are lists.
       Does 4 exist in L1? No.
       Does 5 exist in L1? No.
       Intersection is [].

    Iteration 2: Element of L2 is [6, 8].
       Intersection of L1 and [6, 8].
       Does 6 exist in L1? No.
       Does 8 exist in L1? No.
       Intersection is [].

    Result: [[], []]. Matches expected.

    Wait, there is a nuance in Example 1.
    L1 is a flat list of ints. L2 is a list of lists.
    In Example 2, L1 is a list of lists. L2 is a list of lists.

    The logic "Intersection of elements of list_two_item with list_one" works for both.
    However, the definition of "element" needs to be careful.
    If list_one is [[2, 3, 1], ...], and list_two_item is [4, 5].
    The elements of list_one are lists. The elements of list_two_item are ints.
    Intersection of sets of lists and ints is empty. This is correct.

    What if the types don't match? The set intersection handles it naturally.

    Refined Algorithm:
    1. Initialize empty result list.
    2. Iterate through each item in list_two (the second argument).
    3. For the current item:
       a. Prepare a list to collect matches.
       b. Iterate through each element in list_one.
       c. If the element from list_one is present in the current item (list_two_item):
          - Add that element to the match list.
          - Note: We are looking for elements OF list_one that are INSIDE list_two_item.
          - Wait, Example 1: L1=[1..14], L2_item=[12, 18]. 
            Element '12' is in L1. '12' is in L2_item. Match.
          - Example 2: L1=[[2,3,1], ...], L2_item=[4,5].
            Element [2,3,1] is in L1. Is [2,3,1] in [4,5]? No.
            Element [4,5] is in L1. Is [4,5] in [4,5]? Yes.
            So if L1 contained [4,5], it would match.
            In Example 2, L1 is [[2,3,1], [4,5], [6,8]]. 
            Does [4,5] exist in L1? YES.
            Does [4,5] exist in L2_item ([4,5])? YES.
            So why is the result [] for the first iteration of Example 2?

    Re-reading Example 2:
    assert intersection_nested_lists([[2, 3, 1], [4, 5], [6, 8]],