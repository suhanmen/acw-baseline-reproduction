from typing import Union

def dog_age(human_years: Union[int, float]) -> int:
    """
    Calculates a dog's age in dog years based on the provided human years.

    The calculation follows the pattern derived from the provided test cases:
    - 12 human years -> 61 dog years
    - 15 human years -> 73 dog years
    - 24 human years -> 109 dog years

    By analyzing the differences:
    (15 - 12) = 3 human years -> (73 - 61) = 12 dog years. Difference = 4.
    (24 - 15) = 9 human years -> (109 - 73) = 36 dog years. Difference = 4.

    The relationship is linear: dog_years = (human_years * 4) + constant.
    For 12: (12 * 4) + C = 61 => 48 + C = 61 => C = 13.
    Verification for 24: (24 * 4) + 13 = 96 + 13 = 109.

    Args:
        human_years (Union[int, float]): The age of the dog in human years.

    Returns:
        int: The age of the dog in dog years.

    Raises:
        ValueError: If human_years is negative.
        TypeError: If human_years is not an integer or a float.
    """

    # --- Input Validation ---

    # Check if the input is a numeric type
    if not isinstance(human_years, (int, float)):
        raise TypeError(
            f"Expected human_years to be an int or float, "
            f"but received {type(human_years).__name__}."
        )

    # Check if the input is logically valid (age cannot be negative)
    if human_years < 0:
        raise ValueError(
            f"Human years cannot be negative. Received: {human_years}"
        )

    # --- Calculation ---

    # Multiplier constant: Every human year is roughly 4 dog years
    multiplier: float = 4.0

    # Offset constant: Derived from the test cases provided
    # (Age * 4) + 13 = Dog Age
    offset: float = 13.0

    # Calculate the raw dog age
    # We perform the calculation as floats to maintain precision 
    # before the final conversion to integer.
    calculated_dog_age_float: float = (human_years * multiplier) + offset

    # Convert to an integer as the requirement implies integer outputs
    # We use round() to handle cases where float inputs might result 
    # in slight precision errors (e.g., 12.00000001).
    final_dog_age: int = int(round(calculated_dog_age_float))

    return final_dog_age

if __name__ == "__main__":
    # The following assertions are provided in the problem description
    assert dog_age(12) == 61
    assert dog_age(15) == 73
    assert dog_age(24) == 109