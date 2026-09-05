from typing import List, Union, Tuple

Number = Union[int, float]

def validate_input(
    array: List[Number],
    operation_count: int,
    removal_index: int
) -> Tuple[bool, str]:
    """
    Validates the inputs against the problem requirements.

    Returns:
        Tuple[bool, str]: A tuple containing (is_valid, error_message).
                          If is_valid is True, error_message is an empty string.
    """
    # Check if array is None
    if array is None:
        return False, "Input array cannot be None."

    # Check if operation_count is negative
    if operation_count < 0:
        return False, "Operation count cannot be negative."

    # Check if removal_index is negative
    if removal_index < 0:
        return False, "Removal index cannot be negative."

    # Check if removal_index is out of bounds relative to the current array size
    # The problem implies we are removing 'operation_count' elements.
    # The indices 0, 1, ... removal_index must be valid within the array bounds.
    # Specifically, the last removed element is at 'removal_index' in the ORIGINAL array?
    # Or is 'removal_index' relative to the state after some removals?
    # Looking at the examples:
    # [2,5,4], 3, 2 -> Returns 2. (Index 2 is '4')
    # [4,3], 2, 2 -> Returns 2. (Index 2 is out of bounds for length 2 originally, 
    #   but if we remove 2 elements from [4,3], we have [4], remove index 0? 
    #   Wait, let's re-analyze the logic based on the examples provided.)

    # Analysis of Example 1: get_Position([2,5,4], 3, 2) == 2
    # Array: [2, 5, 4]
    # Operation count: 3. Total elements = 3.
    # Removal index: 2.
    # Result: 2.
    # Hypothesis: We simulate removing elements one by one. 
    # If we remove 3 elements from a list of 3 elements.
    # Step 1: Remove index 0 (value 2). Array becomes [5, 4]. Last removed position relative to CURRENT array was 0.
    # Step 2: Remove index 0 (value 5). Array becomes [4]. Last removed position relative to CURRENT array was 0.
    # Step 3: Remove index 0 (value 4). Array becomes []. Last removed position relative to CURRENT array was 0.
    # This doesn't match the return value 2.

    # Let's try the interpretation: "removal_index" is the index in the ORIGINAL array of the last removed element.
    # If we remove 'operation_count' elements sequentially from the START (index 0), 
    # then the elements removed are at original indices: 0, 1, ..., operation_count-1.
    # The LAST removed element would be at original index = operation_count - 1.
    # Example 1: op_count=3. Last removed index = 3-1 = 2. Matches return 2.
    # Example 2: [4,3], 2, 2. op_count=2. Last removed index = 2-1 = 1. 
    #   But the expected output is 2. 
    #   Original array length is 2. Indices are 0, 1.
    #   How can we return 2? 
    #   Maybe 'removal_index' is not "index to remove" but "the index we are asking about"?
    #   Re-reading the prompt: "find the position of the last removed element from the given array".
    #   Arguments: array, operation_count, removal_index.
    #   In Ex 2: array=[4,3], op=2, rem_idx=2. Output=2.
    #   If we remove 2 elements from [4,3]. 
    #   Maybe the logic is: We remove elements starting from index `removal_index`?
    #   If we start removing from index 2 (which doesn't exist initially), maybe it wraps? No, unlikely.
    #   Maybe `removal_index` specifies WHICH element is the "last removed" in a sequence of removals defined by `operation_count`?

    # Let's look at Example 3: [1,2,3,4], 4, 1 -> Returns 4.
    # Op count 4. Array length 4.
    # If we remove all 4 elements starting from index 0, the last one removed is at original index 3.
    # But output is 4? 
    # This is confusing. Let's reconsider the parameters.
    # get_Position(array, operation_count, removal_index)
    # Maybe `removal_index` is not an index into the array, but a parameter defining the "current head" or something?

    # Alternative Theory: The problem is about a deque or a stack where we remove elements.
    # Let's look at the return values again.
    # 1. [2,5,4], 3, 2 -> 2.
    # 2. [4,3], 2, 2 -> 2.
    # 3. [1,2,3,4], 4, 1 -> 4.

    # Observation:
    # In Ex 1, removal_index (2) is the answer.
    # In Ex 2, removal_index (2) is the answer.
    # In Ex 3, removal_index (1) is NOT the answer (answer is 4).

    # Wait, could the function return the index in the ORIGINAL array?
    # Ex 3: Op=4. We remove 4 items.
    # If we remove items one by one from the FRONT (standard queue):
    # Remove 1st (orig idx 0).
    # Remove 2nd (orig idx 1).
    # Remove 3rd (orig idx 2).
    # Remove 4th (orig idx 3).
    # Last removed original index = 3. Output says 4.

    # What if we remove from the END?
    # Remove 1st (orig idx 3).
    # Remove 2nd (orig idx 2).
    # Remove 3rd (orig idx 1).
    # Remove 4th (orig idx 0).
    # Last removed original index = 0. Output says 4.

    # Let's re-read carefully: "position of the last removed element".
    # Maybe the "position" refers to the 1-based index in the original array?
    # Ex 1: Orig indices 1, 2, 3. Values 2, 5, 4.
    #   If we remove 3 items from front. Last removed is '4'. Original 1-based index = 3. Output 2. No.
    #   If we remove 3 items from back. Last removed is '2'. Original 1-based index = 1. Output 2. No.

    # Let's try to interpret `removal_index` as the starting point of removal?
    # Ex 1: Start removal at index 2 (value 4). Remove 3 times?
    #   List: [2, 5, 4]. Start at 2. Remove 4. List: [2, 5]. Next remove from start? Or continue?
    #   If circular: Remove 4 (idx 2), then 5 (idx 0), then 2 (idx 1). Last removed is 2 (orig idx 0). Output 2. No.

    # Let's look at the function name: `get_Position`.
    # Arguments: array, operation_count, removal_index.
    # Is it possible `removal_index` is simply the index we want to know the position of AFTER some operations?
    # But the description says "position of the last removed element".

    # Let's reconsider the examples with a different perspective.
    # Maybe the "removal_index" parameter indicates how many elements were removed *before* the operation count? No.

    # Let's try to reverse engineer the math.
    # Case 1: len=3, ops=3, rem_idx=2 -> res=2.
    # Case 2: len=2, ops=2, rem_idx=2 -> res=2.
    # Case 3: len=4, ops=4, rem_idx=1 -> res=4.

    # Is it possible the function returns `removal_index` if `operation_count` equals `len(array)`?
    # Ex 1: 3 == 3. Returns 2. (matches rem_idx)
    # Ex 2: 2 == 2. Returns 2. (matches rem_idx)
    # Ex 3: 4 == 4. Returns 4. (matches operation_count, NOT rem_idx which is 1)
    # So if full removal happens, it returns something else in Ex 3.

    # What if the logic is: 
    # We remove `operation_count` elements. 
    # The "last removed element" is identified by the parameter `removal_index`.
    # But `removal_index` seems to be the target answer in Ex 1 and Ex 2, but not Ex 3.
    # In Ex 3, the answer is 4. `removal_index` is 1. `operation_count` is 4.
    # Maybe `removal_index` is 1-based? If 1-based, Ex 3 -> `removal_index`=1 means start removing from index 0?

    # Let's try a specific algorithm often used in these types of problems: 
    # "Josephus Problem" variation? No, too complex for these simple asserts.
    # "Stack" operations?

    # Let's try this logic:
    # We have an array. We perform `operation_count` removals.
    # The removals happen starting from index `removal_index`.
    # BUT, if the index goes out of bounds, we wrap around or shift?

    # Let's try: The `removal_index` is the index of the element that was JUST removed?
    # No, we need to calculate it.

    # Let's look at Ex 3 again: [1,2,3,4], 4, 1 -> 4.
    # If we remove 1 element starting at index 1 (value 2). List: [1, 3, 4].
    # Then remove 2nd element from... where?

    # WAIT. Is it possible the problem is simpler?
    # "Find the position of the last removed element".
    # Maybe the "removal_index" parameter is actually the INDEX in the CURRENT array at the time of removal?
    # And `operation_count` is just noise? No, that violates the "production grade" expectation to use all inputs.

    # Let's reconsider the "1-based indexing" hypothesis for the RETURN VALUE.
    # If the function returns 0-based index:
    # Ex 1: Returns 2 (value 4).
    # Ex 2: Returns 2. But list has length 2. Index 2 is out of bounds (0, 1).
    #   UNLESS it returns 1-based index?
    #   If 1-based: Ex 2 returns 2. (Value 3, which is at index 1).
    #   Ex 1 returns 2. (Value 5, which is at index 1? Or Value 4 at index 2?)
    #   If 1-based, value 5 is pos 2. Value 4 is pos 3.
    #   If we remove 3 items from [2,5,4].
    #   Remove 2 (pos 1). Remove 5 (pos 2). Remove 4 (pos 3). Last removed is 4 (pos 3).
    #   Assert says 2. So not 1-based index of value 4.

    # Let's go back to the most straightforward interpretation that fits Ex 2 and Ex 3 partially.
    # Ex 2: Input [4,3], ops=2, rem_idx=2. Output 2.
    # Note: `removal_index` == Output.
    # Ex 1: Input [2,5,4], ops=3, rem_idx=2. Output 2.
    # Note: `removal_index` == Output.
    # Ex 3: Input [1,2,3,4], ops=4, rem_idx=1. Output 4.
    # Note: `removal_index` != Output. `operation_count` == Output.

    # Why the difference?
    # In Ex 1 and 2, `removal_index` >= `operation_count`? 
    #   Ex 1: 2 >= 3? False.
    #   Ex 2: 2 >= 2? True.
    #   Ex 3: 1 >= 4? False.

    # Maybe the `removal_index` indicates the number of elements to SKIP before starting removals?
    # Ex 1: Skip 2 elements [2, 5]. Start removing from index 2 (value 4).
    #   Remove 4. List [2, 5].
    #   Next removal? From where?