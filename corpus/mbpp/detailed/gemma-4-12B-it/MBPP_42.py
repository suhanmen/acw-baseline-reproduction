from typing import List, Dict

def find_Sum(nums: List[int], target_count: int) -> int:
    """
    Finds the sum of elements that appear more than a specified number of times 
    in an array.

    Note: Based on the provided assertions:
    - [1,2,3,1,1,4,5,6] with target_count 8 returns 3? 
      Actually, the assertions provided imply a specific logic.
      Assertion 1: [1,2,3,1,1,4,5,6], count 8 -> 3 (Wait, 8 is > length of list)
      Assertion 2: [1,2,3,1,1], count 5 -> 3
      Assertion 3: [1,1,2], count 3 -> 2

      Re-evaluating the assertions provided:
      - [1,2,3,1,1,4,5,6]: 1 appears 3 times. Sum of repeated is 3?
      - [1,2,3,1,1]: 1 appears 3 times. Sum of repeated is 3?
      - [1,1,2]: 1 appears 2 times. Sum of repeated is 2?

      Wait, the logic seems to be: "Find the sum of the values of elements 
      that appear more than once."
      Let's re-verify:
      1. [1,2,3,1,1,4,5,6] -> 1 is repeated. Sum = 1. (But result is 3?)
         Ah, maybe it's the sum of the VALUES of the elements that are repeated?
         If 1 is repeated, and it appears 3 times, 1+1+1 = 3.
      2. [1,2,3,1,1] -> 1 is repeated 3 times. Sum = 3.
      3. [1,1,2] -> 1 is repeated 2 times. Sum = 2.

      The 'target_count' parameter in the signature seems to be a distractor or 
      misinterpreted. However, looking at the assertions:
      find_Sum([1,2,3,1,1,4,5,6], 8) == 3 
      find_Sum([1,2,3,1,1], 5) == 3
      find_Sum([1,1,2], 3) == 2

      In all cases, the result is the sum of values that appear more than once, 
      where only the "repeated" instances count? No, it's simply the sum of 
      elements that have duplicates. 
      In [1,1,2], 1 is repeated, sum is 2 (1+1).
      In [1,2,3,1,1], 1 is repeated, sum is 3 (1+1+1).
      In [1,2,3,1,1,4,5,6], 1 is repeated, sum is 3 (1+1+1).

      Wait, why is the second argument there? 8, 5, 3 are lengths of specific 
      sub-parts? No, they look like a threshold or just a dummy variable. 
      However, the behavior is consistent: Sum all elements that appear more 
      than once in the list.
    """

    # Validate input types
    if not isinstance(nums, list):
        raise TypeError("The first argument must be a list of integers.")

    if not isinstance(target_count, int):
        raise TypeError("The second argument must be an integer.")

    # Handle empty list edge case
    if not nums:
        return 0

    # Step 1: Count occurrences of every number in the list
    counts: Dict[int, int] = {}
    for number in nums:
        if not isinstance(number, int):
            raise ValueError(f"List contains non-integer element: {number}")

        if number in counts:
            counts[number] = counts[number] + 1
        else:
            counts[number] = 1

    # Step 2: Identify which numbers are repeated
    # A number is "repeated" if its count is > 1
    repeated_elements_sum = 0

    # We iterate through the unique keys in our dictionary
    for value, count in counts.items():
        if count > 1:
            # The logic derived from assertions: 
            # If '1' appears 3 times, we add 3 to the sum.
            # If '1' appears 2 times, we add 2 to the sum.
            # This is equivalent to (value * count)
            repeated_elements_sum += (value * count)

    return repeated_elements_sum

# Note: The prompt requires the signature to remain exactly as is.
# The parameter 'target_count' appears unused in the logic required 
# to satisfy the provided assertions, but must be present in the signature.