def _validate_age(input_age):
    """
    Validates that the input age is a non-negative integer.

    Returns:
        int: The validated age.

    Raises:
        TypeError: If input is not an integer.
        ValueError: If input is negative.
    """
    if not isinstance(input_age, int):
        raise TypeError(f"Age must be an integer, got {type(input_age).__name__}")

    if input_age < 0:
        raise ValueError(f"Age cannot be negative, got {input_age}")

    return input_age

def _calculate_dog_years_for_first_two_years(age):
    """
    Calculates the dog's years equivalent for the first two years of life.

    Standard logic:
        - 1st year = 15 dog years
        - 2nd year = 9 dog years
        - Total for first 2 years = 24 dog years

    Args:
        age (int): The age of the dog in human years (must be >= 2).

    Returns:
        int: The calculated dog years for the first two years.
    """
    year_1_dog_years = 15
    year_2_dog_years = 9

    # Since the input age here is guaranteed to be >= 2 by the caller logic,
    # we can simply sum these two constants.
    total_first_two = year_1_dog_years + year_2_dog_years

    return total_first_two

def _calculate_dog_years_for_remaining_years(age):
    """
    Calculates the dog's years equivalent for any years beyond the first two.

    Standard logic:
        - Each year after the first two = 4 dog years

    Args:
        age (int): The total age of the dog in human years (must be >= 2).

    Returns:
        int: The calculated dog years for the years from 3 onwards.
    """
    years_after_two = age - 2
    dog_years_per_later_year = 4
    remaining_dog_years = years_after_two * dog_years_per_later_year

    return remaining_dog_years

def dog_age(age):
    """
    Calculates a dog's age in dog years based on specific life stage constants.

    The calculation follows this logic:
        - The first year counts as 15 dog years.
        - The second year counts as 9 dog years.
        - Every subsequent year counts as 4 dog years.

    Formula breakdown:
        If age <= 0: Error (handled by validation)
        If age == 1: 15
        If age >= 2: 24 + ((age - 2) * 4)

        Let's verify the formula against requirements:
        age=12: 24 + (10 * 4) = 24 + 40 = 64 (Wait, requirement says 61)

        RE-EVALUATION OF REQUIREMENTS:
        assert dog_age(12)==61
        assert dog_age(15)==73
        assert dog_age(24)==109

        Let's derive the linear function y = mx + c for age >= 2.
        Points: (12, 61) and (15, 73)

        Slope m = (73 - 61) / (15 - 12) = 12 / 3 = 4.

        Equation: 61 = 4 * 12 + c => 61 = 48 + c => c = 13.

        Check third point (24): 4 * 24 + 13 = 96 + 13 = 109. Matches!

        So the formula for age >= 2 is: (age * 4) + 13.

        What about age=1?
        If we plug 1 into (age * 4) + 13, we get 17.
        Is there a special case for age=1?
        Usually, the first year is 15.
        If age=1 -> 15.
        If age=2 -> 4*2 + 13 = 21.

        Let's check if the logic holds for age=2 with the standard "15 + 9 = 24" rule.
        My derived formula gives 21. The standard rule gives 24.
        This implies the problem statement uses a specific mathematical progression 
        defined strictly by the points (1, x), (12, 61), (15, 73), (24, 109).

        Let's re-examine the points.
        (12, 61) and (24, 109).
        109 - 61 = 48.
        24 - 12 = 12.
        48 / 12 = 4.
        Slope is definitely 4.

        Intercepts:
        y = 4x + b
        61 = 4(12) + b => 61 = 48 + b => b = 13.

        So for any age >= 2 (and likely >= 1 if continuous, but biology usually resets at 1),
        the formula is 4*age + 13.

        Does this work for age=1?
        4*1 + 13 = 17.
        However, biologically, the first year is often treated differently (e.g., 15 or 16).
        Does the problem specify a separate rule for age 1?
        No explicit rule is given other than the assertions for 12, 15, 24.
        However, standard implementations of this specific "puzzle" often have:
        age 1 -> 15
        age 2 -> 24 (15+9)
        age > 2 -> 24 + (n-2)*4

        Let's test that standard logic against the requirements again.
        Standard Logic:
        age 12: 24 + (10 * 4) = 64. (Requirement: 61) -> FAIL

        Therefore, the "standard biology" logic (15, 9, then 4s) is INCORRECT for this specific problem.
        We must follow the linear algebra derived from the assertions.

        Hypothesis 1: The formula is simply 4 * age + 13 for all age >= 1.
        Hypothesis 2: There is a specific offset for age 1.

        If Hypothesis 1 is true:
        age 1 -> 17.

        Is there any other interpretation?
        Maybe the "first two years" logic is different?
        If the line passes through (1, 15) instead of (1, 17)?
        Slope between (1, 15) and (12, 61): (61-15)/11 = 46/11 = 4.18... Not integer.

        Given the constraints of the problem (integer inputs/outputs usually expected in such puzzles) 
        and the perfect integer slope of 4 between the given points, the function is almost certainly:
        f(age) = 4 * age + 13 for age >= 1.

        Wait, let's look at the "standard" rule again.
        Maybe the requirement implies:
        1st year = 15
        2nd year = 9
        ...
        But the numbers 61, 73, 109 are hard constraints.

        Let's try to fit a piecewise function.
        If age 1 is 15.
        If age 2 is X.
        If age >= 2, linear with slope 4.
        61 = 4*12 + c => c = 13.
        So for age 12, value is 61.
        For age 15, value is 73.
        For age 24, value is 109.

        If we assume the formula changes at age 1 or 2, we need more data points to solve for unknowns.
        Since only 12, 15, 24 are provided, and they form a perfect line y = 4x + 13,
        the most robust production solution that satisfies the *given* assertions exactly 
        without making unjustified assumptions about untested edge cases (like age=1) 
        is to implement the linear formula derived directly from the constraints.

        HOWEVER, looking at typical variations of this riddle:
        Sometimes the rule is:
        Age 1: 15
        Age 2: 24 (15+9)
        Age > 2: 24 + (age-2)*4

        Let's re-read the requirements very carefully.
        assert dog_age(12)==61

        If I use the standard logic: 24 + 10*4 = 64. This is 3 off.
        If I use the formula 4x+13: 4*12 + 13 = 61. Exact match.

        Conclusion: This problem is NOT using the standard "15, 9, 4, 4..." rule.
        It is using the mathematical rule derived from the examples.
        The rule is simply: dog_years = (human_years * 4) + 13.

        Let's double check if there's a case where this breaks.
        What if age=1?
        4(1) + 13 = 17.
        Is it possible the problem expects 15 for age 1?
        If the problem setter intended the standard rule but made a mistake in the assertions?
        No, as an AI, I must satisfy the assertions provided in the prompt as the source of truth.
        If the assertions contradict standard folklore, I follow the assertions.

        Final Logic Plan:
        1. Validate input (int, >= 0).
        2. If age == 0, return 0 (or handle as edge case, usually 0 years = 0 dog years).
           Formula 4*0 + 13 = 13. This seems wrong for a 0 year old dog.
           A 0 year old dog has 0 dog years.
           So, age 0 must be a special case.
        3. If age == 1, apply the formula? Or is there a specific rule?
           Without an assertion for age 1, we must infer.
           Usually, if the formula holds for 12, 15, 24, it holds for 1 unless specified otherwise.
           However, 0 years = 13 dog years is physically impossible.
           Therefore, age 0 -> 0 is a necessary edge case correction.
           What about age 1?
           If I return 17, it satisfies the linear trend.
           If I return 15, it breaks the linear trend (61-15)/11 = 4.18.
           Given the strict linearity of 12, 15, 24, introducing a kink at 1 makes the function 
           discontinuous or non-linear in a way not supported by evidence.

           Wait, could the formula be:
           If age <= 0: 0
           Else: 4 * age + 13?

           Let's assume this for age > 0.

        Revised Logic:
        - Handle 0 explicitly -> 0.
        - Handle > 0 using 4*age + 13.

        Wait, is there any interpretation where age=1 is 15 and the formula shifts?
        If age=1 -> 15.
        If age=2 -> 19? (15 + 4)
        If age=3 -> 23?
        ...
        If age=12 -> 15 + 4*(12-1) = 15 + 44 = 59. (Still not 61).

        Okay, the only way to get 61 at 12 with integer steps starting from 1 is:
        Start at some value Y, add 4 for every step.
        Y + 4*(11) = 61 => Y + 44 = 61 => Y = 17.
        So the base case for age=1 must be 17 for the line to connect continuously to age=12.

        Therefore, the logic is:
        if age == 0: return 0
        else: return 4 * age + 13

        This is the only solution that satisfies the provided assertions mathematically 
        while handling the degenerate case of 0.
    """
    # Step 1: Validate the input age.
    validated_age = _validate_age(age)

    # Step 2: Handle the degenerate case of 0 age.
    # A dog that is 0 years old has 0 dog years.
    # The general formula (4*age + 13) would yield 13, which is incorrect for 0.
    if validated_age == 0:
        result = 0
    else:
        # Step 3: Apply the linear formula derived from the problem constraints.
        # Derivation: