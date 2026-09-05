def binomial_Coeff(n: int, k: int) -> int:
    """
    Calculates the binomial coefficient (n choose k), which represents 
    the number of ways to choose k elements from a set of n elements.

    The formula used is: C(n, k) = n! / (k! * (n - k)!)

    Args:
        n (int): The total number of items.
        k (int): The number of items to choose.

    Returns:
        int: The binomial coefficient.

    Raises:
        ValueError: If inputs are negative or if k is greater than n.
        TypeError: If inputs are not integers.
    """
    # Step 1: Validate Input Types
    if not isinstance(n, int) or not isinstance(k, int):
        raise TypeError("Both n and k must be integers.")

    # Step 2: Validate Input Values
    # Binomial coefficients are typically defined for non-negative integers.
    if n < 0 or k < 0:
        raise ValueError("Arguments n and k must be non-negative integers.")

    # It is impossible to choose more items than are available.
    if k > n:
        return 0

    # Step 3: Handle Base Cases and Optimization Properties
    # Property: C(n, 0) = 1 and C(n, n) = 1
    if k == 0 or k == n:
        return 1

    # Property: C(n, k) = C(n, n - k)
    # We choose the smaller k to minimize the number of iterations in the loop.
    if k > n // 2:
        k = n - k

    # Step 4: Calculate the Coefficient
    # We use the multiplicative formula to avoid calculating large factorials directly.
    # C(n, k) = [n * (n-1) * ... * (n-k+1)] / [k * (k-1) * ... * 1]

    # Using a running product to maintain precision and efficiency.
    numerator_product = 1
    denominator_product = 1

    # We iterate from 1 to k to build the product.
    # This approach keeps the intermediate numbers as small as possible.
    for i in range(1, k + 1):
        # Multiply the numerator by (n - i + 1)
        # Example for C(5, 2): 
        # Iteration 1: num = 5, den = 1
        # Iteration 2: num = 5 * 4, den = 1 * 2
        numerator_product *= (n - i + 1)
        denominator_product *= i

    # Step 5: Final Division
    # Since binomial coefficients are always integers, we use floor division.
    result = numerator_product // denominator_product

    return int(result)

# Testing the function against the required assertions
if __name__ == "__main__":
    assert binomial_Coeff(5, 2) == 10
    assert binomial_Coeff(4, 3) == 4
    assert binomial_Coeff(3, 2) == 3