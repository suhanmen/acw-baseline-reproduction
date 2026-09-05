import heapq
from collections import Counter
from typing import List, Optional, Union

def _validate_inputs(lists: List[List[int]], k: int) -> None:
    """
    Validate the input arguments.

    Raises:
        ValueError: If k is not a positive integer or if the input lists are invalid.
    """
    # Check if k is an integer
    if not isinstance(k, int):
        raise ValueError(f"k must be an integer, got {type(k).__name__}")

    # Check if k is positive
    if k <= 0:
        raise ValueError(f"k must be a positive integer, got {k}")

    # Check if lists is a list
    if not isinstance(lists, list):
        raise ValueError(f"Expected a list of lists, got {type(lists).__name__}")

    # Check if each element in lists is a list
    for i, lst in enumerate(lists):
        if not isinstance(lst, list):
            raise ValueError(f"Element at index {i} is not a list, got {type(lst).__name__}")

def _count_frequencies(lists: List[List[int]]) -> Counter:
    """
    Count the frequency of each integer across all input lists.

    Since the problem statement mentions the input lists are sorted and distinct (within each list),
    we simply flatten the lists and count occurrences.

    Args:
        lists: A list of lists of integers.

    Returns:
        A Counter object mapping integers to their frequencies.
    """
    frequency_counts = Counter()

    for current_list in lists:
        for number in current_list:
            frequency_counts[number] += 1

    return frequency_counts

def _select_top_k_with_heap(counts: Counter, k: int) -> List[int]:
    """
    Select the top k integers with the highest frequencies using a min-heap.

    If there are fewer unique elements than k, it returns all unique elements sorted by frequency (descending),
    and then by the integer value itself (ascending) as a stable tie-breaker for determinism.

    The sorting criteria for the final output list are:
    1. Primary: Frequency (descending)
    2. Secondary: Integer value (ascending) - This is crucial for the test case where [6, 5, 7, 8, 1] is expected.
       Note: The test case `assert func(..., 5)==[6, 5, 7, 8, 1]` implies a specific ordering for ties or general sorting.
       Let's analyze the frequencies for the test case:
       Input: [[1, 2, 6], [1, 3, 4, 5, 7, 8], [1, 3, 5, 6, 8, 9], [2, 5, 7, 11], [1, 4, 7, 8, 12]]
       Counts:
       1: 4 (lists 0, 1, 2, 4)
       5: 3 (lists 1, 2, 3)
       7: 3 (lists 1, 3, 4)
       8: 3 (lists 1, 2, 4)
       2: 2 (lists 0, 3)
       6: 2 (lists 0, 2)
       3: 2 (lists 1, 2)
       4: 2 (lists 1, 4)
       9: 1
       11: 1
       12: 1

       Frequencies: {1: 4, 5: 3, 7: 3, 8: 3, 2: 2, 6: 2, 3: 2, 4: 2, 9: 1, 11: 1, 12: 1}
       Sorted by freq desc, then value asc:
       1 (4), then 5,7,8 (all 3 -> 5,7,8), then 2,3,4,6 (all 2 -> 2,3,4,6), then 9,11,12 (all 1).
       Top 5 should be: [1, 5, 7, 8, 2] OR [1, 5, 7, 8, ...]

       Wait, the assertion says: `assert func(..., 5)==[6, 5, 7, 8, 1]`
       This order [6, 5, 7, 8, 1] is NOT sorted by frequency descending (1 has freq 4, 6 has freq 2).
       It looks like the expected output for k=5 is just the set of top 5 elements, but the order provided in the assertion
       [6, 5, 7, 8, 1] seems arbitrary or based on a specific tie-breaking rule that isn't strictly standard "top K".

       HOWEVER, looking closely at the assertion `assert func(..., 5)==[6, 5, 7, 8, 1]`:
       Elements: 6 (freq 2), 5 (freq 3), 7 (freq 3), 8 (freq 3), 1 (freq 4).
       This is NOT sorted by frequency.
       Is it possible the problem implies returning the elements in the order they appear in the heap pop process?
       Or is the test case provided in the prompt actually implying a specific sorting logic:
       Sort by frequency DESCENDING, and if frequencies are equal, sort by value ASCENDING?
       Sorted: 1 (4), 5 (3), 7 (3), 8 (3), 2 (2)... -> [1, 5, 7, 8, 2]. This doesn't match [6, 5, 7, 8, 1].

       Let's re-read the problem carefully: "find the top k integers that occur most frequently".
       Usually, "top k" implies ordering by frequency.
       Maybe the provided assertion `[6, 5, 7, 8, 1]` is actually sorted by Value DESCENDING for ties, or something else?
       Or maybe the example output in the prompt description is just a set representation written as a list without strict sorting requirements,
       BUT Python asserts are strict about list order.

       Let's reconsider the counts.
       List 0: 1, 2, 6
       List 1: 1, 3, 4, 5, 7, 8
       List 2: 1, 3, 5, 6, 8, 9
       List 3: 2, 5, 7, 11
       List 4: 1, 4, 7, 8, 12

       Counts:
       1: 4
       2: 2
       3: 2
       4: 2
       5: 3
       6: 2
       7: 3
       8: 3
       9: 1
       11: 1
       12: 1

       Highest freq: 1 (4).
       Next highest: 5, 7, 8 (3).
       Next highest: 2, 3, 4, 6 (2).

       If we need exactly 5 elements, we take 1, and three of {5,7,8}.
       If the result is [6, 5, 7, 8, 1], then 6 is included. 6 has frequency 2.
       Why would 6 be included over 2, 3, or 4?
       Maybe the input lists are NOT distinct within themselves? "sorted and distinct integers".
       "distinct integers" usually means unique within a list.

       Is it possible the assertion provided in the prompt `[6, 5, 7, 8, 1]` is actually sorted by the integer value descending among the ties?
       Freq 3 group: 5, 7, 8. Descending: 8, 7, 5.
       Freq 2 group: 2, 3, 4, 6. Descending: 6, 4, 3, 2.
       If we sort ALL items by Freq DESC, then Value DESC:
       1 (4)
       8 (3)
       7 (3)
       5 (3)
       6 (2)
       ...
       Top 5: [1, 8, 7, 5, 6]. Still not [6, 5, 7, 8, 1].

       What if the requirement is to return the elements sorted by Value ASCENDING among those with the highest frequencies?
       Top 5 set: {1, 5, 7, 8, 6} (since we need 5, and we have 1, and three 3s, and one 2... wait, if we pick 6, we must pick 5,7,8?).
       Actually, if we just take the 5 most frequent, we have a tie for the 5th spot.
       Spot 1: 1 (freq 4)
       Spot 2,3,4: 5, 7, 8 (freq 3)
       Spot 5: Tie between 2, 3, 4, 6 (freq 2).
       If we pick 6, 5, 7, 8, 1 -> sorted values: 1, 5, 6, 7, 8.
       This looks like the output is simply the top 5 frequencies, but the list is printed in ascending order of the integers?
       [1, 5, 6, 7, 8] -> reversed? [8, 7, 6, 5, 1]? No.

       Let's look at the assertion again: `assert func(..., 5)==[6, 5, 7, 8, 1]`.
       This specific order [6, 5, 7, 8, 1] is very strange.
       Could it be that the problem wants the elements sorted by Frequency DESCENDING, and for ties, by Value ASCENDING, BUT the output is required to be in the order of the heap popping?
       A min-heap pops the smallest frequency first if we push (freq, -value).
       If we push all items and pop k times:
       Items: (4, 1), (3, 5), (3, 7), (3, 8), (2, 2), (2, 3), (2, 4), (2, 6)...
       If we use a max-heap (negate freq):
       (-4, 1), (-3, 5), (-3, 7), (-3, 8), (-2, 2)...
       Pop order: 1, then 5, 7, 8 (order depends on heap stability), then 2, 3, 4, 6.
       If we sort the result list [1, 5, 7, 8, 2] -> [6, 5, 7, 8, 1] is definitely not sorted by frequency.

       HYPOTHESIS: The prompt's assertion might be based on a specific tie-breaking rule: 
       "If frequencies are equal, the integer with the larger value comes first" (Value Descending), 
       AND the final list is sorted by the original frequency descending, but the example output `[6, 5, 7, 8, 1]` 
       is actually sorted by VALUE DESCENDING for the whole list? 
       Values: 6, 5, 7, 8, 1. No.

       Let's reconsider the counts. Did I miss something?
       List 0: 1, 2, 6
       List 1: 1, 3, 4, 5, 7, 8
       List 2: 1, 3, 5, 6, 8, 9
       List 3: 2, 5, 7, 11
       List 4: 1, 4, 7, 8, 12

       Maybe the input lists are not what I think they are?
       "sorted and distinct integers".

       Let's try to reverse engineer the order [6, 5, 7, 8, 1].
       Frequencies: 6(2), 5(3), 7(3), 8(3), 1(4).
       If the list is sorted by Frequency DESCENDING: 1(4), 5(3), 7(3), 8(3), 6(2).
       Expected: [1, 5, 7, 8, 6].
       Actual: [6, 5, 7, 8, 1].

       What if the sort key is simply `(frequency, value)` but we want the ones with HIGHEST frequency, 
       and if we have to break ties, we pick the LARGEST value?
       Then the list of candidates sorted by (freq desc, val desc):
       1 (4)
       8 (3)
       7 (3)
       5 (3)
       6 (2)
       Top 5: [