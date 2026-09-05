def bf(planet1, planet2):
    '''
    There are eight planets in our solar system: the closerst to the Sun 
    is Mercury, the next one is Venus, then Earth, Mars, Jupiter, Saturn, 
    Uranus, Neptune.
    Write a function that takes two planet names as strings planet1 and planet2. 
    The function should return a tuple containing all planets whose orbits are 
    located between the orbit of planet1 and the orbit of planet2, sorted by 
    the proximity to the sun. 
    The function should return an empty tuple if planet1 or planet2
    are not correct planet names. 
    Examples
    bf("Jupiter", "Neptune") ==> ("Saturn", "Uranus")
    bf("Earth", "Mercury") ==> ("Venus")
    bf("Mercury", "Uranus") ==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    '''

    # Define the ordered list of planets by proximity to the Sun
    PLANETS = [
        "Mercury",
        "Venus",
        "Earth",
        "Mars",
        "Jupiter",
        "Saturn",
        "Uranus",
        "Neptune"
    ]

    # Set of valid planet names for O(1) lookup
    VALID_PLANET_SET = set(PLANETS)

    # Validate inputs: check if both planet1 and planet2 are valid planet names
    is_valid1 = planet1 in VALID_PLANET_SET
    is_valid2 = planet2 in VALID_PLANET_SET

    # If either input is invalid, return an empty tuple immediately
    if not is_valid1 or not is_valid2:
        return ()

    # Get the index of each valid planet in the PLANETS list
    try:
        index1 = PLANETS.index(planet1)
    except ValueError:
        # This case should not be reached due to the validation above,
        # but is included for explicit error handling completeness.
        return ()

    try:
        index2 = PLANETS.index(planet2)
    except ValueError:
        # This case should not be reached due to the validation above,
        # but is included for explicit error handling completeness.
        return ()

    # Determine the start and end indices for the slice
    # We need to ensure we handle cases where planet1 is beyond planet2 (e.g., Earth, Mercury)
    if index1 < index2:
        start_index = index1 + 1
        end_index = index2
    else:
        # planet1 is further from the Sun than planet2 (or equal, though equal yields empty)
        start_index = index2 + 1
        end_index = index1

    # Extract the planets between the two indices
    # The slice [start_index:end_index] excludes end_index naturally
    intermediate_planets = PLANETS[start_index:end_index]

    # Convert the list result to a tuple as required by the problem statement
    result_tuple = tuple(intermediate_planets)

    return result_tuple