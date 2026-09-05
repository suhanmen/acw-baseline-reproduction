from typing import Tuple, Union

Number = Union[int, float]

def validate_input(
    first_term: Number,
    last_term: Number,
    common_ratio: Number
) -> Tuple[Number, Number, Number]:
    """
    Validates that all inputs are finite numbers and returns them.
    Raises ValueError if any input is invalid.
    """
    if not (isinstance(first_term, (int, float)) and isinstance(last_term, (int, float)) and isinstance(common_ratio, (int, float))):
        raise ValueError("All inputs must be numbers (int or float).")

    if not (float('inf') != first_term and float('inf') != last_term and float('-inf') != first_term and 
            float('inf') != last_term and float('-inf') != last_term and
            float('inf') != common_ratio and float('-inf') != common_ratio):
        raise ValueError("All inputs must be finite numbers.")

    return first_term, last_term, common_ratio

def calculate_geometric_series_sum(
    first_term: Number,
    last_term: Number,
    common_ratio: Number
) -> Number:
    """
    Calculates the sum of a geometric progression.

    Given:
    - first_term (a): The first term
    - last_term (l): The last term
    - common_ratio (r): The common ratio

    Returns the sum of the series: a + ar + ar^2 + ... + ar^(n-1)

    Special case handling:
    - If r == 1: Sum is n * a
    - If r != 1: Sum is a * (r^n - 1) / (r - 1)
      where n is the number of terms derived from l = a * r^(n-1)
    """

    # Determine the number of terms (n)
    # Since we have the last term, we can find n by working backwards
    # l = a * r^(n-1)
    # l/a = r^(n-1)
    # ln(l/a) = (n-1) * ln(r)
    # n-1 = ln(l/a) / ln(r)
    # n = ln(l/a) / ln(r) + 1

    if common_ratio == 1:
        # Case where ratio is 1: all terms are equal to first_term
        if first_term == 0:
            return 0

        # Calculate number of terms needed to reach last_term (should be 1 if ratio is 1 and terms are equal)
        # If ratio is 1, last_term must equal first_term for a valid GP with this definition
        if last_term != first_term:
            raise ValueError("When common_ratio is 1, first_term must equal last_term for a valid geometric progression.")

        # Number of terms is derived from the fact that all terms are equal
        # We need to find n such that the series makes sense. 
        # However, the problem implies we sum the sequence starting at 'first_term' 
        # with ratio 'common_ratio' until we reach/exceed 'last_term'.
        # If ratio is 1 and first_term == last_term, it's just one term? 
        # Or does it imply an arbitrary length? 
        # Looking at the examples: sum_gp(1,5,2) -> 1+2+4+8+16 = 31 (5 terms)
        # sum_gp(1,5,4) -> 1+4+16+64 (stops before 64? No, 1+4+16 = 21 != 341)
        # Let's re-examine the examples to understand the "last_term" definition.

        # Example 1: a=1, l=5, r=2. Sum=31.
        # 1 + 2 + 4 + 8 + 16 = 31. Here the last term of the sum is 16, not 5.
        # This suggests the second parameter might not be the mathematical "last term" of the sequence,
        # but perhaps the upper bound of the index or something else?
        # Wait, let's look at the standard geometric series sum formula S_n = a(r^n - 1)/(r-1).
        # If result is 31, a=1, r=2: 1*(2^n - 1)/1 = 31 => 2^n = 32 => n=5.
        # So there are 5 terms.
        # How does 'last_term=5' relate to n=5? It seems 'last_term' might be the exponent count or upper limit?
        # Let's check Example 2: a=1, l=5, r=4. Sum=341.
        # 1*(4^n - 1)/(3) = 341 => 4^n - 1 = 1023 => 4^n = 1024. 
        # 4^5 = 1024. So n=5.
        # Again, last_term=5 corresponds to n=5.

        # Check Example 3: a=2, l=6, r=3. Sum=728.
        # 2*(3^n - 1)/(2) = 728 => 3^n - 1 = 728 => 3^n = 729.
        # 3^6 = 729. So n=6.
        # Here last_term=6 corresponds to n=6.

        # Conclusion: The second parameter is NOT the last term value in the sequence.
        # It is the NUMBER OF TERMS (n).
        # The variable name "last_term" in the problem description is misleading based on the examples.
        # It is actually the count of terms to sum.
        # Let's re-verify with the function signature expectation.
        # If input (1, 5, 2) means a=1, count=5, r=2.
        # Series: 1, 2, 4, 8, 16. Sum = 31. Correct.
        # If input (1, 5, 4) means a=1, count=5, r=4.
        # Series: 1, 4, 16, 64, 256. Sum = 1+4+16+64+256 = 341. Correct.
        # If input (2, 6, 3) means a=2, count=6, r=3.
        # Series: 2, 6, 18, 54, 162, 486. Sum = 728. Correct.

        # Therefore, the function signature is sum_gp(first_term, number_of_terms, common_ratio).
        # The problem description calling the second argument "last_term" is technically incorrect
        # based on the provided assertions, but the logic for calculation is clear now:
        # The second argument is the number of terms 'n'.

        n = last_term
        if n <= 0:
            return 0
        return first_term * n

    else:
        # General case where ratio != 1
        n = last_term

        if n <= 0:
            return 0

        # Check for fractional powers if inputs are floats, but standard geometric series
        # usually implies integer n. If n is not integer, the concept of "n terms" is ambiguous.
        # Assuming n is intended to be an integer count.

        # Calculate sum using formula: S_n = a * (r^n - 1) / (r - 1)

        numerator_term = pow(common_ratio, n) - 1
        denominator_term = common_ratio - 1

        # Handle potential division by zero if r is very close to 1 (though we handled exact 1 above)
        if abs(denominator_term) < 1e-15:
            # Fallback to n * a if r is extremely close to 1 due to floating point precision
            return first_term * n

        product_a_num = first_term * numerator_term
        result = product_a_num / denominator_term

        return result

def sum_gp(first_term: Number, last_term: Number, common_ratio: Number) -> Number:
    """
    Finds the sum of a geometric progression series.

    Based on the provided assertions, the arguments are interpreted as:
    - first_term: The first number in the sequence.
    - last_term: The number of terms to sum (n).
    - common_ratio: The common ratio of the geometric progression.

    Args:
        first_term: The first term of the geometric progression.
        last_term: The number of terms to include in the sum.
        common_ratio: The common ratio between consecutive terms.

    Returns:
        The sum of the geometric progression.

    Raises:
        ValueError: If inputs are invalid or if the logic dictates an impossible series.
    """

    # Step 1: Validate inputs
    validate_input(first_term, last_term, common_ratio)

    # Extract validated values into local variables for clarity
    a = first_term
    n = last_term
    r = common_ratio

    # Step 2: Handle edge cases for count
    if n < 1:
        # If the number of terms is zero or negative, the sum is zero
        return 0.0 if isinstance(n, float) else 0

    # Step 3: Check for integer requirement for term count
    # Geometric series with discrete terms usually requires integer n.
    # If n is a float that isn't a whole number, we treat it as invalid for discrete counting
    # or round it? Given the problem context of assertions, n is an integer.
    # We will enforce that n is effectively an integer (or very close).
    if isinstance(n, float) and not n.is_integer():
        raise ValueError("The number of terms must be an integer.")

    # Step 4: Execute calculation logic based on ratio
    return calculate_geometric_series_sum(a, n, r)