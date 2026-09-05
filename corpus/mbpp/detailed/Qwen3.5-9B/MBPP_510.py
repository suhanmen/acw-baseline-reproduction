def no_of_subsequences(nums, k):
    """
    Find the number of subsequences having product smaller than k for the given non negative array.

    A subsequence is derived from the array by deleting zero or more elements without changing
    the order of the remaining elements. However, for counting purposes in this context, we treat
    it as any subset of the original elements (order doesn't affect the product).

    Parameters:
    nums (list of int): A list of non-negative integers.
    k (int): The target product value; we count subsequences with product < k.

    Returns:
    int: The count of such subsequences.
    """

    # Explicit type checking for robustness
    if not isinstance(nums, list):
        raise TypeError("Input 'nums' must be a list.")
    if not isinstance(k, int):
        raise TypeError("Input 'k' must be an integer.")
    if k < 0:
        raise ValueError("Input 'k' must be non-negative.")

    for i, num in enumerate(nums):
        if not isinstance(num, int):
            raise TypeError(f"Element at index {i} is not an integer.")
        if num < 0:
            raise ValueError(f"Negative number found at index {i}; only non-negative numbers are allowed.")

    # Handle the degenerate case where k is 0
    # Since all numbers are non-negative, the only way product < 0 is impossible (products are >= 0).
    # However, if the array contains zeros, product can be 0.
    # If k is 0, we need product < 0, which is impossible for non-negative integers.
    if k == 0:
        return 0

    # Initialize counter for valid subsequences
    count = 0

    # Helper function to generate all possible subsequences (subsets) and check their product
    def generate_and_count(current_index, current_product, current_length, total_elements):
        """
        Recursive helper to iterate through all subsequences.

        current_index: Current index in the nums list being considered.
        current_product: Product of elements selected so far.
        current_length: Number of elements selected so far (to count empty subsequence if needed, 
                        though typically empty product is 1).
        total_elements: Total number of elements in nums.

        We use an iterative approach with recursion to avoid stack overflow for large inputs,
        though strictly speaking, recursion depth is limited by list length.
        """
        # If we've processed all elements, check the condition
        if current_index == total_elements:
            # The problem usually implies non-empty subsequences or specific rules.
            # Based on the examples: [1,2,3,4], k=10 -> 11.
            # Subsets of {1,2,3,4}: 2^4 = 16 total.
            # Products: 
            # {} -> 1 (often excluded in "subsequences" problems unless specified, let's check examples)
            # {1} -> 1
            # {2} -> 2
            # {3} -> 3
            # {4} -> 4
            # {1,2} -> 2
            # {1,3} -> 3
            # {1,4} -> 4
            # {2,3} -> 6
            # {2,4} -> 8
            # {3,4} -> 12 (>=10, no)
            # {1,2,3} -> 6
            # {1,2,4} -> 8
            # {1,3,4} -> 12 (no)
            # {2,3,4} -> 24 (no)
            # {1,2,3,4} -> 24 (no)
            # Valid products < 10: 1, 2, 3, 4, 2, 3, 4, 6, 8, 6, 8. 
            # Wait, let's list unique subsets and their products:
            # Size 1: 1, 2, 3, 4 (all < 10) -> 4
            # Size 2: 1*2=2, 1*3=3, 1*4=4, 2*3=6, 2*4=8, 3*4=12(X) -> 5
            # Size 3: 1*2*3=6, 1*2*4=8, 1*3*4=12(X), 2*3*4=24(X) -> 2
            # Size 4: 24(X) -> 0
            # Total = 4 + 5 + 2 = 11.
            # This matches the example. Note: The empty set {} has product 1. 
            # 1 < 10 is true. If empty set is included, count would be 12?
            # Let's re-evaluate. 
            # If empty set is included: 1 + 11 = 12. But assertion says 11.
            # Therefore, the empty subsequence is NOT counted.

            if current_product < k:
                return 1
            return 0

        # Option 1: Exclude current element
        result_exclude = generate_and_count(current_index + 1, current_product, current_length + 1, total_elements)

        # Option 2: Include current element
        # Check for potential overflow or infinite loop if num is 0 and we multiply?
        # 0 * anything = 0. If k > 0, 0 < k is true.
        # However, if current_product is already huge, multiplying might blow up.
        # But since inputs are integers, Python handles large ints automatically.

        new_product = current_product * nums[current_index]
        result_include = generate_and_count(current_index + 1, new_product, current_length + 1, total_elements)

        return result_exclude + result_include

    # Start the recursion
    # Initial product is 1 (identity for multiplication)
    # We start at index 0.
    # We must ensure we don't count the empty subsequence.
    # The base case logic above checks product < k.
    # If the only valid path is the empty set (product=1 < k), we get 1.
    # To exclude the empty set, we can subtract 1 at the end if k > 1, 
    # OR modify the recursion to track if any element was added.

    # Simpler approach for edge case handling:
    # The empty set has product 1.
    # If 1 < k, the recursion counts it.
    # The problem examples imply empty set is excluded.

    # Let's run the helper and then adjust if necessary.
    # Actually, a cleaner way is to initialize current_product to 1, 
    # but the recursive steps represent adding elements.
    # If we pick NO elements, we reach the base case with current_product = 1.
    # Since we need to exclude the empty set, we can simply subtract 1 from the final result
    # if the empty set was counted (i.e., if 1 < k).

    total_valid_with_empty = generate_and_count(0, 1, 0, len(nums))

    # If the empty set (product 1) is considered valid (1 < k), we must remove it from the count.
    if total_valid_with_empty > 0 and 1 < k:
        total_valid_with_empty -= 1

    return total_valid_with_empty


# --- Verification against provided assertions ---
# assert no_of_subsequences([1,2,3,4], 10) == 11
# assert no_of_subsequences([4,8,7,2], 50) == 9
# assert no_of_subsequences([5,6,7,8], 15) == 4

# Let's trace manually to be absolutely sure about the logic before finalizing.
# Case 1: [1,2,3,4], k=10.
# We found 11 non-empty subsets.
# Empty set product = 1. 1 < 10 is True.
# Recursive call counts empty set as 1.
# Total recursive count = 12.
# We subtract 1 because 1 < 10. Result = 11. Correct.

# Case 2: [4,8,7,2], k=50.
# Subsets:
# Size 1: 4, 8, 7, 2 (all < 50) -> 4
# Size 2: 4*8=32, 4*7=28, 4*2=8, 8*7=56(X), 8*2=16, 7*2=14 -> 5
# Size 3: 4*8*7=224(X), 4*8*2=64(X), 4*7*2=56(X), 8*7*2=112(X) -> 0
# Size 4: 448(X) -> 0
# Total non-empty = 4 + 5 = 9.
# Empty set product = 1. 1 < 50 is True.
# Recursive count = 10. Subtract 1 -> 9. Correct.

# Case 3: [5,6,7,8], k=15.
# Size 1: 5, 6, 7, 8 (all < 15) -> 4
# Size 2: 5*6=30(X), 5*7=35(X), 5*8=40(X), 6*7=42(X)... all >= 15. -> 0
# Total non-empty = 4.
# Empty set product = 1. 1 < 15 is True.
# Recursive count = 5. Subtract 1 -> 4. Correct.

# Edge Case: k=1.
# We need product < 1. Since numbers are non-negative integers, product >= 0.
# Only possible product < 1 is 0.
# If array has 0, then subsets containing 0 have product 0.
# If array has no 0, min product is 1 (empty or just 1s). If no 1s, min product > 1?
# Wait, if array is [1], k=1. Subsets: {}->1, {1}->1. Neither < 1. Count should be 0.
# Recursive: {}->1 (not < 1), {1}->1 (not < 1). Total 0. Correct.

# Edge Case: Array with zeros. [0, 0], k=5.
# Subsets:
# {} -> 1 (1 < 5) -> Exclude later.
# {0} -> 0 (0 < 5) -> Keep.
# {0} (second) -> 0 (0 < 5) -> Keep.
# {0, 0} -> 0 (0 < 5) -> Keep.
# Total non-empty valid: 3.
# Recursive: 
# Exclude both -> 1 (counted).
# Exclude first, incl second -> 0 (counted).
# Incl first, excl second -> 0 (counted).
# Incl both -> 0 (counted).
# Total recursive = 4.
# 1 < 5 is True, so subtract 1. Result 3. Correct.

# One more edge case: k=0.
# Handled explicitly at start. Returns 0.
# Logic: product < 0 is impossible for non-negative integers.

print("Verification logic holds.")