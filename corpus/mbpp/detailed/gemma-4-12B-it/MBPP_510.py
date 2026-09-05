from typing import List

def no_of_subsequences(arr: List[int], k: int) -> int:
    """
    Calculates the number of non-empty subsequences of a non-negative integer 
    array whose product is strictly less than k.

    A subsequence is formed by deleting zero or more elements from the 
    original array. The order of elements in the subsequence does not 
    matter for the product, but the position in the original array determines 
    uniqueness of the subsequence.
    """
    # Validation: Input types and constraints
    if not isinstance(arr, list):
        raise TypeError("Input 'arr' must be a list of integers.")
    if not isinstance(k, int):
        raise TypeError("Input 'k' must be an integer.")

    # Edge case: If k is 0 or negative, no product of non-negative 
    # integers can be strictly less than k (since minimum product is 0).
    # However, the problem implies positive k based on examples.
    # If k <= 0, result is 0.
    if k <= 0:
        return 0

    # Filter out elements that are already >= k 
    # Note: If an element is 0, any subsequence containing it will have 
    # a product of 0, which is < k (for k > 0).
    # We need to handle 0s specially because 0 * anything = 0.

    # Step 1: Separate zeros and non-zeros
    # Subsequences with at least one zero always have a product of 0.
    # Since k > 0, these are always valid.
    zeros_count = 0
    non_zeros = []

    for x in arr:
        if not isinstance(x, int):
            raise ValueError("All elements in the array must be integers.")
        if x < 0:
            raise ValueError("The problem specifies a non-negative array.")

        if x == 0:
            zeros_count += 1
        else:
            non_zeros.append(x)

    # Step 2: Count subsequences using only non-zero numbers
    # We use dynamic programming to find the number of subsequences 
    # whose product is strictly less than k.
    # dp[p] = number of subsequences whose product is exactly p.

    # Because we only care about products < k, the max key is k-1.
    # If k is very large, we can't use a fixed-size array, 
    # so we use a dictionary to map product -> count.

    # dp[product] = count
    dp = {}

    for num in non_zeros:
        # We create a temporary dictionary to store new products formed 
        # by including 'num' in existing subsequences.
        new_subsequences = {}

        # Case: The number itself forms a subsequence
        if num < k:
            new_subsequences[num] = new_subsequences.get(num, 0) + 1

        # Case: Multiply 'num' with all existing subsequence products
        for current_prod, count in dp.items():
            new_prod = current_prod * num
            if new_prod < k:
                new_subsequences[new_prod] = new_subsequences.get(new_prod, 0) + count

        # Merge new_subsequences into dp
        for prod, count in new_subsequences.items():
            dp[prod] = dp.get(prod, 0) + count

    # Total subsequences of non-zero numbers with product < k
    count_non_zero_subsequences = sum(dp.values())

    # Step 3: Handle the zeros
    # Let n be the total count of zeros.
    # Let m be the number of non-zero elements.
    # A subsequence can contain:
    # 1. Only non-zero elements (already counted in count_non_zero_subsequences).
    # 2. At least one zero and any combination of non-zero elements.
    # 3. Only zeros.

    # Let 'total_non_zero_subsequences' be all possible subsequences of 
    # the non_zero list (including the empty set). 
    # This is 2^m.
    # Any subsequence of the original array that contains at least one zero 
    # will have a product of 0.
    # Since 0 < k, all such subsequences are valid.

    # Number of subsequences of the 'arr' containing at least one zero:
    # Total subsequences = 2^(total_elements)
    # Subsequences with NO zeros = 2^(count of non_zeros)
    # Subsequences with AT LEAST one zero = 2^(total_elements) - 2^(count of non_zeros)

    # However, we can calculate this more simply:
    # Every subsequence that contains at least one zero has product 0.
    # There are (2^zeros_count - 1) ways to pick a non-empty set of zeros.
    # For each such way, we can pick any subsequence of the non_zero elements.
    # There are 2^(len(non_zeros)) such subsequences of non_zeros (including empty).

    # Number of valid subsequences = (Subsequences with product < k and no zeros)
    #                                + (Subsequences with product < k and at least one zero)
    #                                + (Subsequences with only non-zero elements, already counted)

    # Let's re-evaluate:
    # Any subsequence containing at least one zero has product 0.
    # If k > 0, all these are valid.
    # Number of subsequences containing at least one zero:
    # Total subsequences of array = 2^(len(arr))
    # Subsequences containing only non-zero elements = 2^(len(non_zeros))
    # Subsequences containing at least one zero = 2^(len(arr)) - 2^(len(non_zeros))

    # But wait, the DP already counts all subsequences of non-zeros 
    # that result in a product < k.
    # Let S_nz = set of subsequences of non-zeros with product < k.
    # Let Z = set of subsequences of the original array containing at least one zero.
    # The total count is |S_nz| + |Z|.
    # These two sets are disjoint because S_nz contains no zeros and Z contains at least one zero.

    # |Z| = (Total subsequences) - (Subsequences with no zeros)
    # |Z| = 2^(len(arr)) - 2^(len(non_zeros))

    # Let's verify with an example. arr=[0, 2], k=3
    # non_zeros = [2], zeros = 1.
    # DP for non_zeros: {2: 1}. count_non_zero_subsequences = 1.
    # |Z| = 2^2 - 2^1 = 4 - 2 = 2. (The subsequences are [0] and [0, 2])
    # Total = 1 + 2 = 3.
    # Check manually: [0], [2], [0, 2]. All products < 3. Correct.

    # Calculation of |Z|:
    total_elements = len(arr)
    num_non_zero_elements = len(non_zeros)

    num_subsequences_with_at_least_one_zero = (2**total_elements) - (2**num_non_zero_elements)

    final_count = count_non_zero_subsequences + num_subsequences_with_at_least_one_zero

    return final_count