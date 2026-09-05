import math

def binomial_probability(n: int, k: int, p: float) -> float:
    """
    Computes the binomial probability: P(X = k) = (n choose k) * (p^k) * (1-p)^(n-k)

    Args:
        n (int): The number of independent trials.
        k (int): The number of successful outcomes.
        p (float): The probability of success in a single trial.

    Returns:
        float: The binomial probability.

    Raises:
        ValueError: If input parameters are out of logical bounds.
        TypeError: If inputs are not of the expected types.
    """
    # --- Input Validation ---

    # Validate n (number of trials)
    if not isinstance(n, int):
        raise TypeError(f"n must be an integer, got {type(n).__name__}")
    if n < 0:
        raise ValueError(f"n (number of trials) cannot be negative, got {n}")

    # Validate k (number of successes)
    if not isinstance(k, int):
        raise TypeError(f"k must be an integer, got {type(k).__name__}")
    if k < 0:
        raise ValueError(f"k (number of successes) cannot be negative, got {k}")
    if k > n:
        # In binomial distribution, k cannot exceed n. 
        # The probability is mathematically 0 in this case.
        return 0.0

    # Validate p (probability)
    if not isinstance(p, (int, float)):
        raise TypeError(f"p must be a float or int, got {type(p).__name__}")
    if p < 0.0 or p > 1.0:
        raise ValueError(f"p (probability) must be between 0 and 1 inclusive, got {p}")

    # --- Handle Degenerate Cases ---

    # If no trials are performed
    if n == 0:
        # If k is 0, probability is 1.0, else 0.0 (but k > n is handled above)
        return 1.0 if k == 0 else 0.0

    # If probability of success is 0
    if p == 0.0:
        # Probability is 1 only if we want 0 successes
        return 1.0 if k == 0 else 0.0

    # If probability of success is 1
    if p == 1.0:
        # Probability is 1 only if we want n successes
        return 1.0 if k == n else 0.0

    # --- Computation Logic ---

    # Formula: P(X = k) = (nCk) * (p^k) * (1-p)^(n-k)

    # 1. Calculate Combinations: nCk = n! / (k! * (n-k)!)
    # We use math.comb for precision and efficiency (available in Python 3.8+)
    combinations = math.comb(n, k)

    # 2. Calculate Success Component: p^k
    # Using pow() or ** operator
    prob_success = math.pow(p, k)

    # 3. Calculate Failure Component: (1-p)^(n-k)
    prob_failure_base = 1.0 - p
    num_failures = n - k
    prob_failure = math.pow(prob_failure_base, num_failures)

    # 4. Final result
    result = combinations * prob_success * prob_failure

    return result