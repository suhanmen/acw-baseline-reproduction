import math
from typing import Tuple, Union

Number = Union[int, float]
Dimension = Tuple[Number, Number, Number]

def validate_dimension_value(value: Number, name: str) -> None:
    """
    Validates that a single dimension value is a finite number.

    Args:
        value: The value to validate.
        name: A descriptive name for the value in error messages.

    Raises:
        TypeError: If the value is not a number.
        ValueError: If the value is not finite (e.g., infinity or NaN).
        ValueError: If the value is negative.
    """
    # Check for type
    if not isinstance(value, (int, float)):
        raise TypeError(
            f"The {name} must be an integer or a float, "
            f"but got {type(value).__name__} instead."
        )

    # Check for infinity or NaN
    if not math.isfinite(value):
        raise ValueError(
            f"The {name} must be a finite number, "
            f"but got {value!r} (inf or nan detected)."
        )

    # Check for negative numbers
    if value < 0:
        raise ValueError(
            f"The {name} must be non-negative, but got {value}."
        )


def validate_dimensions(dimensions: Dimension) -> None:
    """
    Validates a tuple of three dimensions for a cuboid.

    Args:
        dimensions: A tuple of (length, width, height).

    Raises:
        TypeError: If the input is not a tuple or does not contain three elements.
        TypeError: If any element is not a number.
        ValueError: If any element is not finite or negative.
    """
    # Check if input is a tuple
    if not isinstance(dimensions, tuple):
        raise TypeError(
            "Dimensions must be provided as a tuple of three numbers, "
            f"but got {type(dimensions).__name__} instead."
        )

    # Check for correct number of elements
    if len(dimensions) != 3:
        raise ValueError(
            f"Dimensions must contain exactly 3 values (length, width, height), "
            f"but got {len(dimensions)} values."
        )

    # Validate each individual dimension
    index_labels = ["length", "width", "height"]
    for index, (value, label) in enumerate(zip(dimensions, index_labels)):
        validate_dimension_value(value, label)


def calculate_volume(dimensions: Dimension) -> float:
    """
    Calculates the volume of a cuboid given its dimensions.

    Args:
        dimensions: A tuple of (length, width, height).

    Returns:
        The calculated volume as a float.
    """
    length, width, height = dimensions

    # Calculate intermediate products explicitly for clarity
    base_area = length * width
    final_volume = base_area * height

    return final_volume


def volume_cuboid(dimensions: Dimension) -> float:
    """
    Calculates the volume of a cuboid with strict input validation.

    This function accepts a tuple of three numbers representing the length,
    width, and height of a cuboid. It performs rigorous validation to ensure
    inputs are finite, non-negative numbers, and that the correct number of
    dimensions is provided. It then calculates the volume by multiplying
    the three dimensions together.

    Args:
        dimensions: A tuple of three numbers (length, width, height).

    Returns:
        The volume of the cuboid.

    Raises:
        TypeError: If the input format or element types are incorrect.
        ValueError: If the dimensions are invalid (e.g., negative, infinity, NaN).
    """
    validate_dimensions(dimensions)
    return calculate_volume(dimensions)