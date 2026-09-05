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
    planets = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")

    if planet1 not in planets or planet2 not in planets:
        return ()

    idx1 = planets.index(planet1)
    idx2 = planets.index(planet2)

    start = min(idx1, idx2)
    end = max(idx1, idx2)

    # The problem asks for planets strictly between the two orbits.
    # If planet1 is Mercury (0) and planet2 is Venus (1), result is empty.
    # If planet1 is Earth (2) and planet2 is Mercury (0), result is Venus (1).
    result = tuple(planets[i] for i in range(start + 1, end))
    return result