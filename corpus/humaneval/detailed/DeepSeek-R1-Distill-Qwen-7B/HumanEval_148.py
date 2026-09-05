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

    # Mapping of planet names to their order from the Sun
    planet_order = {
        'Mercury': 1,
        'Venus': 2,
        'Earth': 3,
        'Mars': 4,
        'Jupiter': 5,
        'Saturn': 6,
        'Uranus': 7,
        'Neptune': 8
    }

    # Helper function to validate and return the order of a planet
    def get_planet_info(planet):
        if planet not in planet_order:
            return None
        return planet_order[planet]

    # Helper function to get the list of planets between two orders
    def get_between(start, end):
        if start > end:
            return []
        # Generate all planets from start to end (exclusive)
        return [planet for order in range(start, end) for planet in planet_order if planet_order[planet] == order]

    # Validate both planets
    if get_planet_info(planet1) is None or get_planet_info(planet2) is None:
        return ()

    # Get the order of both planets
    order1 = get_planet_info(planet1)
    order2 = get_planet_info(planet2)

    # Determine the lower and higher order
    lower = min(order1, order2)
    higher = max(order1, order2)

    # Get all planets between the two orders
    planets_between = get_between(lower, higher)

    # Sort the planets by their order (they are already in order)
    # However, if the lower is less than higher, planets_between will be in order
    # Otherwise, it will be empty list.

    return tuple(planets_between)