from typing import Union, Tuple

Number = Union[int, float]

def _validate_edge_length(edge_length: Number) -> Number:
    """
    Validates that the provided edge length is a number and positive.

    Raises:
        TypeError: If edge_length is not an int or float.
        ValueError: If edge_length is zero or negative.
    """
    if not isinstance(edge_length, (int, float)):
        raise TypeError(
            f"Expected a number (int or float) for edge length, "
            f"got {type(edge_length).__name__} instead."
        )

    if not isinstance(edge_length, bool):
        if edge_length <= 0:
            raise ValueError(
                f"Expected a positive number for edge length, "
                f"got {edge_length}. Edge length must be strictly greater than zero."
            )

    return edge_length

def _calculate_single_face_area(edge_length: Number) -> Number:
    """
    Calculates the area of one face of the cube.

    A face of a cube is a square with side length equal to the cube's edge.
    Area = edge_length * edge_length
    """
    return edge_length * edge_length

def _calculate_lateral_surface_area(edge_length: Number) -> Number:
    """
    Calculates the lateral surface area of the cube.

    The lateral surface area of a cube consists of 4 of its 6 faces.
    The top and bottom faces are excluded from the 'lateral' area.

    Formula:
        Lateral Area = 4 * (area of one face)
                    = 4 * (edge_length^2)

    :param edge_length: The length of the edge of the cube.
    :return: The lateral surface area as a number.
    """
    face_area = _calculate_single_face_area(edge_length)
    lateral_area = 4 * face_area
    return lateral_area

def lateralsurface_cube(edge_length: Number) -> Number:
    """
    Calculates and returns the lateral surface area of a cube given its edge length.

    The lateral surface area is the total area of the four vertical faces of the cube,
    excluding the top and bottom faces.

    The formula used is: Lateral Area = 4 * s^2, where 's' is the edge length.

    Args:
        edge_length: The length of one edge of the cube. Must be a positive number.

    Returns:
        The lateral surface area of the cube.

    Raises:
        TypeError: If edge_length is not a valid numeric type.
        ValueError: If edge_length is zero or negative.

    Examples:
        lateralsurface_cube(5) -> 100 (4 faces * 5 * 5)
        lateralsurface_cube(9) -> 324 (4 faces * 9 * 9)
        lateralsurface_cube(10) -> 400 (4 faces * 10 * 10)
    """
    validated_length = _validate_edge_length(edge_length)
    result = _calculate_lateral_surface_area(validated_length)
    return result