from typing import List, Tuple


def max_Product(nums: List[int]) -> Tuple[int, int]:
    """
    Finds a pair of integers in a list that produces the highest product.

    The function handles:
    - Positive integers: The highest product comes from the two largest positives.
    - Negative integers: The highest product can come from the two smallest 
      (most negative) negatives (e.g., -10 * -10 = 100).
    - Mixed integers: Compares the product of the two largest positives 
      against the product of the two smallest negatives.

    Args:
        nums: A list of integers.

    Returns:
        A tuple containing the two integers that yield the maximum product.

    Raises:
        ValueError: If the input list has fewer than two elements.
        TypeError: If the input is not a list or contains non-integer elements.
    """
    # Input Validation
    if not isinstance(nums, list):
        raise TypeError("Input must be a list of integers.")

    if len(nums) < 2:
        raise ValueError("Input list must contain at least two integers to form a pair.")

    for item in nums:
        if not isinstance(item, int):
            raise TypeError(f"All elements in the list must be integers. Found: {type(item)}")

    # If there are exactly two elements, that is our only choice.
    if len(nums) == 2:
        # Sort them to maintain a consistent order (smaller, larger)
        sorted_pair = sorted(nums)
        return (sorted_pair[0], sorted_pair[1])

    # To find the max product, we only care about the two largest numbers 
    # and the two smallest numbers (which could be large negatives).

    # Sorting the list allows us to easily access extremes.
    # Time Complexity: O(N log N)
    sorted_nums = sorted(nums)

    # The two smallest numbers (potential large negative product)
    smallest_1 = sorted_nums[0]
    smallest_2 = sorted_nums[1]

    # The two largest numbers (potential large positive product)
    largest_1 = sorted_nums[-1]
    largest_2 = sorted_nums[-2]

    # Calculate products
    product_from_smalles = smallest_1 * smallest_2
    product_from_largest = largest_1 * largest_2

    # Determine which product is higher
    if product_from_smallest > product_from_largest:
        # Return the negative pair
        # We return as (smaller_magnitude, larger_magnitude) logic?
        # The prompt examples show:
        # max_Product([0,-1,-2,-4,5,0,-6]) == (-4,-6)
        # Note: -4 is > -6, so order is (larger, smaller) in terms of value?
        # Actually, standard tuple order for (-4, -6) is (-4, -6).
        # Let's check the assertion: (-4, -6). -4 is greater than -6.
        # To match the assertion exactly, we order them.

        # In (-4, -6), -4 comes first.
        # Let's check the order of largest: (7, 8) -> 7 is smaller.
        # This suggests we should return (smaller_value, larger_value) or vice-versa?
        # Looking at max_Product([1,2,3]) == (2,3) -> (smaller, larger)
        # Looking at max_Product([0,-1,-2,-4,5,0,-6]) == (-4,-6) -> (-4 > -6) -> (larger, smaller)

        # Let's re-examine:
        # [1,2,3,4,7,0,8,4] -> Max is 7*8=56. Result (7, 8). 7 < 8.
        # [0,-1,-2,-4,5,0,-6] -> Max is -4*-6=24. Result (-4, -6). -4 > -6.
        # [1,2,3] -> Max is 2*3=6. Result (2, 3). 2 < 3.

        # Logic: It seems the return order is based on the original magnitude or 
        # simply the two numbers found. Let's ensure we return the values correctly.
        # If the product is from negatives, we want the two numbers that made it.
        # In the assertion (-4, -6), the numbers are -4 and -6.
        # Because -4 is "greater" than -6, they are returned in descending order?
        # No, if it was descending, (7, 8) would be (8, 7).
        # It seems the code should return the numbers such that the first 
        # is the one that appears 'closer' to 0? Or just specific order?

        # Actually, looking at the assertions again:
        # (7, 8) -> 7 is smaller than 8
        # (-4, -6) -> -4 is larger than -6
        # (2, 3) -> 2 is smaller than 3

        # Wait, the commonality is:
        # 7 is the "smaller" of the two largest positives.
        # -4 is the "larger" of the two smallest negatives.
        # 2 is the "smaller" of the two largest positives.

        # Let's look at indices in sorted_nums:
        # sorted_nums for [0,-1,-2,-4,5,0,-6] is [-6, -4, -1, 0, 0, 5]
        # The pair is (-6, -4). The assertion says (-4, -6).
        # That means it returns (index 1, index 0).

        # sorted_nums for [1,2,3,4,7,0,8,4] is [0, 1, 2, 3, 4, 4, 7, 8]
        # The pair is (7, 8). The assertion says (7, 8).
        # That means it returns (index -2, index -1).

        # Conclusion: It returns the pair in the order they appear in the sorted list 
        # BUT for the negative case, the assertion (-4, -6) is the REVERSE of 
        # the sorted order (-6, -4).

        # Let's re-read: max_Product([0,-1,-2,-4,5,0,-6]) == (-4,-6).
        # In sorted list [-6, -4, -1, 0, 0, 5], -4 is at index 1, -6 is at index 0.
        # So it's (sorted_nums[1], sorted_nums[0]).

        # Let's re-read: max_Product([1,2,3,4,7,0,8,4]) == (7,8).
        # In sorted list [0, 1, 2, 3, 4, 4, 7, 8], 7 is at index -2, 8 is at index -1.
        # So it's (sorted_nums[-2], sorted_nums[-1]).

        # This is inconsistent unless the rule is "The number with the smaller absolute value first".
        # |7| < |8| -> (7, 8)
        # |-4| < |-6| -> (-4, -6)
        # |2| < |3| -> (2, 3)
        # This logic holds perfectly!

        pair = (smallest_1, smallest_2)
    else:
        pair = (largest_2, largest_1)

    # Final ordering logic: Smallest absolute value first
    if abs(pair[0]) < abs(pair[1]):
        return (pair[0], pair[1])
    else:
        return (pair[1], pair[0])