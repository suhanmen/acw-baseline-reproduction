def max_subarray_product(nums):
    """
    Find the maximum product of a contiguous subarray within the given list of integers.

    This function uses a dynamic programming approach that tracks both the maximum
    and minimum products ending at the current position. This is necessary because
    a negative number multiplied by a minimum (negative) product can yield a new
    maximum product.

    Args:
        nums (list[int]): A list of integers (can include negative numbers, zeros, and positives).

    Returns:
        int: The maximum product of any contiguous subarray.

    Raises:
        ValueError: If the input list is empty.
        TypeError: If the input is not a list or contains non-integer elements.
    """

    # Validate input type
    if not isinstance(nums, list):
        raise TypeError(f"Input must be a list, got {type(nums).__name__}")

    # Validate list elements are integers
    for i, num in enumerate(nums):
        if not isinstance(num, int):
            raise TypeError(f"All elements must be integers, element at index {i} is {type(num).__name__}")

    # Handle edge case: empty input
    if len(nums) == 0:
        raise ValueError("Input list cannot be empty")

    # Initialize result with the first element
    # This handles cases where the maximum product might be negative (if all numbers are negative)
    max_product = nums[0]
    min_product = nums[0]
    current_max = nums[0]
    current_min = nums[0]

    # Iterate through the rest of the array starting from the second element
    for i in range(1, len(nums)):
        num = nums[i]

        # If the current number is negative, swapping max and min handles the sign flip logic
        # effectively before calculation to avoid complex conditional logic later.
        if num < 0:
            temp = current_max
            current_max = current_min
            current_min = temp

        # Calculate potential new max and min values
        # Current number itself is a candidate (starting a new subarray)
        # Extending the previous max/min subarray is another candidate
        possible_max = max(num, current_max * num, current_min * num)
        possible_min = min(num, current_max * num, current_min * num)

        # Update the current tracking variables
        current_max = possible_max
        current_min = possible_min

        # Update the global maximum found so far
        if current_max > max_product:
            max_product = current_max

    return max_product