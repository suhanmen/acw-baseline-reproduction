def binomial_probability(n, k, p):
    """
    Compute the binomial probability for given parameters.

    Args:
        n (int): Number of trials.
        k (int): Number of successes.
        p (float): Probability of success on a single trial.

    Returns:
        float: The binomial probability.

    Raises:
        ValueError: If inputs are invalid.
    """
    # Validate inputs
    if not isinstance(n, int) or not isinstance(k, int) or not isinstance(p, float):
        raise ValueError("Invalid input types.")
    if n < 0 or k < 0 or k > n:
        raise ValueError("Invalid values for n and k.")
    if p < 0.0 or p > 1.0:
        raise ValueError("Invalid probability value.")

    # Compute binomial coefficient
    def binomial_coefficient(n, k):
        if k == 0 or k == n:
            return 1
        k = min(k, n - k)  # Take advantage of symmetry
        numerator = 1
        for i in range(1, k + 1):
            numerator *= (n - i + 1)
        denominator = 1
        for i in range(1, k + 1):
            denominator *= i
        return numerator // denominator

    # Compute probability components
    binom_coeff = binomial_coefficient(n, k)
    p_power = p ** k
    q_power = (1 - p) ** (n - k)

    # Calculate the probability
    probability = binom_coeff * p_power * q_power

    return probability

# Test the function with the given assertions
def test_binomial_probability():
    assert binomial_probability(10, 5, 1.0/3) == 0.13656454808718185
    assert binomial_probability(11, 6, 2.0/4) == 0.2255859375
    assert binomial_probability(12, 7, 3.0/5) == 0.227030335488

# Run the tests
test_binomial_probability()