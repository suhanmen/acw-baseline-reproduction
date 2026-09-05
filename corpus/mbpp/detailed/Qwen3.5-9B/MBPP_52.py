from __future__ import annotations

import math
from typing import Any, Optional, Union

Number = Union[int, float]


def _validate_base(value: Any, param_name: str = "base") -> None:
    """
    Validate that the given value is a valid positive number for the base of a parallelogram.

    A valid base must be:
    1. A numeric type (int or float).
    2. Strictly greater than zero.

    Parameters:
        value: The value to validate.
        param_name: The name of the parameter for error messages.

    Raises:
        TypeError: If value is not a number.
        ValueError: If value is less than or equal to zero.
    """
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        raise TypeError(
            f"The parameter '{param_name}' must be a number (int or float), "
            f"not {type(value).__name__}."
        )

    if value <= 0:
        raise ValueError(
            f"The parameter '{param_name}' must be strictly greater than zero. "
            f"Received {value}."
        )


def _validate_height(value: Any, param_name: str = "height") -> None:
    """
    Validate that the given value is a valid positive number for the height of a parallelogram.

    A valid height must be:
    1. A numeric type (int or float).
    2. Strictly greater than zero.

    Parameters:
        value: The value to validate.
        param_name: The name of the parameter for error messages.

    Raises:
        TypeError: If value is not a number.
        ValueError: If value is less than or equal to zero.
    """
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        raise TypeError(
            f"The parameter '{param_name}' must be a number (int or float), "
            f"not {type(value).__name__}."
        )

    if value <= 0:
        raise ValueError(
            f"The parameter '{param_name}' must be strictly greater than zero. "
            f"Received {value}."
        )


def _calculate_area(base: Number, height: Number) -> Number:
    """
    Calculate the area of a parallelogram using the formula: Area = base * height.

    Parameters:
        base: The length of the base.
        height: The perpendicular height.

    Returns:
        The calculated area as a number.
    """
    area_result = base * height
    return area_result


def parallelogram_area(base: Number, height: Number) -> Number:
    """
    Calculate the area of a parallelogram.

    The area of a parallelogram is calculated as the product of its base and its corresponding height.
    This function includes rigorous input validation to ensure the mathematical integrity of the result.

    Mathematical Formula:
        Area = base × height

    Parameters:
        base (int or float): The length of the base of the parallelogram.
                              Must be a positive number.
        height (int or float): The height of the parallelogram (perpendicular distance between bases).
                               Must be a positive number.

    Returns:
        int or float: The calculated area of the parallelogram.

    Raises:
        TypeError: If either 'base' or 'height' is not a numeric type (int or float).
        ValueError: If either 'base' or 'height' is less than or equal to zero.

    Examples:
        >>> parallelogram_area(10, 20)
        200
        >>> parallelogram_area(15, 20)
        300
        >>> parallelogram_area(8, 9)
        72
        >>> parallelogram_area(0, 5)
        ValueError: ...
        >>> parallelogram_area(5, 0)
        ValueError: ...
        >>> parallelogram_area(-5, 10)
        ValueError: ...
    """
    # Step 1: Validate the 'base' parameter explicitly.
    _validate_base(base, param_name="base")

    # Step 2: Validate the 'height' parameter explicitly.
    _validate_height(height, param_name="height")

    # Step 3: Compute the area using the validated dimensions.
    return _calculate_area(base, height)