from typing import Tuple, List

def bf(planet1: str, planet2: str) -> Tuple[str, ...]:
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

    # Define the ordered list of planets based on proximity to the Sun
    planets_list = [
        "Mercury",
        "Venus",
        "Earth",
        "Mars",
        "Jupiter",
        "Saturn",
        "Uranus",
        "Neptune"
    ]

    def get_planet_index(name: str) -> int:
        """
        Helper function to find the 0-based index of a planet name.
        Returns -1 if the planet name is invalid.
        """
        # Normalize input to ensure casing doesn't cause issues, 
        # though the problem implies strict matching.
        # Given the examples, we assume the input will match the casing of planets_list.
        for index, planet in enumerate(planets_list):
            if name == planet:
                return index
        return -1

    # Validate input planet1
    index1 = get_planet_index(planet1)
    if index1 == -1:
        return ()

    # Validate input planet2
    index2 = get_planet_index(planet2)
    if index2 == -1:
        return ()

    # Determine the range boundaries
    # The problem asks for planets BETWEEN the two orbits.
    # We need to find the minimum and maximum indices to handle inputs 
    # regardless of which planet is "closer" to the Sun.
    start_index = min(index1, index2)
    end_index = max(index1, index2)

    # The "between" logic:
    # If planet1 is Earth (index 2) and planet2 is Mercury (index 0),
    # the result should be Venus (index 1).
    # This implies we want all planets with indices strictly between start_index and end_index.

    # If the indices are the same or adjacent (e.g., Mercury and Venus),
    # there are no planets between them.
    if end_index - start_index <= 1:
        return ()

    # Collect the planets located between the two boundaries
    intermediate_planets = []

    # We iterate from start_index + 1 to end_index - 1 (exclusive of boundaries)
    for i in range(start_index + 1, end_index):
        intermediate_planets.append(planets_list[i])

    # Convert the list to a tuple as required by the signature
    result = tuple(intermediate_planets)

    return result