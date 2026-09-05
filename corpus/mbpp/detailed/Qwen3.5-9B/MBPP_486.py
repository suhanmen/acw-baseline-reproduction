import math
from typing import Union

Number = Union[int, float]


def _validate_inputs(
    n: Number,
    k: Number,
    p: Number,
) -> None:
    """
    Validate the input arguments for the binomial probability calculation.

    Parameters
    ----------
    n : Number
        The number of trials (must be a non-negative integer).
    k : Number
        The number of successful outcomes (must be an integer between 0 and n inclusive).
    p : Number
        The probability of success in a single trial (must be between 0.0 and 1.0 inclusive).

    Raises
    ------
    TypeError
        If any argument is not an int or a float.
    ValueError
        If n is negative, if k is not an integer, if k is out of bounds [0, n],
        or if p is outside the range [0.0, 1.0].
    """
    # Check types
    if not isinstance(n, (int, float)):
        raise TypeError(f"Expected 'n' to be an int or float, got {type(n).__name__}")
    if not isinstance(k, (int, float)):
        raise TypeError(f"Expected 'k' to be an int or float, got {type(k).__name__}")
    if not isinstance(p, (int, float)):
        raise TypeError(f"Expected 'p' to be an int or float, got {type(p).__name__}")

    # Convert to float for range checking to handle potential float inputs for k
    n_float = float(n)
    k_float = float(k)
    p_float = float(p)

    # Check n constraints
    if n_float < 0:
        raise ValueError(f"Expected 'n' to be non-negative, got {n_float}")
    if not math.isfinite(n_float):
        raise ValueError(f"Expected 'n' to be a finite number, got {n_float}")

    # Check k constraints
    if math.isnan(k_float) or math.isinf(k_float):
        raise ValueError(f"Expected 'k' to be a finite number, got {k_float}")
    if k_float != int(k_float):
        # This check ensures k is mathematically an integer
        raise ValueError(f"Expected 'k' to be an integer, got {k}")

    # Check if k is within valid range [0, n]
    if k_float < 0 or k_float > n_float:
        raise ValueError(f"Expected 'k' to be between 0 and {n_float}, got {k_float}")

    # Check p constraints
    if p_float < 0.0 or p_float > 1.0:
        raise ValueError(f"Expected 'p' to be between 0.0 and 1.0, got {p_float}")
    if not math.isfinite(p_float):
        raise ValueError(f"Expected 'p' to be a finite number, got {p_float}")


def _calculate_factorial(num: int) -> int:
    """
    Calculate the factorial of a non-negative integer.

    Parameters
    ----------
    num : int
        A non-negative integer.

    Returns
    -------
    int
        The factorial of num.
    """
    if num < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if num == 0:
        return 1

    result = 1
    for i in range(1, num + 1):
        result = result * i
    return result


def _compute_binomial_coefficient(n: int, k: int) -> int:
    """
    Compute the binomial coefficient C(n, k) = n! / (k! * (n-k)!).
    Uses integer arithmetic to avoid floating point inaccuracies for the coefficient itself.

    Parameters
    ----------
    n : int
        The total number of items (must be >= k).
    k : int
        The number of items to choose.

    Returns
    -------
    int
        The binomial coefficient.
    """
    if k < 0 or k > n:
        raise ValueError(f"k ({k}) must be between 0 and {n}.")

    # Optimization: C(n, k) == C(n, n-k)
    # Use the smaller k to minimize calculations
    k_effective = min(k, n - k)

    if k_effective == 0:
        return 1

    numerator = 1
    denominator = 1

    # Compute C(n, k) iteratively: n * (n-1) * ... * (n-k+1) / (1 * 2 * ... * k)
    for i in range(k_effective):
        numerator = numerator * (n - i)
        denominator = denominator * (i + 1)

        # Perform division at each step to keep numbers manageable,
        # but since we know the result is an integer, we can multiply numerator
        # by the denominator terms and divide by denominator product at the end
        # OR, more safely for very large numbers, multiply and divide incrementally
        # ensuring divisibility.
        # However, to keep it simple and robust for typical ranges:
        pass

    # Re-calculate using the iterative multiplication/division to ensure exact integer result
    # where possible, or just compute full factorials if range is small.
    # Given the problem constraints (n up to 12 in tests), direct factorial is safe.
    # But for a "production grade" generic function, let's use the multiplicative approach carefully.

    coeff = 1
    for i in range(k_effective):
        coeff = coeff * (n - i)
        coeff = coeff // (i + 1)

    return coeff


def binomial_probability(n: Number, k: Number, p: Number) -> float:
    """
    Compute the binomial probability of getting exactly k successes in n trials
    with success probability p per trial.

    Formula: P(X=k) = C(n, k) * p^k * (1-p)^(n-k)

    Parameters
    ----------
    n : Number
        Number of independent trials (non-negative integer).
    k : Number
        Number of successful outcomes (integer between 0 and n).
    p : Number
        Probability of success in a single trial (float between 0.0 and 1.0).

    Returns
    -------
    float
        The calculated binomial probability.

    Raises
    ------
    TypeError
        If inputs are not numeric.
    ValueError
        If inputs are out of valid ranges.
    """
    # Step 1: Validate all inputs explicitly
    _validate_inputs(n, k, p)

    # Step 2: Convert inputs to appropriate types
    n_int = int(n)
    k_int = int(k)
    p_float = float(p)

    # Step 3: Calculate the binomial coefficient C(n, k)
    combinations = _compute_binomial_coefficient(n_int, k_int)

    # Step 4: Calculate p^k
    probability_of_success_power = math.pow(p_float, k_int)

    # Step 5: Calculate (1-p)^(n-k)
    probability_of_failure = 1.0 - p_float
    probability_of_failure_power = math.pow(probability_of_failure, n_int - k_int)

    # Step 6: Combine terms: C(n, k) * p^k * (1-p)^(n-k)
    result = float(combinations) * probability_of_success_power * probability_of_failure_power

    return result